#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from calendar import timegm
from collections import Counter, defaultdict
from copy import deepcopy
from datetime import date, timedelta
from functools import cmp_to_key
import json
from math import ceil, floor

SEASON = 15
# Season 14 registrations.
REGISTRATION_CLOSE_DATE = date(2023, 4, 27)
REGISTRATIONS = [16066, 6793, 11913, 17607, 7387, 7714, 15899, 3952, 17239,
                 11442, 18246, 13710, 6881, 5292, 14769, 9156, 16401, 12022,
                 8869, 6430, 13705, 6771, 7304, 10588]

# Season 13 registrations.
#REGISTRATION_CLOSE_DATE = date(2022, 9, 29)
#REGISTRATIONS = [6793, 11913, 11099, 11442, 3952, 15899, 8869, 5292, 13710, 15428, 16338, 7387,
#                 6881, 14769, 7714, 16066, 12957, 9984, 6771, 6751, 16222, 6430, 12283, 13705,
#                 15421, 7304]
# Season 12 registrations.
#REGISTRATION_CLOSE_DATE = date(2022, 4, 21)
#REGISTRATIONS = [7304, 6771, 6430, 11435, 3952, 8869, 4527, 15421, 16222, 11442,
#                 6793, 16066, 5292, 13710, 6941, 15899, 11913, 7617, 11099, 16401,
#                 7387, 7714, 15428, 10549, 6881, 16338, 9800, 14769, 13086,
#                 16677, 16889, 11855] # 6751 (Tailix)
# Season 11 registrations.
#REGISTRATION_CLOSE_DATE = date(2021, 10 , 8)
#REGISTRATIONS = [9599, 13705, 11705, 7304, 6771, 9877, 7644, 3952, 11435, 8869, 4527, 6766, 6430, 6680, 11855, 15421, 11442, 6793, 7591, 7813, 5292, 13710, 7617, 11913, 12261, 11099, 7714, 12654, 7387, 6751, 13096, 6861, 8860]
# Season 10 registrations.
#REGISTRATION_CLOSE_DATE = date(2020, 11 , 29)
#REGISTRATIONS = [9599, 6771, 7304, 3952, 6430, 7644, 4527, 8869, 6680, 10757, 11435, 11705, 13710, 5292, 11442, 7813, 7299, 8269, 11913, 11855, 6881, 7387, 12964, 7714, 13096, 6891, 7787, 8860, 13060, 13258, 7617, 9342, 10569, 12892, 13574, 13674]


TARGET_DIVISION_SIZE = 12
DIVISION_NAMES = ['Masters', 'Minions', 'Recruits']

with open('docs/data/players.json') as players_file:
    player_names = json.load(players_file)

# Continuity ranking (Nb. Only season finishers are ranked)
# * Season forfeits are placed last in their division
# * Win percentage (for parallel divisions)
# * Playoff/tiebreaker result (if relevant)
# * Points
# * Head-to-head results (recursively)
# * Fewer strikes
# * Length of current streak of completed RAGL seasons
# * Forum id (lower is better)

# Find the length of each player's streaks of completed seasons.
completed_seasons = Counter()
for season in range(1, SEASON):
    completed_season = defaultdict(bool)
    with open('docs/data/standings/s{:02d}.json'.format(season)) as standings_file:
        data = json.load(standings_file)
        for division in data['groups'].values():
            for group in division.values():
                for player in group:
                    if 'seasonForfeit' not in player or not player['seasonForfeit']:
                        completed_season[player['id']] = True
    for player_id in completed_seasons.keys():
        if not completed_season[player_id]:
            completed_seasons[player_id] = 0
    for player_id, completed in completed_season.items():
        if completed:
            completed_seasons[player_id] += 1

def isSeasonForfeit(player):
    return 'seasonForfeit' in player and player['seasonForfeit']

def winPercentage(player):
    if 'won' in player and 'played' in player and player['played'] != 0:
        return player['won'] / player['played']
    return 0

def group_rank(player):
    """Use the previous season's sort fields to create a rank for a player."""
    rank = []
    for fieldDirection in order:
        for field, direction in fieldDirection.items():
            if field in player:
                if direction == 'ASC':
                    rank.append(-player[field])
                else:
                    rank.append(player[field])
            else:
                rank.append(0)
    return rank

def division_player_rank(order, playoff_results, playerA, playerB):
    """Compare two players and return positive if A is better, or negative if B is better."""
    # Season forfeit is always the first ranking field.
    if isSeasonForfeit(playerA) != isSeasonForfeit(playerB):
        return -1 if isSeasonForfeit(playerA) else 1
    # If the player took part in a playoff then this is more important than the group stage.
    if playoff_results[playerA['id']] != playoff_results[playerB['id']]:
        return 1 if playoff_results[playerA['id']] > playoff_results[playerB['id']] else -1
    # Win percentage is used for parallel divisions.
    if playerA['group'] != playerB['group']:
        if winPercentage(playerA) != winPercentage(playerB):
            return 1 if winPercentage(playerA) > winPercentage(playerB) else -1
    else:
        # Same group, so use the standard fields for the season.
        rankA, rankB = group_rank(playerA), group_rank(playerB)
        if rankA != rankB:
            return 1 if rankA > rankB else -1
    # As a final tiebreaker then we use season completion streak and forum id.
    if completed_seasons[playerA['id']] != completed_seasons[playerB['id']]:
        return 1 if completed_seasons[playerA['id']] > completed_seasons[playerB['id']] else -1
    return playerB['id'] - playerA['id']

def division_sort_function(order, playoff_results):
    """Function to compare all players for the continuity ranking."""
    return lambda playerA, playerB: division_player_rank(order, playoff_results, playerA, playerB)

