#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import seed, shuffle

SEASON = 12

divisions = [
('Masters', sorted(
'''goat (Denmark)
Kav (Finland)
happy (England)
ZxGanon (Germany)
Mr Cloudy (England)
Pinkthoth (Finland)
SinJul (Germany)
Blackened (USA)
Goremented (Germany)
KSK_Nico (Germany)
anjew (Australia)
Upps (Germany)
FiveAces (Austria)
Sigil (USA)'''.split('\n'), key=str.casefold)),

('Minions Alfa', sorted(
'''Eugenator (Austria)
Kaution (Belgium)
Moods (Canada)
Dodder (Ireland)
Mo (Wales)
TTTPPP (UK)
worldpeace (USA)
Nilhall (China)
MR C (UK)
[bye] ()'''.split('\n'), key=str.casefold)),

('Minions Bravo', sorted(
'''Unano (maceman) (England)
TiTo (Slovenia)
Gajcus (Poland)
Ekanim (USA)
DVoid (England)
Duke Bones (USA)
Nah (manta151) (Germany)
Tailix Killa Mentor (England)
Therapist (Canada)
potato (Czech Republic)'''.split('\n'), key=str.casefold))
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
