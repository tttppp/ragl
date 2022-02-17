# RAGL

This repository contains several archived resources related to RAGL.

## RAGL Ladder

The RAGL Ladder is available here: https://tttppp.github.io/ragl/

It combined results from RAGL and the [OpenRA Ladder](http://oraladder.net/?period=all) and uses Glicko2 to create a
seeding for players. This is particularly useful for determining which division players should be put into if they have
not played in the previous season of RAGL.

### FAQ

*What algorithm is used for the ranking?*

The RAGL Ladder uses Glicko2 (r=1500, RD=350) and ranks players using `r - 3*RD` (i.e. three standard deviations below
their raw rating). The column headed "error" is the value `3*RD`.

*There's a mistake in the [results list](results)*

If you spot a mistake in the results list (e.g. because the RAGL dataset included a game that wasn't really part of
RAGL) then please let me know. I will correct the data unless it is very near to the start of a season.

*Why do we need a second Ladder?*

The aim of this ladder is to provide a seeding for players who did not take part in the previous season of RAGL. By
including all games from previous seasons of RAGL as well as the games on the OpenRA Ladder then we are able to get a
reasonable idea of whether a player from Season 8 of RAGL is better or worse than a new player who's been winning a lot
of games on the OpenRA Ladder.

## RAGL Rules

The rules for each season of RAGL are available in the git history of this repo. See the history of [rules.md](rules.md)
for more details.

## Contributions

Any contributions to this project are very welcome. If you're adding functionality to the ladder website then that's
likely to be very quickly approved. If you are proposing changes to the RAGL rules then it will need more discussion.
