4#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections
import datetime
import glicko2
import json
import math
import os
import requests

results_dir = 'results'
web_dir = 'docs'

ladder_url = 'http://oraladder.net/latest-js?period=all'

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

# Find the latest ladder game already stored.
results_filenames_by_year = collections.defaultdict(dict)
ladder_years = []
for results_filename in os.listdir(results_dir):
    competition, year_str = results_filename.split('.')[0].split('_')
    year = int(year_str)
    results_filenames_by_year[year][competition] = os.path.join(results_dir, results_filename)
    if competition == 'ladder':
        ladder_years.append(year)

for year in reversed(sorted(ladder_years)):
    results_filename = results_filenames_by_year[year]['ladder']
    with open(results_filename) as results_file:
        results = json.load(results_file)
    if len(results) > 0:
        break

last_stored_ladder_time = str_to_date(results[-1]['date'])

# Load the ladder results from the official ladder.
ladder_games = requests.get(ladder_url).json()
new_games_by_year = collections.defaultdict(list)
for ladder_game in sorted(ladder_games, key=lambda game: game['date']):
    # Ignore games involving deleted players.
    if ladder_game['p0'] == None or ladder_game['p1'] == None:
        continue
    # Store the results of new games.
    game_date = str_to_date(ladder_game['date'])
    if game_date > last_stored_ladder_time:
        # Restrict to just the minimum data we want.
        p0 = {'name': ladder_game['p0']['name'], 'id': get_player_id(ladder_game['p0'])}
        p1 = {'name': ladder_game['p1']['name'], 'id': get_player_id(ladder_game['p1'])}
        ladder_game = {'date': ladder_game['date'], 'map': ladder_game['map'], 'p0': p0, 'p1': p1}
        new_games_by_year[game_date.year].append(ladder_game)

# Store any new results.
for year in sorted(new_games_by_year.keys()):
    filename = make_results_filename(year, 'ladder')
    if year in results_filenames_by_year.keys() and 'ladder' in results_filenames_by_year[year].keys():
        with open(filename) as results_file:
            results = json.load(results_file)
        results += new_games_by_year[year]
    else:
        results = new_games_by_year[year]
        results_filenames_by_year[year]['ladder'] = filename
    print('Adding {} games to {}'.format(len(new_games_by_year[year]), year))
    with open(filename, 'w') as results_file:
        json.dump(results, results_file, indent=4, sort_keys=True)

start_datetime = str_to_date('2016-01-04 00:00:00')
now = datetime.date.today()
# End date is the beginning of this week, so we're only including complete weeks.
end_date = now + datetime.timedelta(days=7-now.weekday())
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
    player_data = {}
    while batch_end < end_datetime.timestamp():
        batch_start = batch_end
        batch_end += BATCH_DURATION
        opponent_ratings = collections.defaultdict(list)
        opponent_rds = collections.defaultdict(list)
        results = collections.defaultdict(list)
        for game in reversed(games):
            if timestamp(game) >= batch_start and timestamp(game) < batch_end:
                winner = game['p0']['id']
                loser = game['p1']['id']
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
                        player_data[player['id']] = player['name']
        for player_id in ratings.keys():
            if len(results[player_id]) > 0:
                ratings[player_id].update_player(opponent_ratings[player_id], opponent_rds[player_id], results[player_id])
            else:
                ratings[player_id].did_not_compete()
            if ratings[player_id].rd > MAX_RD:
                ratings[player_id].rd = MAX_RD
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
for year in sorted(results_filenames_by_year.keys()):
    for competition, filename in results_filenames_by_year[year].items():
        with open(filename) as results_file:
            results += json.load(results_file)

data, player_data = glicko2_table(ratings, results)

# Create the data files.
with open(os.path.join('docs', 'data', 'timestamps.json'), 'w') as timestamp_file:
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
    with open(os.path.join('docs', 'data', 'weeks', 'w{}.json'.format(week_timestamp)), 'w') as week_file:
        json.dump(week_table, week_file, indent=4, sort_keys=True)
with open(os.path.join('docs', 'data', 'players.json'), 'w') as players_file:
    json.dump(player_data, players_file, indent=4, sort_keys=True)
for player_id, entries in player_rating_data.items():
    with open(os.path.join('docs', 'data', 'players', 'p{}.json'.format(player_id)), 'w') as player_rating_file:
        json.dump(entries, player_rating_file, indent=4, sort_keys=True)
