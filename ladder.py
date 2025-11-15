#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections
import datetime
import glicko2
import json
import math
import os
import requests

results_dir = 'results'
data_dir = os.path.join('docs', 'data')
skip_update = True

ragl_name = 'ragl'
results_urls = {
    'kk': None,
    'ladder': 'http://oraladder.net/latest-js?mod=ra',
    ragl_name: 'https://ragl.org/games/json'
}

def str_to_date(date_string):
    return datetime.datetime.fromisoformat(date_string)

def timestamp(game):
    return datetime.datetime.timestamp(datetime.datetime.fromisoformat(game['date']))

def to_datetime(timestamp):
    return datetime.datetime.isoformat(datetime.datetime.fromtimestamp(int(timestamp)))

def make_results_filename(year, competition):
    results_filename = '{}_{}.json'.format(competition, year)
    return os.path.join(results_dir, results_filename)

def get_player_id(player_object):
    """Get the player id from the url (which has a format like /player/6010?period=all)"""
    return int(player_object['url'].split('/')[2].split('?')[0])

def create_player_dict(game_object, player_reference):
    if type(game_object[player_reference]) == str:
        return {'name': game_object[player_reference], 'id': game_object[player_reference + '_id']}
    return {'name': game_object[player_reference]['name'], 'id': get_player_id(game_object[player_reference])}

for competition, competition_url in results_urls.items():
    # Find the latest game already stored.
    results_filenames_by_year = collections.defaultdict(dict)
    competition_years = []
    for results_filename in os.listdir(results_dir):
        file_competition, year_str = results_filename.split('.')[0].split('_')
        year = int(year_str)
        results_filenames_by_year[year][file_competition] = os.path.join(results_dir, results_filename)
        if file_competition == competition:
            competition_years.append(year)

    for year in reversed(sorted(competition_years)):
        results_filename = results_filenames_by_year[year][competition]
        with open(results_filename) as results_file:
            results = json.load(results_file)
        if len(results) > 0:
            break

    last_stored_competition_time = str_to_date(results[-1]['date'])

    # Load the results from the url.
    if competition_url != None and not skip_update:
        competition_games = requests.get(competition_url).json()
        new_games_by_year = collections.defaultdict(list)
        for competition_game in sorted(competition_games, key=lambda game: game['date']):
            # Ignore games involving deleted players.
            if competition_game['p0'] == None or competition_game['p1'] == None:
                continue
            # Store the results of new games.
            game_date = str_to_date(competition_game['date'])
            if game_date > last_stored_competition_time:
                # Restrict to just the minimum data we want.
                p0 = create_player_dict(competition_game, 'p0')
                p1 = create_player_dict(competition_game, 'p1')
                competition_game = {'date': competition_game['date'], 'map': competition_game['map'], 'p0': p0, 'p1': p1}
                new_games_by_year[game_date.year].append(competition_game)

        # Store any new results.
        for year in sorted(new_games_by_year.keys()):
            filename = make_results_filename(year, competition)
            if year in results_filenames_by_year.keys() and competition in results_filenames_by_year[year].keys():
                with open(filename) as results_file:
                    results = json.load(results_file)
                results += new_games_by_year[year]
            else:
                results = new_games_by_year[year]
                results_filenames_by_year[year][competition] = filename
            print('Adding {} games to {}'.format(len(new_games_by_year[year]), filename))
            with open(filename, 'w') as results_file:
                json.dump(results, results_file, indent=4, sort_keys=True)

def load_existing_player_data():
    with open(os.path.join(data_dir, 'players.json')) as players_file:
        player_data = json.load(players_file)
        return {int(player_id): name for player_id, name in player_data.items()}

with open(os.path.join(data_dir, 'replacements.json')) as replacements_file:
    player_id_replacements = json.load(replacements_file)

def get_canonical_player_id(player):
    player_id = str(player['id'])
    while player_id in player_id_replacements:
        player_id = str(player_id_replacements[player_id])
    return int(player_id)

with open(os.path.join(data_dir, 'ragl.json')) as ragl_file:
    ragl_details = json.load(ragl_file)

start_datetime = str_to_date('2016-01-01 00:00:00')
now = datetime.date.today()
# End date is the beginning of this week, so we're only including complete weeks.
end_date = now + datetime.timedelta(days=(10 - now.weekday()) % 7 + 1)
end_datetime = datetime.datetime.combine(end_date, datetime.datetime.min.time())

# Calculate Glicko2 rankings.
BATCH_DURATION = 7*24*60*60
MAX_RD = 350
def glicko2_init():
    return glicko2.Player(vol=0.06, rating=1500, rd=MAX_RD)

