# DestinyPowerLeveling

Requirements: Python 3.7+

Meaning of the variables:
item: List with the length of 8 - each element means 1 item slot (3 weapons, 5 armor pieces) - the order doesn't matter

activities: How many rewards are still unclaimed:  [Tier1, Tier2, Tier3/pinnacle]
example -> VoG gives 5 Tier3, Strikes give 1 Pinnacle, Nightfall completions gives Tier 1 and 100k nightfall gives T3 
this results in [1,0,7]

simulate_runs: Number of times the rewards get pulled in a random order

analyze_first_n_drops: 3 means the program returns the best way to complete the next up to 3 challenges 
example -> (1,3,3) means first do T1 then T3 then T3 
