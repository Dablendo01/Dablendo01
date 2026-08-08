# -*- coding: utf-8 -*-
# Story 12 "The Condemned Widow" — VO-synced shot list builder.
# Pairs authored prompts with scene_calculator.py timecodes (narration-only, 23:02 = 1382s).
# Ingredients: Adeline | Clement (minimal, menacing shadow only) | Ambrose Sutter | Dr. Ashford
#   | Opal Marsh | (circuit judge, generic).
# SENSITIVE: the killing is IMPLIED (kicked door, raised gun, a muzzle flash / the moment after) —
# no body, no gore. Bruises shown tastefully/dignified, never exploitative. Gallows shown as a
# suspense object but NO hanging/no body. Papers TEXT-FREE. Names inline. No mid-body em-dashes.
import csv

PROMPTS = [
# ---- COLD OPEN (person + injustice; the gallows clock) ----
"Adeline — A pale composed young woman of twenty-six stands at a small barred cell window listening, dread in her level face, the sound of hammers beyond, cold gray light",
"Adeline — A young woman behind bars looks down through a small window at a courthouse square, a trial deciding her life, tense stillness, cold daylight",
"Men in a sunlit town square raising the raw wooden frame of a gallows with hammers and saws, built before a verdict, grim, flat daylight",
"Adeline — A young woman sits alone on a cell cot listening to her own gallows going up plank by plank, cold certainty on her face, dim barred light",
"A rope being measured and looped over a new gallows beam in a town square, the only question how many hours, cold bright light",
"Dr. Ashford — A weary country doctor with a black bag stands grave and troubled at the edge of the square, a terrible knowledge in his eyes, gray daylight",
"Adeline — Close on a condemned young woman's face, already hanged in the town's heart, quiet and unbroken, cold light",
"A frontier town street where cruel news travels fast, townsfolk clustered and murmuring, judgment in the air, flat daylight",
"Clement — A rich charming young man laughs among a crowd on a boardwalk, the town's false golden hero, warm daylight",
"Clement — Close on a charming man's public smile shading into a cruel drunken edge, the private brute behind the mask, dim saloon light",
"Adeline — A quiet proud young widow works her small failing farm alone at the edge of town, dignified in poverty, gray daylight",
"Adeline — A young widow stands accused and alone before a hard-faced frontier town, judged before she is heard, flat daylight",
"Adeline — A quiet young widow in a plain worn dress keeps to herself on a poor homestead, proud and self-reliant, soft gray light",
"Adeline — A young woman works poor land with her own two hands, paying her way and troubling no one, gray daylight",
"Adeline — A lone young widow on the edge of town with no man to stand for her, terribly unprotected, wide bleak light",
"Clement, Adeline — A rich man's shadow looms at a lonely farmhouse at dusk while a woman stands wary within, an unwanted menace, cold blue evening",
"Adeline — A young widow speaks to a dismissive frontier sheriff who waves her off, turned away by the law, flat daylight",
"Adeline — A young woman alone in a poor lamplit kitchen at night, bracing for a thing she knows is coming, tense warm-dim light",
"A heavy cabin door bursts inward on a cold night, a young woman recoiling in her own kitchen, sudden violence at the threshold, dim lamplight",
"Adeline — Close on a young woman's hand taking an old revolver down from a high kitchen shelf, desperate resolve, dim lamplight",
"Adeline — A terrified resolute young woman stands in her kitchen holding an old revolver in both shaking hands, warning an intruder off, dim lamplight",
"Clement, Adeline — A large threatening shadow of a man advances across a lamplit kitchen toward a woman with a raised gun, menace, dim light",
"Adeline — A single muzzle flash lights a dark kitchen for an instant then a woman stands frozen with the lowered gun and drifting smoke, the aftermath, dim light (no body shown)",
"Dr. Ashford — A grave country doctor examines a powder-burned shirt by lamplight, reading a close-range shot, somber medical study, dim light (no body)",
"Adeline — A dignified young woman with dark bruise marks at her throat and wrists stands under arrest, wronged and composed, cold gray light",
"Dr. Ashford — A country doctor writes careful notes at a desk by lamplight, recording the truth of what he saw, grave, warm dim light (writing not legible)",
"Dr. Ashford — Close on a weary honest doctor's face, certain from the first hour this was no murder, troubled, lamplight",
"Dr. Ashford — A doctor sits with his head bowed and a folded paper in his hands, torn between conscience and the ruin the truth will bring, dim light",
"Ambrose Sutter — A powerful proud frontier man of about fifty-eight in a fine dark suit, cold grief-hardened face, commanding and dangerous, dim study light",
"Ambrose Sutter — A ruthless self-made man stands before a great map of holdings, an empire built with hard hands, cold lamplight",
"Ambrose Sutter — Close on a grieving powerful man's face turning from sorrow to a black total rage, the most dangerous thing in the world, dim light",
"Ambrose Sutter — A proud man clutches a portrait of his son, refusing to hear one word against him, grief turned to fury, dim lamplight",
"Ambrose Sutter — A rich man speaks quietly to a nervous prosecutor and a compromised judge in a lamplit room, buying a trial, cold intent",
"Ambrose Sutter — A powerful banker lets a quiet threat be known to frightened townsmen, ruin promised to any who speak up, cold daylight",
"Men build a gallows in a town square while a trial goes on, a rich man's message that the verdict is already decided, grim daylight",
"A frontier courtroom mid-trial, a browbeaten crowd, the outcome a foregone thing, tense pale window light",
"A prosecutor gestures at a silent accused woman before a packed courtroom, painting a cruel false picture, pale daylight",
"Adeline — A young woman sits still in the dock with fading bruises at her throat, listening to a town build the lie that will kill her, pale light",
"Adeline — Close on a condemned young woman's face that has given up, a terrible quiet peace, pale courtroom light",
"Opal Marsh — A work-worn frontier farm wife of about thirty-five with children at a poor homestead, a nobody with every reason to keep her head down, gray daylight",
"Opal Marsh — A neighbor woman recalls a man's horse tied outside a lonely farm at dusk and a distant cry, a witness who cannot forget, blue evening",
"Opal Marsh — A frightened farm wife rises trembling and uninvited in a courtroom, sudden reckless courage, pale window light",
"Opal Marsh — A trembling farm wife speaks out across a hushed courtroom, saying the unsayable about a dead golden man, pale light",
"Opal Marsh, Ambrose Sutter — A farm wife falters as a rich man turns in his seat with a face like winter, a charged cruel gap, pale light",
"Ambrose Sutter — A banker at a desk coldly calls in a family's note the next morning, the price of a few brave words, dim lamplight (papers not legible)",
"Dr. Ashford — A doctor sits stricken at the back of a courtroom, a single brave voice having cracked the lie, sick to his soul, pale light",
"Dr. Ashford — A weary doctor grips a black medical bag holding a written examination, the proof he has hidden in his fear, tense dim light",
"Dr. Ashford — Close on a doctor's ashamed frightened face, afraid of a rich man and the ruin that fell on a brave neighbor, dim light",
"Adeline, Dr. Ashford — A doctor watches a condemned woman led back past a half-built gallows, her face gone hopeless, and something turns in him, gray daylight",
"Dr. Ashford — A doctor sits up alone through the night with a folded paper in his hands, wrestling with his conscience, low lamplight",
"Dr. Ashford — A doctor's face resolving at his desk at dawn, a father's words remembered, low first light",
"A finished gallows standing whole in a town square, the rope hung and turning in the wind, seen from a small barred cell window, cold bleak light",
"Dr. Ashford — A doctor's resolute face at first light having made his choice, ready to set out, cold morning",
"Dr. Ashford — A doctor rides out at dawn toward another town, carrying his paper beyond the rich man's reach, cold morning light",
"Dr. Ashford, circuit judge — A doctor lays a written examination on an outside judge's desk and speaks urgently, the truth at last, lamplit office (papers not legible)",
"Dr. Ashford — A doctor speaks with a shaking voice but steady hands, done being afraid, grave resolve, lamplight",
"Dr. Ashford, circuit judge — A doctor pleads across a desk that an innocent woman will hang within the week unless the judge acts, tense lamplight",
"The circuit judge reads a doctor's written examination gravely at his desk, weighing a life, lamplight (papers not legible)",
"The circuit judge stands with grave authority, ordering the bought trial halted and reopened before his own bench, commanding light",
"Ambrose Sutter — A powerful man's face darkening as he feels his control slipping, a proud man losing his grip, dim light",
"A frontier courthouse packed to bursting for the new hearing, the whole county come to watch, tense pale window light",
"Ambrose Sutter — A rich man sits front row white with fury, his lawyers around him, fixing a cold ruinous stare, pale courtroom light",
"Dr. Ashford, Ambrose Sutter — A doctor takes the witness stand and meets a rich man's ruinous stare, beginning to tell the truth of a close-range defensive shot, charged gap, pale daylight",
"Dr. Ashford — A doctor testifies of dated drawn bruises, the marks of a large man's hands on a woman's throat, grave, pale light",
"Dr. Ashford — A doctor lays the dead man's own body out in calm medical words as a witness that cannot be bought, a rapt courtroom, pale light",
"Dr. Ashford — A doctor speaks gravely into a silent courtroom, the truth of a home invasion plain at last, pale window light",
"Dr. Ashford — Close on a doctor's face confessing he hid the proof in fear, honest at last, pale light",
"Ambrose Sutter — A powerful man surges up out of his seat roaring, the naked rage of a man watching the truth escape him, pale courtroom light",
"Ambrose Sutter — A rich man shouts ruinous threats at the doctor, money raging against the truth, pale light",
"Ambrose Sutter, circuit judge — A furious rich man faced down by a stern circuit judge threatening him with a cell, authority against money, pale light",
"Adeline — A condemned young woman who has been spoken over the whole trial, silent and still, the judge turning to her, pale window light",
"Adeline — A young woman who had given up rises slowly to speak, finding she is not done, quiet strength, pale light",
"Adeline — A young widow speaks steadily to a hushed courtroom, telling how she asked for help and was turned away, pale light",
"Adeline — A young woman looks row by row at the town that abandoned her, unflinching, pale window light",
"Adeline — A young woman quietly names the town's cowardice, its nerve owned by a rich man, pale light",
"Adeline — A young woman states plainly she fired one shot to save her own life, dignified and unashamed, pale courtroom light",
"Adeline, Ambrose Sutter — A young widow faces a grieving rich man without flinching across a charged courtroom gap, pale light",
"Adeline, Ambrose Sutter — A young woman tells a rich man his own certainty raised the son who died with his hands on her throat, truth between them, pale daylight",
"Adeline — A young woman says her whole crime was telling a powerful man no, a courtroom holding its breath, pale light",
"The circuit judge speaks the verdict into a hushed room, a killing in lawful defense, a woman cleared, grave relief, pale window light",
"Men tear a gallows apart plank by plank in a town square while the whole town watches, an undoing, cold bright light",
"Ambrose Sutter — A broken powerful man leaves a fine house, ruined where money cannot reach, cold gray light",
"Ambrose Sutter — A lone rich man rides away from the county to grieve a son who never was, the loneliest grief, bleak light",
"Dr. Ashford — Townsfolk who once looked away now stand behind the doctor who stood up first, courage contagious, warm daylight",
"Dr. Ashford — A country doctor tends a patient by warm lamplight, his practice grown, a man a town now trusts, warm glow",
"Opal Marsh — A grateful farm wife stands on her saved farm with her children, brave words rewarded, golden light",
"Adeline — A young widow works her poor farm and walks the main street of the town that condemned her with her head held high, gold daylight",
"Adeline — A young woman makes the town that wronged her meet her eye, a place beginning to change, gold light",
"Adeline — A steady woman answers a call to stand for another woman alone, the one who will never look away again, warm resolve, gold light",
"A frontier town at golden dusk where a hard tale is still told by firelight, the gallows and the widow remembered, warm long shadows",
"Adeline — A lone dignified widow standing on the edge of town, the true measure of a place, gold light",
"Opal Marsh, Dr. Ashford, Adeline — A neighbor woman, a country doctor, and a widow standing together, the quiet ones who stopped being afraid, warm golden light",
"An empty town square at dawn where a gallows once stood, a rich man's tool of fear gone, one soul's courage having spread, cold light warming to gold",
"A single glowing oil lantern on a plank table with dust drifting in its light against a dark background, the story closing, warm intimate glow",
]

ANCHOR = ", 1880s American Old West frontier, period-accurate frontier clothing and props, no modern objects, no contemporary clothing"

def run():
    rows = list(csv.DictReader(open("Story12-Scenes.csv")))
    assert len(rows) == len(PROMPTS), f"{len(rows)} scenes vs {len(PROMPTS)} prompts"
    stamped = [p + ANCHOR for p in PROMPTS]
    out = []
    for r, p in zip(rows, stamped):
        out.append(f"SCENE {int(r['scene']):03d} | {r['in']}-{r['out']} ({float(r['dur_s']):.1f}s)\n{p}")
    open("Story12-CondemnedWidow-ShotList.txt", "w").write("\n\n\n".join(out) + "\n")
    open("Story12-CondemnedWidow-Prompts-Only.txt", "w").write("\n\n\n".join(stamped) + "\n")
    durs = [float(r["dur_s"]) for r in rows]
    print(f"{len(rows)} scenes | {sum(durs)/60:.1f} min | {sum(durs):.0f}s (VO 23:02 = 1382s) | "
          f"shortest {min(durs):.1f}s longest {max(durs):.1f}s")

run()
