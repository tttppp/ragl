#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import seed, shuffle

SEASON = 12

divisions = [
('Masters', sorted(
'''Upps (1463)
Mr Cloudy (1559)
Blackened (1446)
anjew (1365)
Goremented (1375)
Sigil (1179)
Kaution (1322)
Gajcus (1414)
Eugenator (1349)
despro (1313)
maceman (1302)
[bye]'''.split('\n'), key=str.casefold)),

('Minions', sorted(
'''FiveAces (1241)
Mo (1125)
Ekanim (1158)
Jur (1147)
Tux (1130)
DukeBones (1114)
worldpeace (1012)
Dodder (1123)
Margot Honecker (1064)
Azure Anemone (986)
Nilhall (843)
[bye]'''.split('\n'), key=str.casefold)),

('Recruits', sorted(
'''TTTPPP (917)
milkman (890)
BeTe (814)
spetsnaz84 (787)
Pvt_Leaf (674)
Mees (662)
chouchani (163)
RobLoweEscobar (0)
jawsh (0)
daswaseinbefel (0)'''.split('\n'), key=str.casefold))
]

# Make the schedule for the season reproducible.
seed(SEASON)

for division, players in divisions:
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
        print('[size=150][b]{}[/b][/size]'.format(division))
        order = [first] + others[i:] + others[:i]
        for j in range(len(order) // 2):
            if '[bye]' in [order[j], order[-j-1]]:
                swap_order = order[j] == '[bye]'
            else:
                swap_order = (name_ordering.index(order[j]) - name_ordering.index(order[-j-1])) % len(name_ordering) + len(name_ordering) % len(name_ordering) <= len(name_ordering) // 2
            if swap_order:
                print('{} vs {}'.format(order[-j-1], order[j]))
            else:
                print('{} vs {}'.format(order[j], order[-j-1]))
            matches.add((order[j], order[-j-1]))
            matches.add((order[-j-1], order[j]))
        print()
