#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# A script to help generating the forum post for the rulebook.

with open('rules.md') as rules:
    in_list = False
    for line in rules.read().split('\n'):
        if line.startswith('* '):
            if not in_list:
                in_list = True
                print('[list]')
            line = '[*] ' + line[2:]
        elif in_list:
            print('[/list]')
            in_list = False
        if line.startswith('# The Rulebook') or line.startswith('# Schedule Summary'):
            line = '[b][size=200]{}[/size][/b]'.format(line[2:])               
        elif line.startswith('# '):
            line = '[b][size=150]{}[/size][/b]'.format(line[2:])
        elif line.startswith('## '):
            line = '[b]{}[/b]'.format(line[3:])
        elif line.startswith('### '):
            line = '[b]{}[/b]'.format(line[4:])
        if line == '- [The Rulebook](#the-rulebook)':
            continue
        elif line.startswith('- ['):
            line = re.sub(r'^[^\[]*\[([^\]]*).*$', '[b]\\1[/b]', line)
        elif line.strip().startswith('- ['):
            line = re.sub(r'^[^\[]*\[([^\]]*).*$', '\\1', line)
        print(line)
    if in_list:
        print('[/list]')
    print('''[size=200]Changes to the rulebook since last season[/size]

Key:
[color=#0000FF]Text added[/color]
[color=#FF0000]Text removed[/color]''')
 