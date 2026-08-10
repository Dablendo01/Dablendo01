# -*- coding: utf-8 -*-
# Story 14 "The Veiled Widow / Secret Benefactor" — VO-synced shot list builder.
# Pairs authored prompts with scene_calculator.py timecodes (narration-only, 16:25 = 985s).
# Ingredients: Estelle (veiled variant + unveiled) | Millicent | Ada | Hollis.
# Envelopes/notes/deeds/bills TEXT-FREE. Ada's baby only held/loved (minors filter). Names
# inline. No mid-body em-dashes. 67 prompts, one per scene, 1:1 with the narration.
import csv

PROMPTS = [
"Estelle veiled — A woman all in mourning black with a heavy dark veil drawn fully over her face stands alone and mysterious on a frontier street, face unseen, cold spring daylight",  # 1
"Estelle veiled — A veiled woman in mourning black sits silent in the back pew of a church, keeping to herself, leaving before anyone can speak, pale window light",  # 2
"Townsfolk on a boardwalk whisper cruel stories about a distant veiled figure, a mystery they resent, flat daylight",  # 3
"Millicent — A righteous iron-cornered church matron of about 50 holds court among townswomen, declaring the veiled widow an affront, prim daylight",  # 4
"Estelle veiled — A veiled woman moves alone through a cold suspicious town as folk turn their faces away, shunned, gray daylight",  # 5
"Estelle veiled — A veiled figure in black stands still against a wintry town, a reckoning coming, ominous cold light",  # 6
"Estelle veiled — A veiled woman watches the town quietly from behind the black, unknowable, pale light",  # 7
"Estelle veiled — Close on a heavy dark mourning veil hiding a face entirely, a hidden grief behind it, dim light",  # 8
"Estelle — A memory: a dignified woman in fine eastern mourning stands alone in a grand shadowed parlor, great wealth and great grief together, dim rich light",  # 9
"Estelle — A grieving wealthy widow surrounded by grasping suitors and relations reaching for her, a prize and not a person, cold formal light",  # 10
"Estelle veiled — A woman in mourning black boards a westbound train alone, leaving a city and every grasping soul behind, veiling herself, gray daylight",  # 11
"Estelle veiled — A veiled woman in black arrives quietly in a small frontier town, hoping to be no one, pale daylight",  # 12
"Estelle veiled — A veiled woman stands unnoticed at the edge of a street, truly seeing the town's poor for the first time, soft light",  # 13
"Estelle veiled, Ada — A veiled woman watches a poor young mother count her few coins at a mercantile counter, unseen and moved, dim store light",  # 14
"Estelle veiled — A veiled woman takes in the hunger and fear the comfortable townsfolk walk past, quiet resolve forming, gray daylight",  # 15
"Ada — A poor young mother of about twenty with a sick baby on her hip stands worried in a mercantile, a note she cannot pay weighing on her, dim light",  # 16
"Ada — A poor young mother sets a small bottle of medicine back on a shelf because she cannot afford both it and the flour, heartbreaking, dim store light",  # 17
"Estelle veiled, Hollis — A veiled woman speaks quietly with a careful frontier banker in a lamplit bank office, taking him into her confidence, warm dim light",  # 18
"An envelope of money left quietly on a plank table where a poor woman will find it, an anonymous gift, warm light (no readable text)",  # 19
"A load of winter wood delivered to a poor doorstep by a driver who will not say who sent it, a ghostly kindness, gray daylight",  # 20
"Townsfolk on a street speculating eagerly about the secret angel of the town, guessing at prosperous men, animated daylight",  # 21
"Estelle veiled — A veiled woman passes townsfolk who sneer at her, never guessing the hated stranger is their secret angel, flat daylight",  # 22
"Millicent, Estelle veiled — A righteous matron sneers at the passing veiled widow while secretly wondering about the mysterious benefactor, bitter irony, flat daylight",  # 23
"Millicent — A respectable church matron presides as a small tyrant among the townswomen, cold and certain, prim daylight",  # 24
"Millicent — Close on a bored righteous matron's face, her own malice mistaken for principle, cold light",  # 25
"Millicent — A matron organizes the cold shoulders at a church social, ensuring the veiled widow is quietly shut out, tense warm room",  # 26
"Estelle veiled — A veiled woman sits alone and weary in a small rented room above a shop, the veil having bought loneliness not peace, dim lamplight",  # 27
"Estelle veiled — A veiled woman at a dark window at night, wondering why she goes on giving to a town that would spit on her, lonely lamplight",  # 28
"Millicent, Estelle veiled — A matron plants herself in the path of a veiled woman in a churchyard, cornering her before the whole congregation, cold daylight",  # 29
"Millicent — A matron demands loudly that the veiled widow show her face, the churchyard crowd watching, righteous daylight",  # 30
"Millicent, Estelle veiled — A matron issues her ultimatum across a charged gap to a still veiled woman, lift your veil or leave, the churchyard gone silent, pale light",  # 31
"Estelle veiled — A veiled woman stands motionless as every eye in the churchyard fixes on her, a matron flushed with triumph nearby, tense pale light",  # 32
"Estelle — A grieving woman reaches up with both black-gloved hands and lifts her heavy dark veil back from her face, the pivotal moment, pale daylight",  # 33
"Estelle — An unveiled woman of middle years, no scar and no monster, only a handsome tired dignified face marked by grief, calm clear steady eyes, pale light",  # 34
"Estelle — Close on an ordinary kind grieving unveiled face, plainly no monster but a lady, the crowd beginning to realize, pale light",  # 35
"A churchyard of townsfolk staring thrown and confused at an ordinary unveiled woman, their six-month story evaporating, pale cold light",  # 36
"Estelle — An unveiled grieving woman speaks in a low steady cultured voice that carries across a silent churchyard, dignified, pale light",  # 37
"Estelle, Millicent — An unveiled woman looks directly at the matron and names herself the secret benefactor, a charged gap between them, pale daylight",  # 38
"Estelle — An unveiled woman lists her hidden gifts to a dawning churchyard, the miracle explained, pale window light",  # 39
"Millicent, Estelle — A matron stricken pale as the unveiled woman reveals she is the secret angel who kept half the town in their homes, a hush like falling snow, pale light",  # 40
"Ada — A poor young mother pushes forward through the churchyard crowd with her baby on her hip and tears streaming, staring at the unveiled woman, pale daylight",  # 41
"Ada, Estelle — A young mother whispers it was you to the unveiled woman, tearful recognition breaking over her, pale light",  # 42
"Ada, Estelle — A young mother walks up and throws an arm around the unveiled widow and weeps into her shoulder before the whole town, warm amid the cold crowd",  # 43
"Estelle — An unveiled woman who had grieved alone and asked nothing is overcome, her arms going around the weeping young mother, warm light",  # 44
"Ada, Estelle — An unveiled widow holds a poor young mother like a drowning woman, a frozen grief finally breaking open, warm light in a cold churchyard",  # 45
"A churchyard of townsfolk watching in dawning understanding, the size of what they have done settling on their faces, pale light",  # 46
"Townsfolk, comfortable and careless, made to see they let a tyrant tell them who to sneer at, shame dawning, pale daylight",  # 47
"Stricken townsfolk with hands over mouths, the widow Foster and the Colton family understanding they were helped by the one they scorned, pale light",  # 48
"A crowd bowing under a cold tide of shame, the particular shame of being cruel to a secret benefactor, pale cold light",  # 49
"Millicent — A matron stands alone in the middle of the churchyard as the whole town turns from the ugliness she led, isolated, pale light",  # 50
"Millicent — A matron alone under the silent total judgment of a turning crowd, the loudest thing of her small tyrannical life, pale daylight",  # 51
"Estelle — An unveiled woman stands with a choice before her, free to leave the town that wronged her, pale light",  # 52
"Estelle — An unveiled woman addresses the churchyard, her veil folded back for good, I came here to be no one, dignified, pale daylight",  # 53
"Estelle — An unveiled woman speaks her truth plainly, that money makes you a target and grief makes you invisible, steady and clear, pale light",  # 54
"Estelle — An unveiled woman resolute, choosing to be the somebody she chooses rather than the town's villain, pale window light",  # 55
"Estelle — An unveiled woman openly present in the town at last, done with secret giving that let cruelty go easy, resolve, daylight",  # 56
"Estelle — A woman helps frightened families openly at a bank counter, looking each one in the eye as she saves their home, warm daylight (papers not legible)",  # 57
"Estelle, Ada — An unveiled woman takes a young mother and her baby into a warm home, a family grief made and kindness bound, warm light",  # 58
"Estelle, Ada — An unveiled woman who lost her own child holds a young mother's baby, a daughter and grandchild found at the far end of mourning, warm glow",  # 59
"Estelle, Millicent — An unveiled woman openly pays a humbled matron's note and looks her in the eye with quiet mercy, warm daylight (papers not legible)",  # 60
"Estelle — An unveiled woman remembered by the town, a mirror held up rather than a monster, warm light",  # 61
"A small frontier town at dusk, bored tongues and quick judgments, an old needful truth, warm long shadows",  # 62
"Estelle veiled — A veiled figure in black, the stranger a town made its villain, unknowable, a quiet reproach, dim light",  # 63
"Estelle — A dark veil half lifted from a kind grieving face, how quick we are to hate what we cannot see, soft light",  # 64
"A gentle figure walking over to a veiled stranger with a kind word, choosing to wait and see the face, warm daylight",  # 65
"Estelle — Close on an unveiled woman's kind grieving face, the mercy that looks back from behind the black, warm light",  # 66
"A single glowing oil lantern on a plank table with dust drifting in its light against a dark background, the story closing, warm intimate glow",  # 67
]

ANCHOR = ", 1880s American Old West frontier, period-accurate frontier clothing and props, no modern objects, no contemporary clothing"

def run():
    rows = list(csv.DictReader(open("Story14-Scenes.csv")))
    assert len(rows) == len(PROMPTS), f"{len(rows)} scenes vs {len(PROMPTS)} prompts"
    stamped = [p + ANCHOR for p in PROMPTS]
    out = []
    for r, p in zip(rows, stamped):
        out.append(f"SCENE {int(r['scene']):03d} | {r['in']}-{r['out']} ({float(r['dur_s']):.1f}s)\n{p}")
    open("Story14-VeiledWidow-ShotList.txt", "w").write("\n\n\n".join(out) + "\n")
    open("Story14-VeiledWidow-Prompts-Only.txt", "w").write("\n\n\n".join(stamped) + "\n")
    durs = [float(r["dur_s"]) for r in rows]
    print(f"{len(rows)} scenes | {sum(durs)/60:.1f} min | {sum(durs):.0f}s (VO 16:25 = 985s) | "
          f"shortest {min(durs):.1f}s longest {max(durs):.1f}s")

run()
