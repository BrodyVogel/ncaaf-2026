# Roster reconciliation — depth-chart names the grade never mentions

_pipeline/roster_reconcile.py. Flags Athlon depth-chart players absent from the team's grade write-up. P1 = the Butler profile (a transfer in NEITHER the write-up NOR the CFBD portal pull — magazine-only, no data backstop). Review P1/P2 by hand; P3 is often a legit omission. roster_2026.json is empty field-wide and unused; coverage is the 21 teams with a parseable depth chart._


## P1 transfer/no-backstop — 7 flag(s)

| team | depth-chart entry | slot | in portal data? |
|---|---|---|---|
| Clemson | `Andy Burburija* (Jr)` (→ Burburija) | backup | NO |
| Oregon_State | `Bailey*(Jr.)` (→ Bailey) | starter | NO |
| Oregon_State | `Comer*` (→ Comer) | backup | NO |
| Utah_State | `Wade*` (→ Wade) | backup | NO |
| Virginia_Tech | `Michael Troutman III* (Fr, Penn State)` (→ Troutman) | backup | NO |
| Washington_State | `McKendry*` (→ McKendry) | backup | NO |
| Washington_State | `Hutson*` (→ Hutson) | backup | NO |

## P2 transfer dropped — 24 flag(s)

| team | depth-chart entry | slot | in portal data? |
|---|---|---|---|
| Boston_College | `Reed Swanson* (Jr, Colgate)` (→ Swanson) | backup | yes |
| Boston_College | `Veguer Jean-Jumeau* (So, Tennessee State` (→ Jean-Jumeau) | backup | yes |
| Boston_College | `Jani Norwood* (So, UNC)` (→ Norwood) | backup | yes |
| Boston_College | `Trevon Humphrey* (Sr, NC Central)` (→ Humphrey) | backup | yes |
| Boston_College | `Cameron Kossmann* (Fr, Florida)` (→ Kossmann) | backup | yes |
| California | `Cooper Perry* (So, Oregon)` (→ Perry) | starter | yes |
| California | `Jacob Arop* (So, South Dakota)` (→ Arop) | backup | yes |
| California | `Ashun Shepphard* (Sr, Mississippi State)` (→ Shepphard) | backup | yes |
| California | `Justin Beadles* (Sr, Louisville)` (→ Beadles) | backup | yes |
| Duke | `Braden Miller* (Sr, Cal)` (→ Miller) | backup | yes |
| Fresno_State | `Okafor*` (→ Okafor) | backup | yes |
| Fresno_State | `Stewart*` (→ Stewart) | starter | yes |
| Oregon_State | `Odoemenem*` (→ Odoemenem) | backup | yes |
| Syracuse | `Meyers*` (→ Meyers) | backup | yes |
| Utah_State | `Lynch*` (→ Lynch) | backup | yes |
| Utah_State | `Remenowsky*` (→ Remenowsky) | backup | yes |
| Utah_State | `Cunningham*` (→ Cunningham) | backup | yes |
| Virginia | `Ryan Brubaker* (Sr, South Carolina)` (→ Brubaker) | backup | yes |
| Virginia | `Ezekiel Larry* (Sr, Yale)` (→ Larry) | backup | yes |
| Virginia | `Jalen McNair* (Sr, Buffalo)` (→ McNair) | backup | yes |
| Virginia_Tech | `Marlion Jackson* (Sr, LA Tech)` (→ Jackson) | backup | yes |
| Washington_State | `Pedersen*` (→ Pedersen) | backup | yes |
| Washington_State | `Leaupepetele*` (→ Leaupepetele) | backup | yes |
| Washington_State | `Frausto-Ramos*` (→ Frausto-Ramos) | backup | yes |

## P3 starter unmentioned — 13 flag(s)

| team | depth-chart entry | slot | in portal data? |
|---|---|---|---|
| Boston_College | `Johnathan Montague Jr. (So)` (→ Montague) | starter | NO |
| Boston_College | `Syair Torrence (So)` (→ Torrence) | starter | NO |
| California | `Trevor Rogers` (→ Rogers) | starter | NO |
| Florida_State | `Jasen Lopez` (→ Lopez) | starter | NO |
| Florida_State | `return threats Singleton + Danzy + Lopez` (→ Carter) | starter | NO |
| Syracuse | `Hatcher` (→ Hatcher) | starter | NO |
| Syracuse | `Clement` (→ Clement) | starter | NO |
| Texas_State | `Landry(Jr.)` (→ Landry) | starter | NO |
| Texas_State | `Bradley(Fr.)` (→ Bradley) | starter | NO |
| Virginia | `Dillon Newton-Short (So)` (→ Newton-Short) | starter | NO |
| Virginia_Tech | `Brody Meadows (Sr)` (→ Meadows) | starter | NO |
| Wake_Forest | `Elliot Demaine (Fr)` (→ Demaine) | starter | NO |
| Wake_Forest | `Ashaad Williams (Sr, yr4)` (→ Williams) | starter | NO |

## Coverage

Covered (21 teams w/ Athlon depth chart): Boston_College, California, Clemson, Duke, Florida_State, Fresno_State, Oklahoma_State, Oregon_State, San_Diego_State, Syracuse, TCU, Texas_State, Texas_Tech, UCF, Utah, Utah_State, Virginia, Virginia_Tech, Wake_Forest, Washington_State, West_Virginia.


Not covered (117 teams — no parseable depth chart; would need prose parsing): Air_Force, Akron, Alabama, App_State, Arizona, Arizona_State, Arkansas, Arkansas_State, Army, Auburn, BYU, Ball_State, Baylor, Boise_State, Bowling_Green, Buffalo, Central_Michigan, Charlotte, Cincinnati, Coastal_Carolina, Colorado, Colorado_State, Delaware, East_Carolina, Eastern_Michigan, Florida, Florida_Atlantic, Florida_International, Georgia, Georgia_Southern, Georgia_State, Georgia_Tech, Hawai'i, Houston, Illinois, Indiana, Iowa, Iowa_State, Jacksonville_State, James_Madison, Kansas, Kansas_State, Kennesaw_State, Kent_State, Kentucky, LSU, Liberty, Louisiana, Louisiana_Tech, Louisville, Marshall, Maryland, Massachusetts, Memphis, Miami, Miami_(OH), Michigan, Michigan_State, Middle_Tennessee, Minnesota, Mississippi_State, Missouri, Missouri_State, NC_State, Navy, Nebraska, Nevada, New_Mexico, New_Mexico_State, North_Carolina, North_Dakota_State, North_Texas, Northern_Illinois, Northwestern, Notre_Dame, Ohio, Ohio_State, Oklahoma, Old_Dominion, Ole_Miss, Oregon, Penn_State, Pittsburgh, Purdue, Rice, Rutgers, SMU, Sacramento_State, Sam_Houston, San_José_State, South_Alabama, South_Carolina, South_Florida, Southern_Miss, Stanford, Temple, Tennessee, Texas, Texas_A&M, Toledo, Troy, Tulane, Tulsa, UAB, UCLA, UConn, UL_Monroe, UNLV, USC, UTEP, UTSA, Vanderbilt, Washington, Western_Kentucky, Western_Michigan, Wisconsin, Wyoming.

