# The Rulebook

Red Alert Global League (RAGL), Season 14 is played starting 2023-05-01. We will aim to be finished in 10 weeks by 2023-07-09. This timespan includes up to 7 weeks for the group stage and 3 weeks reserved for unforeseen delays, tiebreakers and playoffs.
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
  - [3.3 Failed contact notices](#33-failed-contact-notices)
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

1.1.2 Masters division is always a single group of players. There is a minimum of 8 players in Masters division. There is a maximum of 16 players in Masters division.

1.1.3 Each division except Masters may consist of one or more groups of players. There is a minimum of 8 players per group. There is a maximum of 16 players per group.

1.1.4 Players are assigned to divisions according to the [division assignment algorithm](divisionAssigner.py).

1.1.6 Players who feel like they've found themselves in a division above their skill level may request to be dropped to a lower division to better accommodate them. These requests will be considered by the administrators.

1.1.7 League officials reserve the rights to not honour the above rules in special cases.

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

1.3.4 Strikes can be given for a number of different reasons, including failure to report a match, cheating, etc. Each strike is marked in Scoreboards.

1.3.5 Three strikes accumulated during the season result in a straight Disqualification from the group stage. Disqualified players are cleared of any results in that season and are placed last in their respective group.

1.3.6 Players finishing in the top 4 spots of Masters are promoted into Masters Playoffs which decide final standings in Masters.

1.3.7 In case any division is split into several groups, players finishing in the 1st place in their respective groups take part in Playoffs to decide the division Champion.

1.3.8 Any required rematches are to be resolved in a week time following the end of the group stage. In case of failure of one of the players to schedule and play the rematch in the specified timeframe that player is automatically assigned a technical loss. In case of failure of both of the players to schedule and play the rematch in the specified timeframe both players are excluded from prize allocations and any following stages of the season.

1.3.9 Due to the nature of the League, actual promotions/relegations between divisions can't be defined up until the start of the next season.

## 1.4 Playoffs

1.4.1 Players finishing in the top 4 spots of Masters are promoted into Masters Playoffs. Playoffs consist of two Semi-final matches, Bronze Match and Final. All matches are Best-of-5.

1.4.2 Players finishing 1st and 4th play in the first Semi-final. Players finishing 2nd and 3rd play in the second Semi-final. Semi-final losers play in Bronze Match for the 3rd and 4th place overall. Semi-final winners play in the Final for the Masters Champion title and 2nd place overall.

1.4.3 In case any division is split into 2 groups, players finishing 1st in their groups play in a Final for the division Champion title. The match is a Best-of-5.

1.4.4 In case any division is split into 4 groups, players finishing 1st in their groups play in Semi-finals, drawn at random. The Semi-finals winners play in a Final for the division Champion title. All matches are Best-of-5.

1.4.5 Semi-final matches are to be resolved in 2 weeks time following the end of the group stage. In case of failure of one of the players to schedule and play the match in the specified timeframe that player is automatically assigned a technical loss. In case of failure of both of the players to schedule and play the match in the specified timeframe both players are excluded from prize allocations and any following stages of the season.

1.4.6 Final and 3rd place matches are to be resolved in 3 weeks time following the end of the group stage. In case of failure of one of the players to schedule and play the match in the specified timeframe that player is automatically assigned a technical loss. In case of failure of both of the players to schedule and play the match in the specified timeframe both players are excluded from prize allocations.

1.4.7 Admins reserve the right to replace players excluded under 1.4.5 and 1.4.6 with the aim of preserving the integrity of the league.

## 1.5 Prizes

1.5.1 By estimate, the prize pool is split as follows (final shares might differ due to the prize pool size, transfer fees and values rounding):
* 38% Masters Champion
* 19% Masters 2nd
* 16% Masters 3rd
* 12% Season finisher prizes
* 15% Mapmaker who wins the preliminary community voted map competition.

1.5.1.1 Prize payments are subject to transfer fees and consequently it is not worth paying very small prizes. A small prize pool may result in prizes being omitted.

1.5.2 Players who successfully finished the season and did not win any other prize will be entered into the Season finisher prize draw.

1.5.2.1 The season finisher prize pool will be split into some number of season finisher prizes and those players with more unused strikes will have a higher chance of winning a prize. (Nb. Due to the implementation of the prize draw the chance of winning may not be proportional to the number of strikes a player has left)

1.5.3 Prize pools are completely voluntary and are not expected to be significant each season. If the prize pool for a particular season is thin the exact spread and rewards will be carefully considered.

1.5.4 Players may be ineligable for prizes if they are based in countries on economic sanctions lists (for example PayPal is currently not operating in Russia). We reserve the right to reassign prizes if this is the case.

# 2. Registrations

## 2.1 New signups

2.1.1 New players have until 2023-04-27 to send the registration info.

2.1.2 Registration takes place through Discord (#ragl-signups in https://discord.gg/99zBDuS), the primary channel of communication for RAGL, or in the registrations forum thread.

2.1.3 Registration info must include the following:
* Nickname that will be used throughout the season;
* Country of origin and time zone expressed in UTC (see http://www.timeanddate.com);
* OpenRA discord name (Discord is the primary channel for communication);
* Forum name (used to find player id).

2.1.4 Registered players are put onto Signup list. If the player sent their registration info but wasn't put onto Signup list then they should subsequently contact the officials no later than the final date.

## 2.2 Returning players

2.2.1 Players transferring over from the previous season have until 2023-04-27 to confirm their participation.

2.2.2 Returning players don't have to provide any other information than the expressed confirmation, officials are to request any of the above if mandatory information is missing.

## 2.3 Qualifications

2.3.5 Players who have been forfeit or disqualified in more seasons than they have completed will need to play some pre-season games on the ladder to be eligible to return. Players must have played `4*(incomplete - complete)²` games on the ladder in the month prior to registration closing.

For example: If a player has season forfeit in 3 seasons and only completed 1 season then they must play `4*(3-1)² = 4*2² = 16` preseason ladder games to be eligible for the season.

See https://tttppp.github.io/ragl/forfeits.html for individual records.

## 2.4 Waiting list

2.4.1 In the event of players leaving during first week for any reasons, players may be added from the waiting list. The league officials will use a combination of the waiting list and promotion to fill the vacancy.

# 3. Communications
Official communications between the players and with league officials are primarily done through Discord.

## 3.1 Match scheduling

3.1.1 All participating players are themselves responsible for their weekly matches. Special private per-division Discord channels are recognized as the official means of players communication. However, at the discretion of the players, any venue of contact can be used as long as you recognize that league officials will be of limited help should things go awry. League officials cannot guarantee or take responsibility for information processed outside of official channels.

3.1.2 Players are advised to contact their opponents early (i.e. via private messaging) and establish communication as well as schedule matches, as time zones and personal activities play a major part in match scheduling.

## 3.2 Match reporting

3.2.1 Match reporting is done automatically by RAGL.org and playing on the official RAGL servers. Any attempts of playing games on any other server than the RAGL official server will void the replays and the games will not count. After you have completed your matches, it should appear on your player profile at ragl.org as completed.

3.2.8 Failure to play a match until its weekly deadline can result in strikes for both players. These matches still need to be played (same timeframe as delayed matches).

## 3.3 Failed contact notices

3.3.1 In case match opponent is not responding or otherwise ignores the proper match scheduling, the player should inform officials of a Failed contact. Reporting a Failed contact notice protects a player that has filed such notice from receiving a strike for an unreported match.

3.3.2 Players caught dodging, being unresponsive or scheduling matches at inappropriate times for their benefit will be punished. Punishments include but are not limited to: warnings, strikes, defaulted matches, season forfeits, and permanent banning from RAGL.

3.3.3 The player has to notify both officials and the opponent, preferably in the dedicated Discord channel. Any info regarding the contact failure should be present in the notice for officials to resolve the matter.

3.3.4 Failed contact notices must be sent ASAP, leaving a failed contact notice attempt until after the deadline for the match will mean it will not be addressed; matches will be noted as a strike.

3.3.5 Failure to respond entirely will result in a 0-2 loss and a strike.

3.3.6 Any strikes awarded will be published on Discord.

## 3.4 Season Forfeit

3.4.1 Player is to explicitly state a season forfeit notice due to any reason that prevents finishing the season in a normal manner. Player has to notify officials, preferably in the dedicated Discord channel.

3.4.2 Players that forfeited the season are cleared of any results (except strikes) for that season and are placed last in their respective group.

## 3.5 Disputes

3.5.1 Players are to contact officials explicitly in the event of a supposedly erroneous information in Scoreboards, incorrect handling of the situation or any other issues that concern the league, preferably in the dedicated Discord channel.

3.5.2 The league officials reserve the right to make the final call in disputed situations with the health of the league in mind.

3.5.3 CHEATING: any forms of cheating will be marked with various penalties decided by admins. Cheating can be anything deemed to give an unfair advantage to one player. This could be (but not limited to) Disconnecting on purpose, pausing and using actions, macros, GPS hacks etc. Penalties can range from a replay of the game to a ban from the league. DO NOT CHEAT.

## 3.6 Match delays

3.6.1 Matches are possible to be delayed by one player for up to one week, or by both players for up to two weeks.

3.6.2 Delay notices must be published in the dedicated Discord channel with a mention of the opponent.

3.6.3 Delay notices must be sent no later than the next week's Monday 23:59 UTC+0.

3.6.4 Players can have up to 3 delay requests active at the same time.

3.6.5 There are no regulations regarding matches being played before their designated schedule, thus it is advised to play matches early instead of delaying.

3.6.6 Failed contact notices will take precedence over delay notices. If only one player is actively trying to schedule a match then their opponent will be issued with a strike, rather than the active player having to use a delay.

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
* Reusable engineers: On (optional off if both players agree)
* Redeployable MCVs: On
* Kill Bounties: On (optional off if both players agree)
* Debug Menu : Off
* Starting Cash : $5000
* Tech Level : Unrestricted
* Starting Units : MCV Only
* Game Speed : Normal
* Player spots must be random.
* Handicap: 0%

4.1.5 The game is played until one of the players is named defeated (either by all buildings and MCVs being destroyed or by pressing "Surrender"). Leaving the game before this occurs is highly discouraged as it prevents proper recording of a game result in a replay. If a player disconnects rather than surrendering then the other player may also leave the game afterwards, but should not surrender.

4.1.6 The use of external software macros (programmed keypress sequences of commands that are not possible to be executed by game engine means, i.e. ordering units automation) is an unsportsmanlike conduct and is forbidden. More obvious automation scripts resulting in APM spikes are detectable by replay parsing tools, other suspicious behaviours might be up for scrutiny by officials. Positive confirmation of using external tools to gain game advantage will impose a strict ruling, up to a possible ban from participation in RAGL for as long as admins see fit.

4.1.7 The use of modified clients that alter core gameplay in anyway are strictly forbidden. Positive confirmation of the use of a modified client to gain an unfair advantage will impose a strict ruling, up to a possible ban from participation in RAGL for as long as admins see fit.

4.1.8 Players found colluding in order to influence the result of their match and remove the uncertainty in the outcome of a match will be subject to strict ruling, up to a possible ban from participation in RAGL for as long as admins see fit. This includes players who surrender prematurely.

4.1.9 Rules from the OpenRA Competitive server also apply to in-game chat and player names - don't be a dick. Failure to comply with this rule will result in disqualification.

4.1.10 All players must be authenticated for their games. The RAGL servers will enforce this.

## 4.2 Map pool

4.2.1 Map pool consists of 10-12 maps specifically uploaded to the Resource Centre and marked as "Category: RAGL 14" and explicit naming and thumbnail watermarks. Usage of any other versions of these maps for the league games is disallowed and will be rejected from being reported as a valid match result.

4.2.2 All maps include custom balance changes.

4.2.3 Map pool can be found in the Competitive Discord server.

### 4.2.4 Map contest

4.2.4: There will be a vote for the community's favourite map before RAGL, this map will be automatically included in the pool. Maps must be submitted by 2023-04-13.

4.2.4.1: Map submissions should be made in this thread or in the #map-making channel of the OpenRA Competitive Discord server,

4.2.4.2: Up to two maps per mapmaker

4.2.4.3: Maps do not have to be new, but may not have featured in previous seasons of RAGL

4.2.4.4: Voting will open once map submissions have closed.

4.2.4.5: Voting will close on 2023-04-20.

4.2.4.6: Voters assign 3pts, 2pts and 1pt to three different maps (it is not allowed to vote for fewer than three maps)

4.2.4.7: Votes are final at the point they are seen by TTTPPP and cannot be changed after this

4.2.4.8: Mapmakers can't vote for their own maps

4.2.4.9: Any mapmakers who vote will receive 3pts bonus on all maps they submitted

4.2.4.10: The map with the highest score will win. If two maps are tied on the same score then the tiebreaker will be number of people who gave it a score (including bonus points). If the maps are still tied after this then the map with the lowest resource centre id wins (as shown in the links below).

## 4.3 Game disconnects

4.3.1 Players are to decide between themselves the outcome of a disconnected game. If it is decided to re-play the game, the game that resulted in disconnect prior to this is deemed forfeit and cannot be used in a match result report.

4.3.2 If the players cannot come to an agreement with regards to a game that resulted in disconnect, a notice to the officials should be stated including the replay of the game in question, preferably in the dedicated Discord channel. The evaluation of such game will likely result in a re-play unless the game is undoubtedly decided towards one player. The final word will be up to the official evaluation regardless.

4.3.3 Players who get disconnected more than 3 times during a season will forfeit the game points of their following disconnected games regardless of the state of the ongoing game.

# 5. Miscellaneous

## 5.1 Streaming/casting

5.1.1 Streamers should add a minimum of 90 seconds delay to their streams when covering a league match, unless both players explicitly state their wish to disregard this rule.

5.1.2 Streamers who do not participate in the league but are officially recognised can be added to the Discord channels to stay informed about game scheduling.

## 5.2 Prize pool contributions

5.2.1 Personal email account, OpenRA.RAGL@gmail.com, is connected via PayPal to host the prize pool contributions (https://www.paypal.me/openraragl). Any person willing to contribute is to send a payment through PayPal to this email address. Name or a request to remain anonymous is to be stated in 'Write a note' section, as well as a request to a specific league contribution or a prize.

5.2.2 PayPal contributions are converted into Dollars ($), if you send money in your local currency the prize pool host will cover the conversion fees.

5.2.3 Current Season 14 prize pool: TBA

## 5.3 Officials

5.3.1 The list of officials to contact is as follows:
* .won(.1)
* TTTPPP
* Anjew
* Milkman

5.3.2 RAGL has its own discord, it can be found here https://discord.gg/99zBDuS Please post in the discord with any questions. Please, refrain from using discord personal messages unless the matter is urgent and cannot be discussed by other means.

5.3.3 League officials reserve the rights to alter or override the rulebook at any time, including during an ongoing season. All players will be immediately notified if any substantial changes are made during the season. Any change to the rulebook after player registrations are over is duplicated via a post in this thread.

For all inquiries you can contact us through Discord or reply on this thread.

# Schedule Summary

* 2023-04-13 Map submission deadline
* 2023-04-20 Community map vote deadline
* 2023-04-27 Player registrations close
* 2023-05-01 Start of week 1
* 2023-06-19 Start of Playoffs
* 2023-07-09 Target for end of Playoffs