def glicko2_table(ratings, games):
    batch_end = int(start_datetime.timestamp())
    played = collections.Counter()
    won = collections.Counter()
    data = collections.defaultdict(dict)
    player_data = load_existing_player_data()
    while batch_end < end_datetime.timestamp():
        batch_start = batch_end
        batch_end += BATCH_DURATION
        opponent_ratings = collections.defaultdict(list)
        opponent_rds = collections.defaultdict(list)
        results = collections.defaultdict(list)
        for game in reversed(games):
            if timestamp(game) >= batch_start and timestamp(game) < batch_end:
                winner = get_canonical_player_id(game['p0'])
                loser = get_canonical_player_id(game['p1'])
                opponent_ratings[winner].append(ratings[loser].rating)
                opponent_rds[winner].append(ratings[loser].rd)
                results[winner].append(1)
                opponent_ratings[loser].append(ratings[winner].rating)
                opponent_rds[loser].append(ratings[winner].rd)
                results[loser].append(0)
                played[winner] += 1
                played[loser] += 1
                won[winner] += 1
                for player in [game['p0'], game['p1']]:
                    if player['id'] not in player_data:
                        player_data[player['id']] = {'name': player['name']}
        for player_id in ratings.keys():
            if len(results[player_id]) > 0:
                ratings[player_id].update_player(opponent_ratings[player_id], opponent_rds[player_id], results[player_id])
            else:
                ratings[player_id].did_not_compete()
            if ratings[player_id].rd > MAX_RD:
                ratings[player_id].rd = MAX_RD
            else:
                data[batch_end][player_id] = {
                    'i': player_id,
                    'r': round(ratings[player_id].rating - 3 * ratings[player_id].rd),
                    'e': round(3 * ratings[player_id].rd),
                    'p': played[player_id],
                    'w': won[player_id]
                }
    return data, player_data

ratings = collections.defaultdict(glicko2_init)

results = []
per_player_ragl_games = collections.defaultdict(lambda: collections.defaultdict(lambda: {'p': 0, 'w': 0}))
head_to_head_ragl_scores = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(lambda: [0, 0])))
for year in sorted(results_filenames_by_year.keys()):
    for competition, filename in results_filenames_by_year[year].items():
        with open(filename) as results_file:
            competition_results = json.load(results_file)
            if competition == ragl_name:
                for season, seasonDates in ragl_details['seasonDates'].items():
                    seasonStart = seasonDates['start'].replace('T', ' ')
                    seasonEnd = seasonDates['end'].replace('T', ' ')
                    for result in competition_results:
                        if result['date'] >= seasonStart and result['date'] <= seasonEnd:
                            winner, loser = get_canonical_player_id(result['p0']), get_canonical_player_id(result['p1'])
                            for p in [winner, loser]:
                                per_player_ragl_games[p][season]['p'] += 1
                            per_player_ragl_games[winner][season]['w'] += 1
                            if sum(head_to_head_ragl_scores[season][winner][loser]) < 2:
                                head_to_head_ragl_scores[season][winner][loser][0] += 1
                                head_to_head_ragl_scores[season][loser][winner][1] += 1
            results += competition_results

# Currently this only copes with a single depth of head-to-head results.
def populate_head_to_head_results(division, forfeit_player_ids, head_to_head_season_scores):
    sort_vectors = {}
    for player_data in division:
        if player_data['id'] not in forfeit_player_ids:
            sort_vectors[player_data['id']] = (player_data['won'],)
    unsorted = []
    for sort_vector in set(sort_vectors.values()):
        if list(sort_vectors.values()).count(sort_vector) > 1:
            tied_players = [player_id for (player_id, vector) in sort_vectors.items() if vector == sort_vector]
            unsorted.append(tied_players)
    head_to_head_displays = collections.defaultdict(list)
    while len(unsorted) > 0:
        tied_players = unsorted.pop()
        # Need to add h2h results to the end of the vector for each player.
        new_sort_vectors_to_players = collections.defaultdict(list)
        for player_id in tied_players:
            opponent_ids = [opponent_id for opponent_id in tied_players if opponent_id != player_id]
            won = sum(result[0] for (opponent_id, result) in head_to_head_season_scores[player_id].items() if opponent_id in opponent_ids)
            lost = sum(result[1] for (opponent_id, result) in head_to_head_season_scores[player_id].items() if opponent_id in opponent_ids)
            head_to_head_displays[player_id].append(f'{won}-{lost}')
            new_sort_vector = sort_vectors[player_id] + (won,)
            new_sort_vectors_to_players[new_sort_vector].append(player_id)
            sort_vectors[player_id] = new_sort_vector
        if len(new_sort_vectors_to_players) > 1:
            for player_ids in new_sort_vectors_to_players.values():
                if len(player_ids) > 1:
                    unsorted.append(player_ids)
    for player_data in division:
        head_to_head_display = head_to_head_displays[player_data['id']]
        if len(head_to_head_display) > 0:
            player_data['headToHead'] = ', '.join(head_to_head_display)

def wins_from_scores_string(scores_string):
    return tuple(int(score.split('-')[0]) for score in scores_string.split(', '))

def player_data_to_sort_vector(player_data):
    if 'seasonForfeit' in player_data and player_data['seasonForfeit']:
        return (0, int(player_data['id']))
    head_to_head_wins = wins_from_scores_string(player_data['headToHead']) if 'headToHead' in player_data else (0,)
    strikes = player_data['strikes'] if 'strikes' in player_data else 0
    tie_break_wins = wins_from_scores_string(player_data['tieBreak']) if 'tieBreak' in player_data else (0,)
    return (1, player_data['won'], head_to_head_wins, -strikes, tie_break_wins, int(player_data['id']))

