# The Rulebook

Red Alert Global League (RAGL), Season 17 is played starting 2025-10-06. We will aim to be finished in 10 weeks by 2025-12-14. This timespan includes up to 7 weeks for the group stage and 3 weeks reserved for unforeseen delays, tiebreakers and playoffs.
Timespan of the season is subject to change depending on actual player rosters and will be finalized after player registrations are closed.

Current prize pool total: TBA
For details on prize pool contributions, check out the [Prize Pool section](#5.2-Prize-pool-contributions).

- [The Rulebook](#the-rulebook)
- [1. Format](#1-format)
  - [1.1 League structure](#11-league-structure)
  - [1.2 Group stage](#12-group-stage)
  - [1.3 Placements, promotions, relegations](#13-placements-promotions-relegations)
  - [1.4 Playoffs](#14-playoffs)
  - [1.5 Prizes](#15-prizes)
- [2. Registrations](#2-registrations)
  - [2.1 New signups](#21-new-signups)
  - [2.2 Returning players](#22-returning-players)
  - [2.3 Qualifications](#23-qualifications)
  - [2.4 Waiting list](#24-waiting-list)
- [3. Communications](#3-communications)
  - [3.1 Match scheduling](#31-match-scheduling)
  - [3.2 Match reporting](#32-match-reporting)
  - [3.3 Strikes](#33-strikes)
  - [3.4 Season Forfeit](#34-season-forfeit)
  - [3.5 Disputes](#35-disputes)
  - [3.6 Match delays](#36-match-delays)
- [4. Match regulations](#4-match-regulations)
  - [4.1 Game setup](#41-game-setup)
  - [4.2 Map pool](#42-map-pool)
    - [4.2.4 Map contest](#424-map-contest)
  - [4.3 Game disconnects](#43-game-disconnects)
- [5. Miscellaneous](#5-miscellaneous)
  - [5.1 Streaming/casting](#51-streamingcasting)
  - [5.2 Prize pool contributions](#52-prize-pool-contributions)
  - [5.3 Officials](#53-officials)
- [Schedule Summary](#schedule-summary)


# 1. Format

## 1.1 League structure

1.1.1 The League is split into Masters (1st tier) and Minions (2nd tier) divisions.

1.1.1.1 Recruits division (3rd tier) might be considered in case there are enough signups for its creation.

1.1.4 Players are assigned to divisions according to the [division assignment algorithm](divisionAssigner.py).

1.1.6 Players who feel like they've found themselves in a division above their skill level may request to be dropped to a lower division to better accommodate them. These requests will be considered by the administrators.

1.1.7 If there are only fifteen or fewer players who are qualified to play then the season will be delayed until later point.

## 1.2 Group stage

1.2.1 The group stage is held in a round robin format, where each player is to play a match against every opponent in his group.

1.2.2 A single match consists of 2 games. Game wins are added to the score table as points.

## 1.3 Placements, promotions, relegations

1.3.1 Players are ranked within their group based on game wins counted as points.

1.3.2 In the event of tied points at the end of the season, the players will be ranked against each other based on:
* Result of the players' current season matchup
* Total number of strikes accumulated by players (less strikes is better)
* Best-of-3 rematch (if necessary to determine playoff spots)

1.3.3 In the event of a tie for first place in any group except Masters at the end of the season, the tied players will be ranked against each other based on a Best-of-5 round robin (for two players this will be a single Bo5). The ranking will be decided based on:
* Match points (i.e. The player who wins the most Bo5s)
* Game points
* Game point difference (i.e. wins minus losses)
* Group stage matchup
* Total strikes (less strikes is better)
* RAGL Ladder rating from the Friday before the Bo5s started

1.3.4 Strikes can be given for a number of different reasons, including failure to report a match, cheating, etc. Strikes are listed in the forum.

1.3.5 Three strikes accumulated during the season result in a straight disqualification from the group stage. Disqualified players are cleared of any group stage results in that season and are placed last in their group.

1.3.6 Players finishing in the top 4 spots of Masters are promoted into Masters Playoffs which decide final standings in Masters.

1.3.8 Any required rematches are to be resolved in the week following the end of the group stage. In case of failure of one of the players to schedule and play the rematch in the specified timeframe that player is automatically assigned a technical loss. In case of failure of both of the players to schedule and play the rematch in the specified timeframe both players are excluded from any following stages of the season.

1.3.9 Due to the nature of the League, actual promotions/relegations between divisions can't be defined up until the start of the next season.

## 1.4 Playoffs

1.4.1 Players finishing in the top 4 spots of Masters are promoted into Masters Playoffs. Playoffs consist of two Semi-final matches, Bronze Match and Final. All matches are Best-of-7.

1.4.2 Players finishing 1st and 4th play in the first Semi-final. Players finishing 2nd and 3rd play in the second Semi-final. Semi-final losers play in Bronze Match for the 3rd and 4th place overall. Semi-final winners play in the Final for the Masters Champion title and 2nd place overall.

1.4.3 If any player has finished all their group stage matches and is in a Playoff spot, but then drops before the Semi-final maps are announced then a different player will included in the Playoffs. For example if the 3rd place finisher drops then the Semi-finals will be 1st against 5th and 2nd against 4th.

1.4.4 Once the Semi-final maps are announced then any Playoff player dropping will not be replaced. It is possible that a prize will be unallocated and rolled over to the next season.

1.4.5 Semi-final matches are to be resolved in the 2 weeks following the end of the group stage. In case of failure of one of the players to schedule and play the match in the specified timeframe that player is automatically assigned a technical loss. In case of failure of both of the players to schedule and play the match in the specified timeframe both players are excluded from top three prize allocations and any following stages of the season.

1.4.6 Final and 3rd place matches are to be resolved in the 3 weeks following the end of the group stage. In case of failure of one of the players to schedule and play the match in the specified timeframe that player is automatically assigned a technical loss. In case of failure of both of the players to schedule and play the match in the specified timeframe both players are excluded from top three prize allocations and their prizes will be rolled over to the next season.

## 1.5 Prizes

1.5.1 By estimate, the prize pool is split as follows (final shares might differ due to the prize pool size, transfer fees and values rounding):
* 38% Masters Champion
* 19% Masters 2nd
* 16% Masters 3rd
* 12% Season Finisher prizes
* 15% Mapmaker who wins the preliminary community voted map competition.

1.5.1.1 Prize payments are subject to transfer fees and consequently it is not worth paying very small prizes. If a prize is less than €5 then it will be omitted. Prizes will be allocated in the order Masters Champion, Mapmaker prize, Masters 2nd, Season Finisher, Masters 3rd. So for example a €20 prize pool will be split in the ratio 38:15 between Masters Champion and the winning mapmaker, giving ~€15 and ~€5 respectively. When trying to split the €20 prize pool three ways (i.e. including a prize for 2nd place) then the minimum prize would drop to ~€4 which is not allowed.

1.5.2 If there are at least four prizes then players who successfully finished the Group Stage and did not win any other prize will be entered into the Season finisher prize draw. Note that if players drop from the Playoffs then they are not eligible for the top three prizes, but could still win a Season finisher prize.

1.5.2.1 The season finisher prize pool will be split into some number of season finisher prizes and those players with more unused strikes will have a higher chance of winning a prize. (Nb. Due to the implementation of the prize draw the chance of winning may not be proportional to the number of strikes a player has left)

1.5.3 Prize pools are completely voluntary and are not expected to be significant each season.

1.5.4 Players may be ineligable for prizes if they are based in countries on economic sanctions lists (for example PayPal is currently not operating in Russia). We reserve the right to reassign or roll over prizes to the next season if this is the case.

# 2. Registrations

## 2.1 New signups

2.1.1 New players have until 2025-10-02 to send the registration info.

2.1.2 Registration takes place through Discord (#ragl-signups in https://discord.gg/99zBDuS), the primary channel of communication for RAGL, or in the registrations forum thread.

2.1.3 Registration info must include the following:
* Nickname that will be used throughout the season;
* Country of origin and time zone expressed in UTC (see http://www.timeanddate.com);
* OpenRA discord name (Discord is the primary channel for communication);
* Forum name (used to find player id).

2.1.4 Registered players are put onto Signup list. If a player has sent their registration info but hasn't been put onto the Signup list then they should contact the officials no later than the final registration date.

## 2.2 Returning players

2.2.1 Players transferring over from the previous season have until 2025-10-02 to confirm their participation.

2.2.2 Returning players don't have to provide any other information than the expressed confirmation, officials will request any of the above if mandatory information is missing.

## 2.3 Qualifications

2.3.5 Players who have been forfeit or disqualified in more seasons than they have completed will need to play some pre-season games on the ladder to be eligible to return. Players must have played `4*(incomplete - complete)²` games on the ladder between the targetted end of playoffs for the previous season (see rules page for previous season) and registration closing for this season.

For example: If a player has season forfeit in 3 seasons and only completed 1 season then they must play `4*(3-1)² = 4*2² = 16` preseason ladder games to be eligible for the season.

See https://tttppp.github.io/ragl/forfeits.html for individual records.

2.3.6 Forfeits during the playoffs of this season will count as a completed season for future qualification (although similar forfeits in some past seasons were subject to different rules and so continue to count as forfeits).

## 2.4 Waiting list

2.4.1 In the event of players leaving during the first week for any reason, they may be replaced from the waiting list. The league officials will use a combination of the waiting list and promotion to fill the vacancy.

# 3. Communications

Official communications between the players and with league officials are primarily done through Discord.

## 3.1 Match scheduling

3.1.1 All participating players are themselves responsible for their weekly matches. Special private per-division Discord channels are recognized as the official means of players communication. However, at the discretion of the players, any venue of contact can be used as long as you recognize that league officials will be of limited help should things go awry. League officials cannot guarantee or take responsibility for information processed outside of official channels.

3.1.2 Players are advised to contact their opponents early (i.e. via private messaging) and establish communication as well as schedule matches, as time zones and personal activities play a major part in match scheduling.

## 3.2 Match reporting

3.2.1 Match reporting is done automatically by ragl.org and playing on the official RAGL servers. Games played on any other server than the RAGL official server will probably need to be replayed at the discretion of the league officials. After you have completed a match, the result should appear on your player profile at ragl.org.

3.2.8 Failure to play a match before its weekly deadline can result in strikes for both players. These matches still need to be played (same timeframe as delayed matches).

## 3.3 Strikes

3.3.1 If a player is unresponsive on the official Discord channel for their division then the league officials will attempt to notify them that they are at risk of receiving a strike.

3.3.2 Players caught dodging, being unresponsive or scheduling matches at inappropriate times for their benefit will be punished. Punishments include but are not limited to: warnings, strikes, defaulted matches, season forfeits, and permanent banning from RAGL.

3.3.6 Any strikes awarded will be published on Discord.

## 3.4 Season Forfeit

3.4.1 Players can give a season forfeit notice if there is any reason that prevents finishing the season in a normal manner. They should notify officials, preferably in the dedicated Discord channel.

3.4.2 If a player forfeits and has unplayed group stage matches then they will be cleared of any results (except strikes) for the season and placed last in their respective group.

3.4.4 If a player has finished the group stage and forfeits during the playoffs then they will be placed last out of those competing in the playoffs (i.e. 4th for the Masters Playoffs). In the unlikely event that more than one player forfeits in this way then they will be ranked against each other based on their playoff seeding.

## 3.5 Disputes

3.5.1 Players are to contact officials explicitly in the event of a supposedly erroneous information in Scoreboards, incorrect handling of the situation or any other issues that concern the league, preferably in the dedicated Discord channel.

3.5.2 The league officials reserve the right to make the final call in disputed situations with the health of the league in mind.

3.5.3 CHEATING: any forms of cheating will be marked with various penalties decided by admins. Cheating can be anything deemed to give an unfair advantage to one player. This could be (but not limited to) disconnecting on purpose, pausing and using actions, macros, GPS hacks etc. Penalties can range from a replay of the game to a ban from the league. DO NOT CHEAT.

## 3.6 Match delays

3.6.1 Matches are possible to be delayed by one player for up to one week, or by both players for up to two weeks, up until the end of the group stage.

3.6.2 Delay notices must be published in the dedicated Discord channel with a mention of the opponent.

3.6.3 Delay notices must be sent no later than the next week's Monday 23:59 UTC+0.

3.6.5 There are no regulations regarding matches being played before their designated schedule, thus it is advised to play matches early instead of delaying.

3.6.6 If only one player is actively trying to schedule a match then their opponent will be issued with a strike, rather than the active player having to use a delay.

3.6.7 Officials will make decisions about any overdue matches in the scheduled order and make a judgement as to which players to assign strikes to.

# 4. Match regulations

## 4.1 Game setup

4.1.1 Games are by default to be played on the latest game release at the moment of season start. In case a new release is shipped during an ongoing season, an explicit official notice is sent to all players regarding the versioning.

4.1.2 The first player listed in the match schedule is to pick the map for the first game. The map pick process should take the following order:

* Second player bans a map;
* First player picks a different map;
* First game is played;
* First player bans a map;
* Second player picks a map excluding the two banned maps and the map used for the first game;
* Second game is played.

Players are free to make exceptions from this rule at the discretion of both parties.

4.1.2.1 If a player wants to ban a map from his opponent's pick he should do that before the pick.

4.1.2.2 A player should be allowed to ban a map if he wishes to do so; so if a map is picked without asking to invoke the map ban, then a player is still allowed to ban a map afterwards.

4.1.3 First map pick is pre-set by officials for Tiebreaker and Playoffs matches, followed by loser's pick.

4.1.3.1 Maps may not be played twice during a Tiebreaker or Playoff match.

4.1.3.2 After the first game in a Tiebreaker or Playoff then the winner should ban a map, followed by the loser. These maps may not be picked by either player for the rest of the match.

4.1.4 The standard game settings in the game lobby should be set as follows:
* Explored Map: On
* Crates: Off
* Short Game : On
* Fog of War : On
* Build off Allies: (irrelevant)
* Limit Build Area: On
* Separate Team Spawns: Off (irrelevant for maps with 2 spawns)
* Reusable engineers: On
* Redeployable MCVs: On
* Kill Bounties: On
* Debug Menu : Off
* Starting Cash : $5000
* Tech Level : Unrestricted
* Starting Units : MCV Only
* Game Speed : Normal
* Player spots must be random.
* Handicap: 0%

4.1.5 The game is played until one of the players is named defeated (either by all buildings and MCVs being destroyed or by pressing "Surrender"). Leaving the game before this occurs is highly discouraged as it prevents proper recording of a game result in a replay. If a player disconnects rather than surrendering then the other player may also leave the game afterwards, but should not surrender.

4.1.5.1 Messages sent in the game chat should not be interpreted as the end of the game. In particular if a player sends a "gg" message then this is not the end of the game unless they are also defeated or they disconnect.

4.1.6 The use of external software macros (programmed keypress sequences of commands that are not possible to be executed by game engine means, i.e. ordering units automation) is an unsportsmanlike conduct and is forbidden. More obvious automation scripts resulting in APM spikes are detectable by replay parsing tools, other suspicious behaviours might be up for scrutiny by officials. Positive confirmation of using external tools to gain game advantage will impose a strict ruling, up to a possible ban from participation in RAGL for as long as admins see fit.

4.1.7 The use of modified clients that alter core gameplay in anyway are strictly forbidden. Positive confirmation of the use of a modified client to gain an unfair advantage will impose a strict ruling, up to a possible ban from participation in RAGL for as long as admins see fit.

4.1.8 Players found colluding in order to influence the result of their match and remove the uncertainty in the outcome will be subject to strict ruling, up to a possible ban from participation in RAGL for as long as admins see fit. This includes players who surrender prematurely or season forfeit in order to cancel their earlier results.

4.1.9 Rules from the OpenRA Competitive server also apply to in-game chat and player names - don't be a dick. Failure to comply with this rule will result in disqualification.

4.1.10 All players must be authenticated for their games. The RAGL servers will enforce this.

## 4.2 Map pool

4.2.1 Map pool consists of 12 maps specifically uploaded to the Resource Centre and marked as "Category: RAGL 17" and explicit naming and thumbnail watermarks. Usage of any other versions of these maps for the league games is disallowed and will be rejected from being reported as a valid match result.

4.2.2 All maps include custom balance changes.

4.2.3 Map pool can be found in the Competitive Discord server or downloaded from ragl.org.

### 4.2.4 Map contest

4.2.4: There will be a vote for the community's favourite map before RAGL, this map will be automatically included in the pool. Maps must be submitted by 2025-09-18.

4.2.4.1: Map submissions should be made in this thread or in the #map-making channel of the OpenRA Competitive Discord server,

4.2.4.2: Up to two maps per mapmaker

4.2.4.3: Maps do not have to be new, but may not have featured in previous seasons of RAGL

4.2.4.4: Voting will open once map submissions have closed.

4.2.4.5: Voting will close on 2025-09-25.

4.2.4.6: Voters assign 3pts, 2pts and 1pt to three different maps (it is not allowed to vote for fewer than three maps)

4.2.4.7: Votes are final at the point they are seen by TTTPPP and cannot be changed after this

4.2.4.8: Mapmakers can't vote for their own maps

4.2.4.9: Any mapmakers who vote will receive 3pts bonus on all maps they submitted

4.2.4.10: The map with the highest score will win. If two maps are tied on the same score then the tiebreaker will be number of people who gave it a score (including bonus points). If the maps are still tied after this then the map with the lowest resource centre id wins (as shown in the links below).

4.2.4.11: If there are fewer than five map authors then the map contest will not be run, but some of the maps may be included in the map pool.

## 4.3 Game disconnects

4.3.1 Players are to decide between themselves the outcome of a disconnected game. If it is decided to replay the game, the game that resulted in disconnect prior to this is deemed forfeit and cannot be used in a match result report.

4.3.2 If the players cannot come to an agreement with regards to a game that resulted in disconnect, a notice to the officials should be stated including the replay of the game in question, preferably in the dedicated Discord channel. The evaluation of such game will likely result in a re-play unless the game is undoubtedly decided towards one player. The final word will be up to the official evaluation regardless.

4.3.3 Players who get disconnected more than 3 times during a season will forfeit the game points of their following disconnected games regardless of the state of the ongoing game.

# 5. Miscellaneous

## 5.1 Streaming/casting

5.1.1 Streamers should add a minimum of 90 seconds delay to their streams when covering a league match, unless both players explicitly state their wish to disregard this rule.

5.1.2 Streamers who do not participate in the league but are officially recognised can be added to the Discord channels to stay informed about game scheduling.

## 5.2 Prize pool contributions

5.2.1 Donations to the pool should be sent in Euros or US Dollars via PayPal to mm_openra@protonmail.com (milkman). Name or a request to remain anonymous is to be stated in 'Write a note' section.

5.2.2 PayPal charges conversion fees for payouts in a different currency than the donation. Conversion fees for payouts will be drawn from the respective prize money rather than the entire pool.

## 5.3 Officials

5.3.1 The list of officials to contact is as follows:
* TTTPPP
* milkman
* .won (.1)
* Anjew

5.3.2 RAGL has its own discord, it can be found here https://discord.gg/99zBDuS Please post in the discord with any questions. Please, refrain from using discord personal messages unless the matter is urgent and cannot be discussed by other means.

5.3.3 League officials reserve the rights to alter or override the rulebook at any time, including during an ongoing season. All players will be immediately notified if any substantial changes are made during the season. Any change to the rulebook after player registrations are over is duplicated via a post in this thread.

For all inquiries you can contact us through Discord or reply on this thread.

# Schedule Summary

* 2025-09-18 Map submission deadline
* 2025-09-25 Community map vote deadline
* 2025-10-02 Player registrations close
* 2025-10-06 Start of week 1
* 2025-11-24 Start of Playoffs
* 2025-12-14 Target for end of Playoffs
