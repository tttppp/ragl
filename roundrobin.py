#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from datetime import date, timedelta
from math import ceil
from random import seed, shuffle

SEASON = 18
GROUP_STAGE_START_DATE = date(2026, 10, 26)
GROUP_STAGE_WEEKS = 7

divisions = [
('Masters', sorted(
'''Gargamel (16814)
sir123 (19305)
tux (15899)
Upps (7304)
maceman (6793)
dark (24123)
Duke Bones (11913)
Ekanim (13710)
Blackened (6430)
Sigil (8869)
Amelza (20510)
ZxGanon (6766)
Mo (5292)
Orb (6748)'''.split('\n'), key=str.casefold)),

('Minions', sorted(
'''bete (15428)
i am bad at this (14724)
milkman (16066)
Svedski (16314)
anjew (3952)
TTTPPP (7387)
Therapist (12654)
akpella (11861)
ORA_CN-Hans (7714)
Stromberg_CN (22545)
Tailix Killa Mentor (6751)
muleyyyy (16788)'''.split('\n'), key=str.casefold)),

('Recruits', sorted(
'''fiwo (18864)
spetsnaz84 (6881)
Wolffang (22897)
808MANN (18417)
Implies (16474)
goldie (18359)
Gadderach (21158)
meowcat (21011)
1997cui (14328)
ERWARLORD (9372)
bongcloud (25635)
Gacid (25670)'''.split('\n'), key=str.casefold)),
]

# Make the schedule for the season reproducible.
seed(SEASON)

match_rounds_by_division = {}
for division, players in divisions:
    if len(players) % 2 == 1:
        players.append('[bye]')
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