# Load previous season's standings from file.
standings_from_last_season = []
eliminations = []
with open('docs/data/standings/s{:02d}.json'.format(SEASON - 1)) as standings_file:
    data = json.load(standings_file)
    order = data['order']
    for division in ['Masters', 'Minions', 'Recruits']:
        if division in data['groups']:
            # The top players might be ranked according to a playoff.
            playoff_results = defaultdict(str)
            if 'playoffs' in data and '{} Playoffs'.format(division) in data['playoffs']:
                for game in data['playoffs']['{} Playoffs'.format(division)]:
                    for player_id, score in game.items():
                        winner = (score == max(game.values()))
                        playoff_results[int(player_id)] += '1' if winner else '0'
            all_groups = []
            for label, group in data['groups'][division].items():
                for player in group:
                    player['group'] = label
                    player['name'] = player_names[str(player['id'])]
                all_groups += group
            ordered = sorted(all_groups, key=cmp_to_key(division_sort_function(order, playoff_results)), reverse=True)
            division_ranking = ([player['id'] for player in ordered])
            standings_from_last_season.append(division_ranking)
            eliminations += [player['id'] for player in all_groups if ('seasonForfeit' in player and player['seasonForfeit'])]

def open_rating_file(registration_close_date):
    """Find the rating date immediately after the registration date."""
    now = date.today()
    if registration_close_date > now:
        registration_close_date = now
    rating_date = registration_close_date + timedelta(days=(11-registration_close_date.weekday())%7)
    timestamp = timegm(rating_date.timetuple())
    while int(timestamp) > 0:
        try:
            return open('docs/data/weeks/w{}.json'.format(int(timestamp)))
        except FileNotFoundError:
            print('WARNING: Rating file not found docs/data/weeks/w{}.json'.format(int(timestamp)))
            # If the file doesn't exist yet then try a week earlier.
            rating_date = rating_date - timedelta(days=7)
            timestamp = timegm(rating_date.timetuple())
            continue

def pick_division_sizes(player_count):
    """Find a suitable size for each division."""
    best_count = 0
    smallest_distance = TARGET_DIVISION_SIZE
    for count in set((floor(player_count / TARGET_DIVISION_SIZE), ceil(player_count / TARGET_DIVISION_SIZE))):
        if count == 0:
            continue
        distance = abs(TARGET_DIVISION_SIZE - player_count / count)
        if distance < smallest_distance:
            smallest_distance = distance
            best_count = count
    division_sizes = []
    for division_index in range(best_count):
        division_sizes.append(ceil((player_count - division_index) / best_count))
    return division_sizes

def continuity_sort(registrations, standings, eliminations):
    """Sort all returning players according to their previous performances."""
    divisions = deepcopy(standings)
    output_list = []
    lower_division = divisions.pop(0)
    is_top_division = True
    is_bottom_division = False
    while len(divisions) > 0:
        higher_division = lower_division
        lower_division = divisions.pop(0)
        if len(divisions) == 0:
            is_bottom_division = True
        while len(higher_division) > 0:
            output_list.append(higher_division.pop(0))
            if len(higher_division) > 0:
                if is_top_division:
                    output_list.append(higher_division.pop(0))
                if len(lower_division) > 0:
                    output_list.append(lower_division.pop(0))
                    if is_bottom_division and not is_top_division and len(lower_division) > 0:
                        output_list.append(lower_division.pop(0))
        is_top_division = False
    output_list += lower_division
    print('### Previous Season ###')
    for player_id in output_list:
        print(player_names[str(player_id)])
    return [player_id for player_id in output_list if player_id in registrations and player_id not in eliminations]

def ladder_sort(registrations, ladder_ratings):
    """Sort all players according to their ladder rating."""
    matching_players = [player for player in ladder_ratings if player['i'] in registrations]
    output_list = []
    for player in sorted(matching_players, key=lambda player: player['r'], reverse=True):
        output_list.append(player['i'])
    for player_id in sorted(set(registrations).difference(output_list)):
        output_list.append(player_id)
    return output_list

def create_divisions(continuity_order, ladder_order):
    """Draw up the divisions using the two sorted lists."""
    combined_list = []
    for i in range(len(continuity_order)):
        if continuity_order[i] not in combined_list:
            combined_list.append(continuity_order[i])
        if ladder_order[i] not in combined_list:
            combined_list.append(ladder_order[i])
    for i in range(len(continuity_order), len(ladder_order)):
        if ladder_order[i] not in combined_list:
            combined_list.append(ladder_order[i])
    division_sizes = pick_division_sizes(len(combined_list))
    return [combined_list[sum(division_sizes[:division_index]):sum(division_sizes[:division_index+1])] for division_index in range(len(division_sizes))]


with open_rating_file(REGISTRATION_CLOSE_DATE) as ratings_file:
    ladder_ratings = json.load(ratings_file)

continuity_order = continuity_sort(REGISTRATIONS, standings_from_last_season, eliminations)
print('### Continuity ranking ###')
for i, player_id in enumerate(continuity_order):
    print('{} ({})'.format(player_names[str(player_id)], i+1))

print('### Ladder ranking ###')
ladder_order = ladder_sort(REGISTRATIONS, ladder_ratings)
for player_id in ladder_order:
    print('{} ({})'.format(player_names[str(player_id)], [player['r'] for player in ladder_ratings if player['i'] == player_id][0]))

print('### Divisions ###')
divisions = create_divisions(continuity_order, ladder_order)
for division_index, division in enumerate(divisions):
    print('--- {} ({}) ---'.format(DIVISION_NAMES[division_index], len(division)))
    for player_id in division:
        print(player_names[str(player_id)])
        #print('{} ({})'.format(player_names[str(player_id)], player_id))
        #print('        - [{}, {}]'.format(player_id, player_names[str(player_id)]))
