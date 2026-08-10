# -*- coding: utf-8 -*-
# Story 13 "The Blind Rancher / Hidden Wealth" — VO-synced shot list builder.
# Pairs authored prompts with scene_calculator.py timecodes (narration-only, 17:20 = 1040s).
# Ingredients: Susannah | Ephraim | Rowena | Warren | Emmett | (city lawyer, generic).
# Blindness with dignity (clouded eyes, straight bearing). Skillet blow IMPLIED (raised arm /
# aftermath), no gore. Letters/deeds/papers TEXT-FREE. Names inline. No mid-body em-dashes.
# 74 prompts, one per scene, 1:1 with the narration.
import csv

PROMPTS = [
"Susannah — A plain dignified woman of thirty-one in a modest dress stands on a frontier street as townsfolk laugh and whisper, mocked for her coming marriage, flat daylight",  # 1
"Susannah, Ephraim — A plain spinster and a blind rancher with clouded eyes stand as the town's pitiful match, he at a hardscrabble spread, cold daylight",  # 2
"Townsfolk on church steps and a mercantile porch laughing cruelly, two leftovers they call them, careless mockery, flat daylight",  # 3
"Rowena — A vain pretty frontier belle laughs loudest on a boardwalk, fanning herself, a cutting cruel remark, bright daylight",  # 4
"Susannah — Close on a plain woman's calm face that has already seen a truth the laughing town has not, quiet knowing, soft light",  # 5
"Susannah, Ephraim — A plain woman and a blind rancher together, the two the town laughed at and the only two paying attention, warm quiet light",  # 6
"Susannah — A plain woman sits alone in a church pew among couples and families, dignified in her solitude, pale window light",  # 7
"Susannah — A plain woman keeps house alone in a small tidy home, years of quiet loneliness behind her, soft daylight",  # 8
"Susannah — A plain woman sews by a window and tends a good garden, self-reliant and proud, gentle daylight",  # 9
"Susannah — Close on a plain woman's kind unbittered face, softened by hard years rather than soured, warm light",  # 10
"Ephraim — A blind rancher of about thirty-eight with clouded eyes and a straight bearing sits alone in a quiet ranch house, written off by the town, dim light",  # 11
"Ephraim, Emmett — A blind rancher and his weathered loyal old foreman on a spread at the end of the valley, quiet isolation, gray daylight",  # 12
"Susannah — A plain woman drives a little cart out along a valley road toward a distant ranch, carrying kindness, soft afternoon light",  # 13
"Susannah, Ephraim — A plain woman reads aloud from a book to a blind rancher in a ranch parlor, an afternoon ritual, warm lamplight",  # 14
"Susannah, Ephraim — A blind rancher listens with a softening face as a woman reads, coming to know her quick warm mind, warm glow",  # 15
"Susannah, Ephraim — A blind rancher and a plain woman lean close in tender understanding, a soul meeting a soul, warm intimate light",  # 16
"Ephraim — A blind rancher at a plain-seeming ranch the whole town believes is poor, a recluse thought to have nothing, dim gray light",  # 17
"Ephraim — Close on a blind rancher's composed careful face, content to let the town believe him a poor man, safe in being underestimated, dim light",  # 18
"A wide valley range that looks poor and hardscrabble on the surface, hiding its true worth, gray daylight",  # 19
"A vast rich cattle range with fine herds under open sky, the best water and graze, the hidden fortune, cold bright light",  # 20
"Ephraim — A blind rancher sits quietly composed, secretly one of the wealthiest cattlemen for two hundred miles, dim lamplight",  # 21
"Susannah, Ephraim — A woman falters mid-reading over a banker's letter as a blind rancher gently says now you know, a secret shared, warm lamplight (letter text not legible)",  # 22
"Susannah — A plain woman sits quietly holding a letter, entrusted with a great secret, thoughtful, warm light (paper text not legible)",  # 23
"Susannah, Ephraim — A woman goes on reading to a blind rancher unchanged by what she knows, keeping his secret month after month, warm glow",  # 24
"Susannah — Close on a plain woman's resolute face, refusing to become one of the grasping people, integrity, soft light",  # 25
"Susannah, Ephraim — A blind rancher takes a plain woman's hand and asks her plainly to marry him, tender and grave, warm lamplight",  # 26
"Susannah, Ephraim — A blind rancher speaks earnestly to a woman about the mockery they will bear, only they knowing the truth, warm intimate light",  # 27
"Susannah — A plain woman answers yes with quiet steady love, a hard choice made gladly, warm glow",  # 28
"Susannah — A plain woman holds her head high amid whispering mocking townsfolk in a mercantile, unbowed, flat daylight",  # 29
"Rowena — A vain belle mocks a plain woman sweetly and cruelly on a boardwalk, sport for the winter, bright daylight",  # 30
"Susannah, Rowena — A plain woman smiles calmly and walks on past a sneering belle, unruffled, which infuriates the mocker, flat daylight",  # 31
"Warren — A smiling empty grasping young man watches a ranch with covetous eyes, a laugher with a reason, dim light",  # 32
"Warren, Ephraim — A smiling young man feigns warmth toward a blind uncle he has long waited to inherit from, false and patient, dim parlor light",  # 33
"Warren — Close on a grasping young man's calculating face, certain the ranch is his by rights, greed, dim light",  # 34
"Warren, Susannah — A grasping young man watches a plain woman move into a ranch house he had counted on, dark busy thoughts, dim light",  # 35
"Warren — Close on a grasping man knowing a fortune hides under the hardscrabble, secret greed, dim light",  # 36
"Warren — A smiling nephew arrives at a ranch that spring, warm-faced and scheming to break a marriage from the inside, dim daylight",  # 37
"Warren, Ephraim — A smiling nephew sits close by a blind uncle, going at the one seam he can split, a blind man's fear of being fooled, dim parlor light",  # 38
"Warren, Ephraim — A nephew murmurs a patient poison into a blind uncle's ear, gentle treachery, dim lamplight",  # 39
"Warren, Ephraim — A nephew leans in twisting a doubt about the plain wife into a blind uncle's ear, a cruel clever lie, dim light",  # 40
"Warren — Close on a young man's falsely concerned face as a patient lie takes hold, treachery, dim light",  # 41
"Ephraim — A blind rancher grows quiet and troubled, unable to watch a face for the truth, a doubt rooting in the dark, dim light",  # 42
"Susannah, Ephraim — A plain woman feels her blind husband pulling coolly away and cannot understand why, old loneliness creeping back, dim ranch light",  # 43
"Susannah — Close on a plain woman's hurt bewildered face as the one man who saw her whole seems to lose sight of her, dim light",  # 44
"Warren — A greedy man in the night decides not to wait on whispers any longer, debts pressing, a dark resolve, cold night",  # 45
"Warren — A smiling man slips toward a ranch house in the dark believing the wife gone to town, murder in mind, cold blue night",  # 46
"Warren — A man moves through a dark ranch yard alone, the foreman away, the blind uncle unguarded, cold night",  # 47
"Susannah — A plain woman returns home early and stands in a dark ranch house hearing a wary voice from the front room, alarm, dim night",  # 48
"Ephraim, Warren — A blind rancher speaks warily into the dark asking who is there, fear in his voice, a shadowed intruder near, cold night",  # 49
"Susannah — A plain woman moves silent and sure through a pitch-dark house she knows by heart, unseen, tense cold night",  # 50
"Susannah, Warren — In a black hallway a woman comes upon an intruder whose hand is on her husband's arm, an iron skillet raised, the instant before, cold night (no gore)",  # 51
"Susannah, Ephraim — A plain woman holds her trembling blind husband in lamplight, an intruder dropped in the dark behind them, waiting for dawn, warm lamp and cold night",  # 52
"Susannah, Ephraim — In gray dawn a woman shows her blind husband a forged paper and unpaid debts found on the intruder, the whole plot understood, cold morning light (papers not legible)",  # 53
"Ephraim — A blind rancher's first instinct to hush it all and stay hidden and safe, a quiet grim morning, dim light",  # 54
"Susannah, Ephraim — A plain woman speaks firmly to her blind husband, no more hiding, no more being nothing, resolve, morning light",  # 55
"Susannah — Close on a plain woman's determined face, done letting the town call her husband nothing, morning light",  # 56
"Susannah, Ephraim — A plain woman walks her blind husband up to the church in Juniper Flat on a Sunday, heads turning, pale daylight",  # 57
"A fine city lawyer in a good coat stands on the church steps before the gathered town and reads aloud, Rowena caught mid-laugh, pale daylight (papers not legible)",  # 58
"A vast rich cattle range and fine herds revealed as the truth of the Vickery fortune, cold bright light",  # 59
"The whole town of Juniper Flat frozen on the church steps in stunned silence, laughter dying, pale cold light",  # 60
"Rowena — A vain belle's fan stops moving and her mocking face goes pale with shock, pale daylight",  # 61
"Susannah, Ephraim — A plain woman on the church steps chosen out of all the world by a man who could not be fooled by a face, quiet vindication, pale light",  # 62
"Susannah — A plain woman in her Sunday dress looks level and calm over the town that mocked her, no gloating, quiet strength, pale daylight",  # 63
"Susannah, Ephraim — A plain woman takes her blind husband's arm and walks him down the church steps through a carved silence, dignified, pale light",  # 64
"Susannah, Ephraim — A plain woman and a blind rancher live a long full contented life at the end of the valley, warm golden light",  # 65
"Susannah — A woman kindly reads to other blind and shut-in souls and hires those who once mocked her, mercy not cruelty, warm daylight",  # 66
"Warren — A grasping man led away to territorial prison, beaten at the one game he thought he could not lose, cold gray light",  # 67
"Rowena — A vain belle years on in a cold unhappy marriage, bitter and fine-faced, dim light",  # 68
"Susannah — Close on a plain woman's kind quiet beloved face, the most loved woman in the valley, warm light",  # 69
"Susannah, Ephraim — A plain woman and a blind rancher together, she loved from the first for the only things that were truly her, warm glow",  # 70
"Susannah — Close on a plain woman's face, her stubborn quiet goodness found at last by the one man looking in the dark, warm light",  # 71
"An old shelf where the world sets the ones it overlooks, a quiet reproach, soft symbolic light",  # 72
"Susannah, Ephraim — A plain woman and a blind rancher walking together in golden evening light, seen at last for what they are, warm long shadows",  # 73
"A single glowing oil lantern on a plank table with dust drifting in its light against a dark background, the story closing, warm intimate glow",  # 74
]

ANCHOR = ", 1880s American Old West frontier, period-accurate frontier clothing and props, no modern objects, no contemporary clothing"

def run():
    rows = list(csv.DictReader(open("Story13-Scenes.csv")))
    assert len(rows) == len(PROMPTS), f"{len(rows)} scenes vs {len(PROMPTS)} prompts"
    stamped = [p + ANCHOR for p in PROMPTS]
    out = []
    for r, p in zip(rows, stamped):
        out.append(f"SCENE {int(r['scene']):03d} | {r['in']}-{r['out']} ({float(r['dur_s']):.1f}s)\n{p}")
    open("Story13-BlindRancher-ShotList.txt", "w").write("\n\n\n".join(out) + "\n")
    open("Story13-BlindRancher-Prompts-Only.txt", "w").write("\n\n\n".join(stamped) + "\n")
    durs = [float(r["dur_s"]) for r in rows]
    print(f"{len(rows)} scenes | {sum(durs)/60:.1f} min | {sum(durs):.0f}s (VO 17:20 = 1040s) | "
          f"shortest {min(durs):.1f}s longest {max(durs):.1f}s")

run()
