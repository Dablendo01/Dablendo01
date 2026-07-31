# -*- coding: utf-8 -*-
# Story 9 "The Hired Girl / the Will" — VO-synced shot list builder.
# Pairs authored prompts with scene_calculator.py timecodes (narration-only, 22:57 = 1377s).
# Ingredients: Clara | Cordelia (+frail) | Louisa | Rufus | Judge Harlan | Levi.
# Text-free props (no readable will/ledger text). Names inline. No em-dashes in prompt bodies.
import csv

PROMPTS = [
# ---- COLD OPEN (first shot is the person, per intro-cliff doctrine) ----
"Clara — A young woman of nineteen in a plain gray dress sits alone on an overturned bucket in a dark barn eating cold supper from a tin plate, one warm lantern beside her, dim horses behind, frozen winter night",
"A poor lamplit frontier kitchen glowing warm through a window seen from a cold blue yard, a family at a full table within, a lonely lit ranch house far up a dark valley hill beyond, cold blue night",
"Clara — A quiet young woman stands framed in an open barn doorway with a tin plate, warm lantern behind her and cold snow before her, two long winters of silence in her face, dusk",
# ---- ACT 1: the girl in the barn ----
"Clara — A ragged seventeen year old girl sits on frozen church steps at dawn with everything she owns tied in a flour sack, orphaned and alone, pale cold morning light",
"Two fresh snow graves with plain wooden markers on a bleak frontier hillside, a lone girl standing small before them, gray winter light",
"Rufus — A self satisfied frontier rancher in a good black coat with his thumbs in his vest stands outside a clapboard church nodding to neighbors, smug and pious, flat daylight",
"Clara — A young hired girl on her knees scrubbing a plank floor before sunrise, exhausted and uncomplaining, a single candle, cold blue predawn kitchen",
"Rufus — A closed hard faced rancher counts coins into a tin at a desk, giving nothing away, tight and miserly, dim lamplight",
"Louisa — A handsome cold faced frontier woman in a fine dark high collared dress stands in a warm parlor with a careful appraising look, soft cruelty, lamplight",
"Louisa — A poised woman in fine dress presides over a front church pew and a lamplit social, gathering flattery, queenly and cold, warm interior light",
"Louisa, Clara — A cold elegant woman lifts a hand to stop a plain gray clad hired girl from sitting at the family supper table, a soft cruel refusal, warm kitchen lamplight",
"Louisa — Close up of a handsome woman speaking softly with a small pleasant smile that does not reach her cold eyes, teaching cruelty gently, lamplight",
"Clara — A young woman presses her face into a horse's mane in a dark barn, crying silently so none will hear, one lantern low, cold night",
"Clara — Close up of a young woman's composed face learning to fold pain away small and hard, quiet dignity not tears, warm lantern glow",
"Clara — A hired girl works a washboard in gray dawn light, rising in the dark and laboring till dark, tireless and unthanked, cold morning",
"A frontier main street of Cottonwood in winter, townsfolk passing, an uneasy shared knowing in the air, flat gray daylight",
"Townsfolk at a general store counter pressing their lips and looking away, easy cowardice, dusty daylight through the window",
"Cordelia — A big weathered ranch house alone at the top of a pine road that no one visits, isolated and grand, cold clear winter light",
"Cordelia — A proud sharp eyed widow near eighty in a fine faded shawl sits amid fine things in a cold grand parlor, the richest and loneliest woman in the valley, dim light",
"A vast snow dusted cattle range under open sky, four thousand acres of the best grass and the only water for forty miles, cold bright light",
"Cordelia — Close up of an old widow's guarded eyes that have learned to see the money hunger behind every smile, sharp and weary, lamplight",
"Rufus, Louisa — A prosperous couple climb a pine road carrying a basket toward a grand ranch house, smiling and false, cold daylight",
"Cordelia — An old widow watches a smiling couple from a cold window with plain distaste, seeing the greed behind the baskets, dim interior light",
"Clara — A plain young hired girl carries a covered basket up a snowy pine road on a bitter January afternoon, sent on an errand no one else wanted, cold light",
"Cordelia — A frail old widow sits alone by a dead cold hearth in a fine room wrapped in a shawl, too proud to call for help and too weak to lay a fire, gray light",
"Clara, Cordelia — A young girl in a doorway meets the eyes of a low and shivering old widow, recognition of a shared coldness, pale winter light",
"Clara — A young woman kneels at a great hearth building a fire up until it roars, warm firelight beginning to fill a cold grand room, tender purpose",
"Clara, Cordelia — A young girl sits on a low stool holding a cup of broth steady to the lips of a frail old widow whose hands shake, warm firelight, quiet care",
"Cordelia, Clara — A sharp old widow studies a plain honest girl with a hard challenging look across a firelit room, testing her, warm glow",
"Cordelia — Close up of a stony old widow's face as something cracks and softens, surprised by an honest soul after twenty years, warm firelight",
# ---- ACT 2: the only kindness ----
"Clara — A young woman climbs a pine road in the gray hour before dawn on her own time, faithful and unpaid, cold blue light, a lit house above",
"Clara — A young woman stacks firewood by a great hearth, warming a house for no reward, refusing to let a thing be cold, warm firelight",
"Cordelia, Clara — An old widow presses coins on a young girl who gently refuses and keeps stacking wood, a kindness that will not be bought, firelight",
"Clara, Cordelia — A young woman reads aloud by lamplight to an old widow in a deep chair, an evening ritual of tenderness, warm glow",
"Clara, Cordelia — A young girl gently combs out an old widow's long white hair by firelight, patient devotion, warm intimate light",
"Cordelia, Clara — A frail old widow grips a young girl's wrist with sudden strength, earnest and moved, firelight on both faces, tender gravity",
"Cordelia — Close up of an old widow's softened eyes, having made a lifelong study of who comes for love and who for money, warm lamplight",
"Clara — A hired girl carries a plate across a frozen dark yard toward a barn, back in her old silence, cold blue night, the Sennett house glowing behind",
"Louisa — A striving cold woman berates a servant in a fine parlor, crueler as a grand church social nears, tense warm light",
"A grand front room being prepared for a lavish church social, lamps lit and a long laden table, the biggest night of the year, warm anticipatory light",
"Louisa — A poised woman in a fine new dress moves like a queen through a crowded lamplit social soaking up flattery, warm glowing room",
"Clara — A plain gray clad hired girl carries and clears dishes along the shadowed edges of a bright crowded party, invisible and tireless, warm light",
"Levi, Clara — A kind young ranch hand pulls out a chair and gestures a weary hired girl toward it in a crowded warm room, an innocent kindness, lamplight",
"Louisa, Clara — A cold elegant woman turns with a soft cruel smile to the whole room, shaming a plain gray clad girl before the county, warm lit party, every face turning",
"Louisa — Close up of a handsome woman delivering a soft laughing cruelty, the help eats in the barn, cold eyes and a sweet smile, warm lamplight",
"Clara — A young woman stands very still holding a stack of dirty plates and answers with a steady unshaking face, dignity under humiliation, warm party light behind",
"Clara — A gray clad girl carries plates out across a frozen yard to a dark barn while a warm party glows behind her in the house, cold blue night",
"Levi — A young ranch hand sits with his ears burning red, ashamed of a cruelty he did not commit, warm crowded room, downcast",
"Cordelia — A frail old widow at a writing desk by lamplight sets her trembling hand to a paper, the last thing she will ever sign, warm low lamp, night",
"Cordelia — A still cold bedroom at first light, an old widow at peace in her bed as if sleeping, a life ended alone, pale gray morning",
# ---- MID-ROLL CLIFF: the death and the question ----
"Clara — A young woman with a cloth wrapped loaf halts in a doorway, feeling the house gone still and cold, dread and grief dawning, gray morning light",
"Clara, Cordelia — A young woman sits on a low stool holding the still hand of an old widow at peace in her bed, weeping real tears, pale gray light",
"Clara — A young woman gently combs an old widow's white hair one last time with bowed head, grief and devotion, soft cold light",
"A frontier main street stirring to sudden greedy life, townsfolk gathering and murmuring, the question of the Tate land in every face, gray daylight",
"Rufus — A rancher pulls on a black coat with unseemly haste before the body is cold, hungry for an inheritance, dim room, cold light",
"Louisa — A cold woman stands gazing over a vast snowy range as if already its mistress, scheming who to freeze out first, cold bright light",
"Judge Harlan — A stern white whiskered judge in a dark coat rides into a frontier town after two days on the road, weary and upright, cold daylight",
# ---- ACT 3: the reading of the will ----
"A packed frontier courthouse crowded with townsfolk come to hear a will read, tense and greedy, pale daylight through tall windows",
"Rufus, Louisa — A prosperous couple sit up front, the woman in fine mourning black with chin high wearing sorrow like a costume, the man thumbs in his vest, cold window light",
"Clara — A plain gray clad young woman stands quietly at the very back by the door, expecting nothing, pale light from the doorway",
"Levi, Clara — A young ranch hand stands protectively near a gray clad girl at the back of a hushed courtroom, steady and near, pale daylight",
"Judge Harlan — An old judge unfolds a paper and settles his spectacles as a courtroom goes dead silent, grave authority, window light",
"Louisa — A woman in fine mourning black shifts with impatience in a front pew, hungry for the only part she cares about, cold window light",
"Judge Harlan — An old judge reads aloud from a paper with hard flat eyes, his voice grave and even, a frozen silent courtroom, pale daylight",
"Louisa — Close up of a woman's proud face turning from lifted triumph to confusion as the words land wrong, dawning unease, cold light",
"Louisa — Close up of a woman's face going white with a terrible dawning horror as she is left nothing at all, composure collapsing, cold window light",
"Judge Harlan — An old judge reads on, speaking a name to a breathless courtroom, grave and clear, pale daylight through tall windows",
"Judge Harlan, Clara — An old judge folds a paper and lifts his eyes over his spectacles toward the back where a gray clad girl stands with a hand pressed over her mouth, the whole room turning, daylight",
"Judge Harlan, Clara — A kind stern judge beckons a stunned gray clad girl to come forward through a courtroom of turning faces, a nobody named the heir, daylight",
# ---- ACT 3: the longest walk ----
"Clara — A young woman in a plain gray dress begins to walk slowly up a long courtroom aisle from the back, quiet and steady, pale daylight",
"Clara — A gray clad young woman passes the merchants wives and the men who mocked her and the Sennett pew, giving no triumph, calm and level, daylight",
"Clara — A young woman in a plain gray dress walks quiet and steady as a whole courtroom rises to its feet one by one, pale window light",
"A courtroom of townsfolk on their feet with shame crawling up their necks, standing not from goodness but because she now holds the water and the land, guilty faces, pale daylight",
"Louisa — A woman frozen in mourning black in a front pew stares straight ahead as the girl she shamed walks past to inherit everything, stricken and rigid, cold light",
"Louisa, Clara — A stricken woman's mouth opens with a soft salvaging word as a gray clad girl draws even and halts beside the pew, tense charged air, cold window light",
"Clara — Close up of a young woman looking calmly down at the woman who shamed her a thousand cold nights, no hatred in her face, pale light",
"A hushed courtroom holding its breath, faces half hoping for a blow that will not come, tense pale daylight",
"Clara, Louisa — A plain gray clad young woman speaks quietly and evenly to a rigid woman in mourning black, I stopped hating you in that barn, mercy without warmth, cold window light",
"Clara — A young woman states her terms plainly and unbowed, the land and the water now hers to say over, treated fair, quiet strength, daylight",
"Clara, Judge Harlan — A gray clad young woman takes an old judge's offered hand and turns to face the whole town, lifted and steady, pale daylight",
# ---- ACT 3: what she did with it ----
"A vast dry summer range under open sky that a bitter heir could have shut the water from and let the cattle die, the cruel path not taken, harsh bright light",
"Clara — A young woman signs no cruelty into a fair lease at a plain desk, keeping the Sennetts on at a fair rent, quiet resolve, lamplight",
"A stream of water running free to cattle across a wide range, mercy shown to good neighbors and bad alike, cold bright daylight",
"Clara — A young woman throws open the big warm kitchen of a grand ranch house on a hard winter night, welcoming the poor in from the dark, golden firelight",
"Clara — A young woman stands at a door welcoming orphans widows and drifters into a warm lamplit kitchen out of the cold, generous and glowing, warm light",
"Clara — A young woman sets a long table heaped with hot food for the hungry of the valley, hands folded in welcome, nobody sent to the barn, warm golden firelight",
"Clara, Levi — A young woman and a kind young ranch hand stand together in a warm doorway the following spring, tender and easy, golden light",
"Levi, Clara — A young ranch hand looks at a young woman with the plain love of a man who saw her worth before there was a dime attached, warm soft light",
"Cordelia — A quiet pine hillside grave under tall pines with fresh flowers, an old widow at rest, remembered at last as a person not a purse, soft daylight",
"Clara — A young woman kneels at a pine hillside grave reading aloud from an old book, wind coming down off the mountains, soft golden light",
# ---- CLOSING ----
"A warm lamplit ranch kitchen with a long full table and every seat taken by the once forgotten, a tale still told by firelight, golden glow",
"Clara — A young woman stands thoughtful in a lantern lit barn doorway remembering, be careful who you send to eat in the dark, warm and cold light",
"Cordelia, Clara — A frail old widow's softened face remembered in firelight beside a young woman warming her shaking hands, one honest soul found at last, warm glow",
"A single glowing oil lantern on a plank table with dust drifting in its light against a dark background, the story closing, warm intimate glow",
]

# Every prompt ends old-west even pasted alone. Fixes modern-setting renders.
ANCHOR = ", 1880s American Old West frontier, period-accurate frontier clothing and props, no modern objects, no contemporary clothing"

def run():
    rows = list(csv.DictReader(open("Story09-Scenes.csv")))
    assert len(rows) == len(PROMPTS), f"{len(rows)} scenes vs {len(PROMPTS)} prompts"
    stamped = [p + ANCHOR for p in PROMPTS]
    out = []
    for r, p in zip(rows, stamped):
        out.append(f"SCENE {int(r['scene']):03d} | {r['in']}-{r['out']} ({float(r['dur_s']):.1f}s)\n{p}")
    open("Story09-HiredGirl-ShotList.txt", "w").write("\n\n\n".join(out) + "\n")
    open("Story09-HiredGirl-Prompts-Only.txt", "w").write("\n\n\n".join(stamped) + "\n")
    durs = [float(r["dur_s"]) for r in rows]
    print(f"{len(rows)} scenes | {sum(durs)/60:.1f} min | {sum(durs):.0f}s (VO 22:57 = 1377s) | "
          f"shortest {min(durs):.1f}s longest {max(durs):.1f}s")

run()
