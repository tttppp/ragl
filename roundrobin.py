#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from datetime import date, timedelta
from math import ceil
from random import seed, shuffle

SEASON = 15
GROUP_STAGE_START_DATE = date(2023, 10, 9)
GROUP_STAGE_WEEKS = 7

divisions = [
('Masters', sorted(
'''Kav (13705)
Fazzar (17239)
Blackened (6430)
Upps (7304)
not happy (15469)
maceman (6793)
tux (15899)
ROCKhardFISTnips (8860)
anjew (3952)
Mr Cloudy (6771)
Mo (5292)
milkman (16066)'''.split('\n'), key=str.casefold)),

('Minions', sorted(
'''Duke Bones (11913)
Nilhall (7714)
bete (15428)
BigHALK (17607)
Nightingale (18968)
TTTPPP (7387)
chouchani (14769)
Tailix Killa Mentor (6751)
goldie (18359)
fiwo (18864)
OpiumPrime (13008)
jediandrew (19133)'''.split('\n'), key=str.casefold))
]

# Make the schedule for the season reproducible.
seed(SEASON)

match_rounds_by_division = {}
for division, players in divisions:
    match_rounds = []
    names = [player.split(' (')[0] for player in players]
    shuffle(names)
    # Use a second list of names to randomise who has first map pick in each match.
    name_ordering = list(names)
    if '[bye]' in name_ordering:
        name_ordering.remove('[bye]')
    shuffle(name_ordering)
    first = names[0]
    others = names[1:]
    matches = set()
    for i in range(len(others)):
        match_round = ''
        order = [first] + others[i:] + others[:i]
        for j in range(len(order) // 2):
            if '[bye]' in [order[j], order[-j-1]]:
                swap_order = order[j] == '[bye]'
            else:
                swap_order = (name_ordering.index(order[j]) - name_ordering.index(order[-j-1])) % len(name_ordering) + len(name_ordering) % len(name_ordering) <= len(name_ordering) // 2
            if swap_order:
                match_round += '{} vs {}\n'.format(order[-j-1], order[j])
            else:
                match_round += '{} vs {}\n'.format(order[j], order[-j-1])
            matches.add((order[j], order[-j-1]))
            matches.add((order[-j-1], order[j]))
        match_rounds.append(match_round)
    match_rounds_by_division[division] = match_rounds

latest_round_played = defaultdict(int)
for week in range(1, GROUP_STAGE_WEEKS + 1):
    start_date = (GROUP_STAGE_START_DATE + timedelta(weeks=week - 1)).strftime('%Y-%m-%d')
    end_date = (GROUP_STAGE_START_DATE + timedelta(days=7 * week - 1)).strftime('%Y-%m-%d')
    print('[size=200][b]Week {}: {} - {}[/b][/size]\n'.format(week, start_date, end_date))
    for division, _ in divisions:
        print('[size=150][b]{}[/b][/size]\n'.format(division))
        round_to_play_up_to = ceil((len(match_rounds_by_division[division]) * week) / GROUP_STAGE_WEEKS)
        for match_round in match_rounds_by_division[division][latest_round_played[division]:round_to_play_up_to]:
            print(match_round)
        latest_round_played[division] = round_to_play_up_to