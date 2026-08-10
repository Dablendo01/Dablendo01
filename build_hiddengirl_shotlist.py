# -*- coding: utf-8 -*-
# Story 16 "The Hidden Girl" — VO-synced shot list builder.
# Pairs authored prompts with scene_calculator.py timecodes (narration-only, 35:24 = 2124s).
# Ingredients: Nell (17 + young-11 variant) | Isaac | Augusta | Horace | Lavinia | Old Man Weld
#   | county lawyer. Deeds/ledgers/papers TEXT-FREE. Young Nell shown WITHOUT peril (grief/graves
# only, no child-distress pairing). Names inline. No mid-body em-dashes. 143 prompts, 1:1.
import csv

PROMPTS = [
"Nell — A plain girl of seventeen in a too-small cast-off dress kneels mucking out stalls in a dim barn, hidden away, cold morning light",  # 1
"Augusta — A cold controlling frontier matron gives a dismissive order the night before, not troubling to lower her voice, dim parlor light",  # 2
"A fine frontier house filling with ribbon and cake as county carriages arrive for a grand dance, bright daylight",  # 3
"Nell — A seventeen year old girl in a dress two sizes too small hauls a fork of manure in a dark barn, hidden like a family shame, dim light",  # 4
"Nell — A worn plain girl labors in a barn, six years worked from dark to dark and thanked for none of it, dim light",  # 5
"Nell — Close on a tired plain girl's face in a hand-me-down dress, the family secret, kept small, a hidden truth behind her eyes, dim light",  # 6
"A fine house on good black bottomland with carriages in the yard, all of it secretly belonging to the girl in the barn, bright daylight",  # 7
"A country road leading toward a frontier town, a reckoning riding up it, gray daylight",  # 8
"Nell, Isaac — A girl forking hay in a lantern-lit barn and a rancher's silhouette at the door, the meeting to come, warm and cold light",  # 9
"A good man surveys the best black bottomland in a valley with a sharp eye, Nell's father in memory, warm daylight",  # 10
"Young Nell — A cherished small girl of a prospering family loved and taught in a fine parlor, a warm remembered life, warm light",  # 11
"Young Nell — A small girl plays a little at a parlor organ, a warm childhood seen from far away, golden light",  # 12
"Two fresh graves with plain markers on a bleak hillside and a small orphaned girl standing before them, grief, gray light",  # 13
"Young Nell — A small girl of eleven alone in a fine empty house, an heiress far too young to know or guard it, dim light",  # 14
"Horace, Augusta — A poor-relation couple arrive in black with long faces and false grief, come to take in an orphan, gray daylight",  # 15
"Horace, Augusta — A couple promise before neighbors to raise the orphan and manage her property, respectable and grasping, daylight",  # 16
"A judge grants a man guardianship of an orphan and her estate, papers on the bench, pale courtroom light (text not legible)",  # 17
"Horace, Augusta — A poor-relation couple installed in a fine house, beginning quietly to make an orphan girl disappear, dim light",  # 18
"Augusta, young Nell — A matron calls a small girl poor lamb before company, a false sweetness, dim parlor light",  # 19
"Young Nell — A small girl watches her dead father's good books crated up and carried off to be sold, a quiet grief, dim light",  # 20
"Lavinia, young Nell — A lavish birthday party fills a parlor for one girl while another stands overlooked in the doorway, cruel contrast, warm party light",  # 21
"Young Nell — A small girl slowly learning to think of herself as a burden and a charity case, diminished, dim light",  # 22
"Young Nell — A small girl neglected and increasingly cold-shouldered in a fine house, patient cruelty, dim light",  # 23
"Nell, Lavinia — A girl put in cast-off dresses while a younger cousin is handed her good clothes, unfair, dim light",  # 24
"Nell — A girl of about fourteen scrubbing floors, doing the labor of a hired girl in a house full of servants, dim light",  # 25
"Nell — A girl scrubbing while unseen the money that is hers flows out to the family, a bitter contrast, dim light",  # 26
"Horace — A guardian spends a ward's money as his own, buying fine carriages, greed dressed as respectability, daylight",  # 27
"A lavish cake and ribbons in a bright parlor set against a girl hauling manure in a dark barn, the stolen fortune, split light",  # 28
"Augusta — Close on a matron's fearful calculating face, dreading the day the ward comes of age or marries, dim light",  # 29
"Horace, Augusta — A couple fear a husband who might ask a lawyer for an accounting no smooth word could survive, dim study light",  # 30
"Horace, Augusta — A couple resolve on one iron rule, that no man must ever court their hidden ward, cold intent, dim light",  # 31
"Nell — A plain girl kept working and hidden away from the eyes of any young man who might see her worth, dim barn light",  # 32
"Augusta, Nell — A matron orders her niece hidden in the barn on the morning of the great dance, cold command, dim light",  # 33
"Nell — Close on a plain girl's face with a stubborn unkilled spark behind her eyes, mind and spirit intact, dim light",  # 34
"Nell — A girl reads a hidden battered book of poems by stub-candlelight in a barn loft after the house sleeps, warm small glow",  # 35
"Nell — A girl talks softly to the horses and the barn cats, her only company, warm dim barn light",  # 36
"Nell — A girl sings quietly to herself in a barn when sure no one can hear, an old song, a stubborn ember, warm dim light",  # 37
"Nell — Close on a plain girl's face refusing, deep down, to believe she is nothing, unkillable spirit, dim light",  # 38
"Nell — A girl in a barn at dusk, her hidden spirit about to get out around the edges, warm-cold light",  # 39
"Lavinia — A pretty accomplished empty young woman of sixteen, raised to be exactly what her mother wished, bright parlor light",  # 40
"Lavinia — A young woman decked in the finest dress set up in a parlor like a prize at a fair, warm party light",  # 41
"Isaac — A quiet solid young rancher of about twenty-two, only son of the county's biggest cattleman, warm daylight",  # 42
"Augusta, Isaac — A scheming matron eyes a fine young rancher for her daughter, a match to set her beyond questions, warm room light",  # 43
"Augusta, Lavinia — A matron maneuvers her daughter into a young rancher's path at a dance, calculating, warm party light",  # 44
"Isaac — A watchful young rancher unimpressed by the prettiest ribbon, quietly taking the room's measure, warm light",  # 45
"Isaac — A bored young rancher endures a parade of accomplished daughters marched past him at a dance, weary, warm party light",  # 46
"Lavinia, Isaac — A young woman plays a parlor organ and laughs on cue, pleasant and empty, a young rancher unmoved, warm light",  # 47
"Isaac — A young rancher makes an excuse about his horse and slips out the back of the house for air, dim evening light",  # 48
"Isaac — A young rancher walks through a yard at dusk past a barn and stops, hearing a girl singing, blue evening light",  # 49
"Isaac — A young rancher stands still in the dusk yard listening to a low true song from the barn, blue evening",  # 50
"Nell, Isaac — A young rancher looks in a barn door at a smudged girl in a too-small dress forking hay by lantern light with a cat at her ankles, singing, warm lantern glow",  # 51
"Isaac — A young rancher struck still in a barn doorway, the tiresome day falling away before something real, warm light",  # 52
"Isaac — Close on a young rancher's kind open face, neither sneering nor condescending, warm lantern light",  # 53
"Nell, Isaac — A young rancher leans easy on a barn doorpost and speaks warmly to a startled girl, honest and unguarded, warm glow",  # 54
"Nell — A smudged girl startled and gone scarlet, then quick-tongued, retorting to the young man in the doorway, warm light",  # 55
"Nell, Isaac — A young rancher laughs a real laugh and sits himself down on a hay bale to stay, easy and delighted, warm lantern glow",  # 56
"Nell, Isaac — A girl and a young rancher talk on hay bales in a lantern-lit barn, easy and alive, warm glow",  # 57
"Nell, Isaac — A girl recites a remembered line of poetry as a young rancher leans forward, captivated, warm lantern light",  # 58
"Nell, Isaac — A girl recites poetry in lantern light while a young rancher watches her face, thinking her beautiful, dust and all, warm glow",  # 59
"Nell, Isaac — A girl makes a young rancher laugh with a dry wicked wit, describing the dance from the outside, warm light",  # 60
"Isaac — A young rancher presses a hand to his mouth to keep from laughing aloud in the yard, delighted, warm dim light",  # 61
"Nell, Isaac — A girl and a young rancher in real conversation, she quicker and kinder and more alive than any of the ladies, warm glow",  # 62
"Isaac — A young rancher puzzled that such a girl mucks stalls while an empty cousin is paraded in the parlor, thoughtful, warm light",  # 63
"Isaac — Close on a young rancher's thoughtful face, a thing that makes no sense to him yet, warm light",  # 64
"Augusta — A matron at a window goes the color of ash seeing the young rancher in the lit barn doorway with the hidden girl, horror, warm-cold light",  # 65
"Augusta, Isaac — A matron sweeps out with false sweetness and steers a young rancher back toward the house, a light lying laugh, warm evening light",  # 66
"Isaac — A young rancher glances back once over his shoulder at the barn as he is led away, a matron's fear like a stone behind him, evening light",  # 67
"Augusta, Nell — A matron in a dark barn at night berates a girl coldly, no sweetness left, cruel, dim lantern light",  # 68
"Augusta, Nell — A matron tells a girl she is plain and low and nothing, that the rancher only amused himself, cruelty, dim light",  # 69
"Augusta, Nell — A matron threatens to put a girl out on the road if she looks at the young man again, cold menace, dim light",  # 70
"Augusta — A matron resolves to keep a girl locked to the house until the marriage scheme is safely settled, cold command, dim light",  # 71
"Nell — A girl lies awake crying in a cold barn loft, changed by one hour of being treated as a whole person, dim light",  # 72
"Nell — Close on a girl's resolute face in the dark, refusing to be sorry for the one good hour that was hers, dim light",  # 73
"Isaac — A young rancher rides home at night unable to stop thinking of the girl in the barn, resolve forming, cold blue night",  # 74
"Isaac — A young rancher at his family's ranch, quietly resolved to find out the truth, morning light",  # 75
"Isaac, Old Man Weld — A young rancher asks his weathered old father about the hired girl at the Bracken place, warm parlor light",  # 76
"Old Man Weld, Isaac — An old cattleman tells his son about the Ainsley family and the orphaned heiress, the son listening hard, warm light",  # 77
"Old Man Weld, Isaac — An old man says that girl owns the ground the Brackens stand on, the truth dawning on a young rancher, warm light",  # 78
"Isaac — A young rancher sits very still as the whole ugly shape of a hidden theft comes clear to him, hardening, warm light",  # 79
"Isaac — Close on a young rancher's face going hard and cold and purposeful, quiet fury, warm light",  # 80
"Isaac, county lawyer — A young rancher lays the matter before a sharp honest county-seat lawyer, grave, lamplit office",  # 81
"County lawyer — A lawyer's eyes narrow, a guardian's management being a matter of record, a duty and a pleasure to examine, lamplight",  # 82
"County lawyer — A lawyer pores over bank records and a property deed in a dead father's name, building a case, lamplit desk (text not legible)",  # 83
"County lawyer — A lawyer assembles the paper trail of a drained estate over three weeks, methodical, lamplight (text not legible)",  # 84
"Nell — A girl kept watched and confined to the house, no errand allowed past the road, unaware of any rescue, dim light",  # 85
"Augusta, Nell — A matron's eyes follow a girl with a new frightened hatred the girl cannot account for, tense dim light",  # 86
"Nell — A confined girl bewildered, thinking herself punished only for being noticed, dim light",  # 87
"Nell — A girl at a window making herself stop hoping, telling herself the young man forgot her, sad dim light",  # 88
"Isaac, Augusta — A young rancher forces a pleasant smile at a matron and a bland cousin, hiding a cold fury, tense warm light",  # 89
"Isaac — A young rancher holds himself in check, knowing one careless word could tip off a thief who might run or hide the money, tense light",  # 90
"Isaac, county lawyer — A young rancher waits, thinking of the locked-away girl, as a lawyer looks up from his papers with news, lamplit office",  # 91
"Isaac, county lawyer — A lawyer counsels a young rancher to choose a public moment for a crime past wriggling out of, and the rancher chooses, lamplight",  # 92
"A great county harvest social gathering at a lantern-strung barn, the public stage set, warm evening light",  # 93
"Horace, Augusta, Lavinia — The Bracken family arrive at the social in their finest, the daughter riding high, warm party light",  # 94
"Nell, Augusta — A plain girl in cast-offs kept at the food tables while a triumphant matron looks on, the trap unknowing, warm party light",  # 95
"Augusta — A smug matron parading her generosity in bringing the poor niece, her single greatest mistake, warm light",  # 96
"Isaac — A young rancher stands on a low fiddlers' platform at a lantern-strung social and asks for quiet, and gets it, warm evening light",  # 97
"Augusta, Lavinia — A matron's heart leaps, sure the offer is coming, and she puts a hand to her daughter's back to push her forward, warm light",  # 98
"Isaac — A young rancher addresses the county gravely of a wrong done in plain sight for six years, warm platform light",  # 99
"County lawyer, Augusta — A lawyer steps up beside the rancher with a leather folio as a matron's leaping heart turns to ice, warm-cold light",  # 100
"County lawyer — A lawyer tells the whole county in a flat unarguable voice of the Ainsley fortune and the guardianship, warm gathering light (text not legible)",  # 101
"County lawyer — A lawyer lays out dollar by dollar the drained estate and the heiress made a hidden servant, damning, warm light",  # 102
"County lawyer, Nell — A lawyer gestures toward the plain girl by the food tables, naming the house and the dresses as hers, the crowd turning, warm light",  # 103
"Augusta, county lawyer — A matron surges forward to cry slander as a lawyer calmly holds up the actual deed, a charged clash, warm light (deed text not legible)",  # 104
"Horace — A blustering man sweating and shrinking as the merciless record is read, a coward exposed, warm light",  # 105
"Nell — The whole county turns as one to look at a plain girl frozen by the food tables, hearing the truth of herself for the first time, warm gathering light",  # 106
"Nell — Close on a plain girl as the truth breaks over her like a wall she leaned on was never there, stunned, warm light",  # 107
"Nell — A girl standing stunned as six years of being told she was nothing collapses into a lie, warm light",  # 108
"Nell — A girl realizing the people who made her a drudge were thieves who robbed a child, dawning, warm light",  # 109
"Nell — A girl in a borrowed too-small dress learning the charity was a lie and all of it was always hers, warm light",  # 110
"Nell — A girl's whole stolen life turning right side up in a single breath, no poor relation but a robbed heiress, warm light",  # 111
"Nell, Isaac — A girl finds a young rancher's face in the crowd and he gives her one steady reassuring nod, a charged gap, warm light",  # 112
"Nell — A girl held down six years slowly standing up straight, dignity rising, warm gathering light",  # 113
"Nell — A girl reaches up calm as still water and unties the mean cheap ribbon her aunt made her wear, warm light",  # 114
"Nell — A cheap ribbon falling to the ground as a girl stands tall in her too-small dress, chin level and eyes clear, warm light",  # 115
"Nell — A girl more a lady in a torn dress than her cousin in stolen silk, the county truly seeing her at last, warm light",  # 116
"Horace, Augusta — A blustering man and a sweetening matron availing nothing against the merciless papers, exposed thieves, warm-cold light",  # 117
"Horace — A guardian arrested for the theft of his ward's estate, fine things bound for the auction block, cold daylight",  # 118
"Augusta — A stripped matron facing her own kind of prison, no jail but ruin, cold gray light",  # 119
"Augusta — A humbled matron living poor and scorned in the town she once lorded over, cold daylight",  # 120
"Lavinia — A humbled young woman stripped of her stolen dresses, learning too late to be ordinary, plain gray light",  # 121
"Nell — A girl reclaiming the fine house and good land that were stolen from her, quiet triumph, warm daylight",  # 122
"Nell — A girl at seventeen restored from a barn drudge to the mistress of the black bottomland, transformed, golden light",  # 123
"Nell — A young woman restored to exactly the life she was born to before the Brackens ever came, warm light",  # 124
"Nell — Close on a young woman's kind unpoisoned face, come through cruelty without the poison in her, warm light",  # 125
"Nell, Lavinia — A young woman faces the empty cousin who never once was kind, a choice before her, warm light",  # 126
"Nell, Lavinia — A young woman offers her humbled cousin a place and a fair wage and a chance to become something real, unexpected mercy, warm light",  # 127
"Lavinia — A humbled young woman at a crossroads, uncertain whether she can grow decent at last, gray light",  # 128
"Isaac — A young rancher who did not come courting the moment the girl was rich, honorable, warm daylight",  # 129
"Nell, Isaac — A young rancher remembering the barn, having wanted the girl when she was a hired hand with nothing, warm memory light",  # 130
"Isaac — A young rancher who moved heaven and the courts not for a fortune but to free a girl he could not stop thinking of, resolute, warm light",  # 131
"Isaac — A young rancher waits a decent while so none could say he came for the money, honorable restraint, warm daylight",  # 132
"Nell, Isaac — A young rancher comes courting honest and hat in hand up the road to the restored house, and a young woman says yes, warm daylight",  # 133
"Nell, Isaac — A young woman and a young rancher married on the black bottomland her father chose, in the restored house, warm golden light",  # 134
"Nell — A young woman risen again into the life meant for her, mistress of her father's place, warm light",  # 135
"Nell — A young woman notices an overlooked servant girl kept down, an eye the comfortable never have, warm daylight",  # 136
"Nell — A young woman quietly and firmly putting a stop to a hidden cruelty wherever she finds it, resolute, warm light",  # 137
"Nell — A hidden kept-down girl arriving up the road to find a young woman's door standing open, warm daylight",  # 138
"Nell — A young woman welcomes a hidden girl in, the kindness of one who knew what it was to be kept small, warm glow",  # 139
"Nell — A tale remembered in the valley, the heiress hidden in the barn found singing by lantern light, warm firelight",  # 140
"A barn at dusk where the world buries its treasures in cast-offs and hides them out back, a quiet reproach, warm-cold light",  # 141
"A figure pausing at a barn at dusk with the ears to catch a hidden song and the decency to stop and see, warm evening light",  # 142
"A single glowing oil lantern on a plank table with dust drifting in its light against a dark background, the story closing, warm intimate glow",  # 143
]

ANCHOR = ", 1880s American Old West frontier, period-accurate frontier clothing and props, no modern objects, no contemporary clothing"

def run():
    rows = list(csv.DictReader(open("Story16-Scenes.csv")))
    assert len(rows) == len(PROMPTS), f"{len(rows)} scenes vs {len(PROMPTS)} prompts"
    stamped = [p + ANCHOR for p in PROMPTS]
    out = []
    for r, p in zip(rows, stamped):
        out.append(f"SCENE {int(r['scene']):03d} | {r['in']}-{r['out']} ({float(r['dur_s']):.1f}s)\n{p}")
    open("Story16-HiddenGirl-ShotList.txt", "w").write("\n\n\n".join(out) + "\n")
    open("Story16-HiddenGirl-Prompts-Only.txt", "w").write("\n\n\n".join(stamped) + "\n")
    durs = [float(r["dur_s"]) for r in rows]
    print(f"{len(rows)} scenes | {sum(durs)/60:.1f} min | {sum(durs):.0f}s (VO 35:24 = 2124s) | "
          f"shortest {min(durs):.1f}s longest {max(durs):.1f}s")

run()
