# -*- coding: utf-8 -*-
# Story 11 "The Mute Witness" — VO-synced shot list builder.
# Pairs authored prompts with scene_calculator.py timecodes (narration-only, 24:20 = 1460s).
# Ingredients: Verna | Hattie | Jasper | Owen | Sheriff Fenn | (circuit judge, generic).
# SENSITIVE: murder shown ONLY as a shadowed struggle through a lit window, no gore, no
# strangling detail. Slate stays TEXT-FREE (chalk marks unreadable / angled away). No graphic
# hanging (use courtroom/justice framing). Names inline. No mid-body em-dashes.
import csv

PROMPTS = [
# ---- COLD OPEN (suspense; person first) ----
"Verna — A frightened young woman of nineteen crouches in the dark behind a rain barrel with both hands pressed hard over her own mouth, terror in her wide eyes, a lantern-lit kitchen window glowing yellow thirty feet beyond, cold blue night",
"Verna — Close on a young woman's horrified eyes over her own clamped hands as a shadowed struggle plays out behind a distant lantern-lit window, silent dread, cold night",
"Verna — A young woman in a plain gray dress presses herself small and silent in the dark, unable to cry out, a hand over her mouth, anguished, cold blue night",
"A single warm lantern-lit farmhouse window at night seen from a dark yard, a man's shadow straightening up inside, the ordinary house of a terrible moment, cold night",
"Jasper, Verna — Through a lit window a well-dressed man's silhouette turns and his cold eyes meet a girl's frightened face in the dark glass, a charged deadly gap between them, cold night",
"Verna — A young woman's stricken face lit by distant lantern glow, a killer who thinks her harmless, a schoolteacher's help still to come, cold blue night",
"Verna — A silent watchful young woman stands unnoticed at the edge of a frontier street while townsfolk pass without a glance, invisible, flat gray daylight",
"Verna — A thin nineteen year old laundry girl with quick dark eyes and rough red hands stirs a great steaming iron wash kettle behind a poor lean-to, working before dawn, cold gray light",
"Verna — A young laundry girl works unseen at the edge of a room while townsfolk talk over her as if she were furniture, invisible and silent, dim indoor light",
"Townsfolk gossiping and shaking their heads pityingly toward a silent girl who stands apart, careless cruelty, flat daylight",
"Verna — Close on a young woman's sharp intelligent dark eyes taking in everything around her, a brilliant mind behind a silent face, soft light",
"Verna — A watchful girl notices a furtive card game and a man slipping toward a widow's door at dusk, seeing all the town's secrets, blue evening",
"Verna, Hattie — A silent young woman and a kind old widow together, the one soul who treats her as whole, warm lamplight",
"Hattie — A sharp kind old widow near seventy in a plain dark dress stands before a tidy little house with a good stone well, weathered warm face, soft daylight",
"Hattie, Verna — An old widow sits a silent girl down at a real table and feeds her, talking warmly as if expecting an answer, warm lamplit kitchen",
"Hattie, Verna — An old widow butters bread and speaks earnestly to a young girl across a plain table, telling her not to let the town make her small, warm kitchen light",
"Hattie, Verna — An old widow grips a young girl's hand with sudden earnestness by lamplight, a warning and a love, warm glow",
"A tidy little house with a reliable stone well under a wide dry country sky, water that never fails, the thing men will kill for, gold daylight",
"Jasper — A handsome charming man in a neat dark coat rides past a modest homestead with cold appraising eyes, quietly coveting the land, flat daylight",
"Jasper — A charming weathered man laughs easily with townsfolk on a boardwalk, remembering names and shaking hands, a trusted mask, warm daylight",
"Jasper — A respectable man in a dark coat stands among church deacons and the sheriff, everyone's friend, flat daylight",
"Jasper — Close on a charming man's face as the warmth drops for an instant to show cold snake eyes beneath, dim light",
"Jasper, Hattie — A smooth man stands on a tidy porch pressing an old widow to sell, her arms folded and face stubborn, tense daylight",
"Jasper — A charming man rides out alone toward a distant house on a cold October night, dark intent under an easy face, cold blue dusk",
"Verna — A young woman crosses a dark farmyard carrying a basket of folded washing toward a lit kitchen door, unaware, cold blue night",
"Jasper, Verna — A man's shadow inside a lit window and a frozen girl in the dark yard, the killer and the one silent witness, a deadly charged gap, cold night",
"Verna — A young woman drops a basket of washing and runs across a black field toward distant town lights, terror and a soundless scream, cold night",
"Verna — A young woman runs through the dark at the edge of town, a man's shadow pounding behind her, breathless silent flight, cold blue night",
"Verna — A young woman pounds desperately with both fists on a lamplit sheriff's office door in the dark, no voice to call out, cold night",
"Sheriff Fenn — A tired heavy frontier lawman in shirtsleeves opens his office door by lamplight, baffled and half awake, dim glow",
"Sheriff Fenn, Verna — A frantic wordless girl grabs a tired sheriff's sleeve and points wildly into the dark, unable to speak, dim lamplight",
"Jasper, Sheriff Fenn — A calm well-dressed man strolls up out of the night tipping his hat to a sheriff, all easy concern, cold lamplit street",
"Jasper — A charming man spreads his hands and speaks smoothly to a sheriff, dismissing the girl as having spells, a liar's easy mask, cold night",
"Sheriff Fenn, Verna, Jasper — A tired sheriff looks between a frantic silent girl and a calm respectable man, and believes the man who can talk, dim lamplight",
"A tidy little house in cold morning light with men gathered grimly at the cellar door, a body being tended, a staged accident, pale gray light",
"Verna — A young woman in a farmyard points frantically at a cellar and clutches her own throat, trying with her whole body to say murder, ignored, gray daylight",
"Townsfolk carry a shrouded still form from a house while a silent girl gestures desperately and is pitied but unheard, gray morning",
"Jasper, Verna — At a graveside a charming man lays a false kind hand on a silent girl's shoulder before the whole town, hat over his heart, gray daylight",
"Jasper, Verna — A man leans close to a girl's ear with a cold whisper while his face stays gentle for the crowd, a private threat, gray graveside light",
"Jasper — A charming man touches his hat to a graveside crowd and walks away a free man, untouched, gray daylight",
"Verna — A silent grieving young woman stands alone by a fresh grave, helpless and unheard, carrying an unbearable secret, gray light",
"Owen — A slight bookish young Eastern schoolteacher with round spectacles and ink-stained fingers arrives at a small frontier schoolhouse, mild and out of place, pale daylight",
"Owen — Close on a mild intelligent young schoolteacher watching quietly through his spectacles, a man who pays attention, soft light",
"Owen, Verna — A schoolteacher notices a silent laundry girl's sharp eyes following every word in a room, seeing the mind behind the silence, dim indoor light",
"Verna — A grieving young woman with a face full of unbearable secret, not the grief of a simpleton, dim light",
"Owen, Verna — A young schoolteacher sits on an upturned crate across from a silent girl in a poor laundry, gentle and earnest, warm lamplight",
"Owen, Verna — A schoolteacher sets a small slate and a piece of chalk on a crate between himself and a silent girl, offering a key, warm lamplight",
"Verna — A young woman stares at a blank slate and chalk like a starving woman staring at bread, desperate hope, warm lamplight",
"Owen, Verna — A schoolteacher guides a silent girl's hand over a slate by lamplight, teaching first letters, tender patient focus, warm glow (chalk marks unreadable)",
"Verna — A young woman bent over a slate by lamplight practicing letters with fierce hunger, night after night, warm glow (marks not legible)",
"Owen — A schoolteacher watches in quiet astonishment as a silent girl devours language faster than any child, dawning realization, warm lamplight",
"Owen — Close on a schoolteacher's face lit with grave understanding, knowing the words locked in her will one day burn the town down, warm light",
"Verna — A young woman studies a slate deep in the night while a distant lit town sleeps, the killer free out there, cold and warm light mixed",
"Jasper — A charming man on a boardwalk watches the lit laundry window from across a dark street, the first touch of fear on his face, cold night",
"Jasper — Close on a charming man's uneasy face, his whole safety built on the girl having no voice, now uncertain, dim light",
"Jasper, Owen — A smiling man stands in a schoolhouse doorway making easy small talk with a mild schoolteacher, a veiled warning, pale daylight",
"Jasper, Owen — Two men face each other across a schoolroom, one warmly smiling and one calmly cleaning his spectacles, a charged quiet duel, pale light",
"Owen — A mild schoolteacher speaks evenly, unbothered, saying the girl will soon have a great deal to say, quiet steel, pale daylight",
"Jasper, Owen — The pleasant mask slips on a charming man's face for an instant as two men understand the game exactly, tense pale light",
"Jasper — A charming man's face gone cold and decided in the dark, resolving to solve a problem he has solved once before, dim menace, cold light",
"Jasper — A man rakes glowing coals from beneath a great iron kettle against a dry wooden wall in a dark laundry, quiet arson, low ember glow",
"A poor lean-to and laundry at night with the first orange flames catching a dry wall, a sleeping figure within unaware, ember and cold night",
"Verna — A young woman jolts awake at the smell of smoke and slips out a window into the dark as flames take the lean-to behind her, then runs through the night, cold night and orange fire",
"Owen, Verna — A schoolteacher opens his door to a shaking girl lit by a distant orange fire, she already reaching past him for slate and chalk, warm doorway light and orange glow",
"Owen, Verna — A young woman writes fast on a slate on a doorstep by firelight, red hands shaking, the words she has carried for months, warm and orange light (marks angled away, unreadable)",
"Owen — Close on a schoolteacher's mild face going hard as flint reading a slate by firelight, grim resolve, warm and orange light",
"Owen, Verna — A schoolteacher speaks urgently and steadily to a girl on his firelit doorstep, we do not hide, a plan forming, warm orange light",
"Owen, Verna — A schoolteacher looks gently at a frightened girl and asks if she can be brave a little longer, and she nods, warm lamplight",
"Owen — Close on a schoolteacher's intent face as a beautiful plan settles, one that turns on the killer's own good name, warm light",
"A frontier church filling with townsfolk for a Sunday meeting about land and water, tense gathering, pale window light",
"Jasper — A charming man sits front and center in a crowded church, smiling, ready to claim a well at last, pale daylight",
"A stern outside circuit judge in a dark coat sits unnoticed in a back pew of a crowded church, untouched by the town's charm, pale light",
"Owen — A mild schoolteacher stands up in the middle of a crowded church and speaks out in a clear carrying voice, every head turning, pale light",
"Owen, Verna — A schoolteacher walks a silent girl to the front of a crowded church before all the townsfolk, steadying her, pale daylight",
"Owen, Verna — A schoolteacher sets a large blank slate on an easel at the front of the church and puts a chalk in a silent girl's hand, pale daylight (slate blank to camera)",
"Jasper — A charming man laughs loudest of all in a church pew, spreading his hands to the mocking crowd, pale daylight",
"Verna — A silent young woman stands at the front of a hushed church and begins to write boldly on a great slate, the laughter dying letter by letter, fierce and not simple, pale window light (marks not legible)",
"Verna — A young woman wipes a slate and writes again with a steady unshaking hand, the church gone dead silent around her, pale light (writing angled away, unreadable)",
"A stunned silent church of townsfolk reading a written accusation climb across a slate, faces going pale, pale window light (slate angled away)",
"Verna, Jasper — A silent young woman at a slate lifts her chalk and points it like an accusing finger straight across the church at a charging pale-faced man, a charged gap, pale daylight",
"Jasper — A charming man's mask cracks clean off into shouting fury in a church, ugly and cornered, half the room flinching, pale light",
"Jasper — A furious man shouts and points, denouncing the girl as a half-wit, the charm gone, pale daylight",
"The stern circuit judge rises slowly in the back of a hushed church and commands the room to turn, grave authority, pale light",
"The circuit judge speaks firmly, offering to question the silent girl and see whether she knows what only a witness could, pale daylight",
"Verna — A silent young woman answers questions on her slate with calm precise detail, eleven years of watching become a blade, pale light (marks unreadable)",
"Verna, Jasper — A young woman's chalk indicates a fresh red scratch on the back of a charming man's right hand, a telling mark, pale light",
"Men crouch in a leaf-strewn farmyard finding drag marks pressed in the dirt exactly where the girl said, damning evidence, pale daylight",
"A dropped basket of washing found caught in a creek behind a house, recovered exactly as the girl wrote, pale outdoor light",
"A church full of townsfolk staring at a silent young woman as though seeing her for the very first time, dawning awe and shame, pale light",
"Jasper — A cornered man bolts for a church door, panic breaking through his charm, pale daylight",
"Jasper — Men rise to their feet blocking a cornered man, the red scratch on his hand plain to all, his lie collapsing, pale daylight",
"The stern circuit judge stands grave in a courtroom of justice, a killer's six-year lie brought down at last, pale window light (no gallows, no violence)",
"Hattie, Verna — A remembered kind old widow's face over a warm table, the will that quietly left everything to the silent girl she loved, warm glow",
"Verna — A once-poor young woman stands as a woman of property before a tidy house and good stone well now her own, quiet dignity, gold daylight",
"Owen, Verna — A schoolteacher and a young woman stand together two years on, tender and easy, married, warm soft light",
"Verna — A young woman gently teaches letters to overlooked silent and slow souls gathered at a schoolhouse, giving them a way to speak, warm light (slates blank)",
"Verna — A young woman writes on a schoolhouse slate for a visitor, calm and wise, no longer unheard, warm daylight (marks not legible)",
"Verna — Close on a young woman's calm knowing face, she who looked for years while no one looked back, warm light",
"A frontier town at golden dusk where a tale is still told by firelight, the laundry girl and the smiling man both gotten backwards, warm long shadows",
"Verna — A quiet dignified young woman on the edge of golden light, a whole ocean behind her watchful eyes, warm glow",
"Verna — A young woman looks steadily toward a silent overlooked soul on the edge of the light, an invitation to look closer, soft warm light",
"A single glowing oil lantern on a plank table with dust drifting in its light against a dark background, the story closing, warm intimate glow",
]

ANCHOR = ", 1880s American Old West frontier, period-accurate frontier clothing and props, no modern objects, no contemporary clothing"

def run():
    rows = list(csv.DictReader(open("Story11-Scenes.csv")))
    assert len(rows) == len(PROMPTS), f"{len(rows)} scenes vs {len(PROMPTS)} prompts"
    stamped = [p + ANCHOR for p in PROMPTS]
    out = []
    for r, p in zip(rows, stamped):
        out.append(f"SCENE {int(r['scene']):03d} | {r['in']}-{r['out']} ({float(r['dur_s']):.1f}s)\n{p}")
    open("Story11-MuteWitness-ShotList.txt", "w").write("\n\n\n".join(out) + "\n")
    open("Story11-MuteWitness-Prompts-Only.txt", "w").write("\n\n\n".join(stamped) + "\n")
    durs = [float(r["dur_s"]) for r in rows]
    print(f"{len(rows)} scenes | {sum(durs)/60:.1f} min | {sum(durs):.0f}s (VO 24:20 = 1460s) | "
          f"shortest {min(durs):.1f}s longest {max(durs):.1f}s")

run()