latest_season = ragl_details['latestSeason']
head_to_head_season_scores = head_to_head_ragl_scores[str(latest_season)]
with open(os.path.join(data_dir, 'standings', f's{latest_season:02d}.json')) as latest_season_file:
    data = json.load(latest_season_file)
    groups = data['groups']
for group_name, group in groups.items():
    for division_name, division in group.items():
        forfeit_player_ids = [player_data['id'] for player_data in division if 'seasonForfeit' in player_data and player_data['seasonForfeit']]
        for player_data in division:
            player_id = player_data['id']
            player_data.pop('headToHead', None)
            if player_id in forfeit_player_ids:
                player_data.pop('played', None)
                player_data.pop('won', None)
                player_data.pop('strikes', None)
                continue
            non_cancelled_scores = [score for (opponent_id, score) in head_to_head_season_scores[player_id].items() if opponent_id not in forfeit_player_ids]
            won = sum(score[0] for score in non_cancelled_scores)
            lost = sum(score[1] for score in non_cancelled_scores)
            player_data['played'] = won + lost
            player_data['won'] = won
        populate_head_to_head_results(division, forfeit_player_ids, head_to_head_season_scores)
        # Finally sort by the appropriate fields to ensure the ordinals are correct in the webpage.
        group[division_name] = sorted(division, key=player_data_to_sort_vector, reverse=True)
with open(os.path.join(data_dir, 'standings', f's{latest_season:02d}.json'), 'w') as latest_season_file:
    data = {'order': [{'won': 'DESC'}, {'headToHead': 'DESC'}, {'strikes': 'ASC'}, {'tieBreak': 'DESC'}]}
    data['groups'] = groups
    json.dump(data, latest_season_file, indent=2, sort_keys=False)

data, player_data = glicko2_table(ratings, results)

for player_id, player_ragl_games in per_player_ragl_games.items():
    player_data[player_id]['ragl'] = player_ragl_games

# Create the data files.
with open(os.path.join(data_dir, 'timestamps.json'), 'w') as timestamp_file:
    json.dump(sorted(data.keys()), timestamp_file, indent=4, sort_keys=True)
player_rating_data = collections.defaultdict(list)
for week_timestamp, week_data in sorted(data.items(), key=lambda item: -item[0]):
    week_table = []
    for player_id, player_week_data in sorted(week_data.items(), key=lambda item: -item[1]['r']):
        week_table.append(player_week_data)
        player_rating_data[player_id].append(dict(player_week_data))
        del(player_rating_data[player_id][-1]['i'])
        player_rating_data[player_id][-1]['d'] = week_timestamp
        frequency = len([row for row in week_data.values() if row['r'] == player_week_data['r']])
        rank = len([row for row in week_data.values() if row['r'] > player_week_data['r']]) + 1
        player_rating_data[player_id][-1]['o'] = rank
        # Rank percentile
        player_rating_data[player_id][-1]['c'] = math.ceil(100.0 * ((rank - 1) + 0.5 * frequency) / len(week_data))
    with open(os.path.join(data_dir, 'weeks', 'w{}.json'.format(week_timestamp)), 'w') as week_file:
        json.dump(week_table, week_file, indent=4, sort_keys=True)
with open(os.path.join(data_dir, 'players.json'), 'w') as players_file:
    json.dump(player_data, players_file, indent=4, sort_keys=True)
position_data = []
percentile_data = []
for player_id, entries in player_rating_data.items():
    with open(os.path.join(data_dir, 'players', 'p{}.json'.format(player_id)), 'w') as player_rating_file:
        json.dump(entries, player_rating_file, indent=4, sort_keys=True)
    position_duration = collections.Counter()
    percentile_duration = collections.Counter()
    # Skip the week in progress and the very first week.
    for entry in entries[1:-1]:
        position_duration[entry['o']] += 1
        percentile_duration[entry['c']] += 1
    position_duration = {position: count for position, count in position_duration.items() if position in sorted(position_duration.keys())[:3]}
    percentile_duration = {percentile: count for percentile, count in percentile_duration.items() if percentile in sorted(percentile_duration.keys())[:3]}
    if len(position_duration) > 0:
        position_data.append({'i': player_id, 'O': position_duration})
        percentile_data.append({'i': player_id, 'C': percentile_duration})
position_data.sort(key=lambda entry: [[pair[0], -pair[1]] for pair in sorted(entry['O'].items())])
percentile_data.sort(key=lambda entry: [[pair[0], -pair[1]] for pair in sorted(entry['C'].items())])
with open(os.path.join(data_dir, 'records_position.json'), 'w') as records_file:
    json.dump(position_data, records_file, indent=4, sort_keys=True)
with open(os.path.join(data_dir, 'records_percentile.json'), 'w') as records_file:
    json.dump(percentile_data, records_file, indent=4, sort_keys=True)
