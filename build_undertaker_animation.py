# -*- coding: utf-8 -*-
# The Undertaker's Kindness — animation prompts for scenes 1-100.
# Each still from the shot list is the START FRAME; the line below is MOTION ONLY.
# Render each clip to its scene duration (from the timed shot list) so the
# animated stretch stays synced to the 41:31 VO. Slow, small motion. No em-dashes.
import csv

MOTIONS = [
"The black coach rolls slowly forward, wheels turning and kicking up drifting dust, townsfolk slowly turning their heads to watch, a loose shutter swaying",
"The lawyer slowly sets his hat on the bar and lifts his gaze to the room, speaking, lamplight flickering, rough men shifting and going still",
"The lawyer's eyes move slowly across the room from face to face, a measured breath, coat unmoving, lamplight wavering on the walls",
"The lawyer speaks slowly with one deliberate question, a slow blink behind his spectacles, warm lamplight flickering, tense faces blurred behind",
"The frail old man shuffles slowly forward into the cold street, his patched coat hem stirring in the wind, shoulders trembling, dust drifting",
"The old man shuffles slowly along the boardwalk while townsfolk turn and cross away, cold glances, coats and skirts moving in the breeze",
"The big undertaker stands still in the lamplit doorway breathing slowly, lamplight flickering on his weathered face, dust motes drifting, coffins dim behind",
"The undertaker pushes the plane slowly along the pine board, thin shavings curling and falling, lamplight flickering, steady careful strokes",
"The undertaker slowly draws a comb through the still old man's white hair, gentle tender motion, lamplight flickering softly, quiet reverence",
"The undertaker slowly lifts and turns a shovel of earth on the hilltop, golden evening light glowing, grass swaying, the far creek shimmering",
"The undertaker stands still at the graveside, hat over his chest, head slowly bowing, wind stirring grass and coat, dusk light softly fading",
"The undertaker slowly tips the last worn coins into his open palm and turns them, lamplight glinting, a quiet resolute breath",
"The undertaker taps the chisel slowly with the mallet, tiny granite chips flaking away, lamplight flickering, absorbed steady rhythm",
"The frail old man stands still, a slow breath lifting his thin shoulders, a flicker of hidden weight passing through his eyes, weak light shifting",
"The dying old man walks slowly along the lonely road at dusk, bent and failing, coat stirring, dust drifting, empty country behind him",
"Lamplight flickers slowly over the folded will and wax seal on the dark desk, a faint curl of shadow moving, the pen catching light",
"The well-fed man rises smoothly to his feet, an oily smile slowly spreading, hooking his thumbs in his silver-buttoned vest, lamplight glinting",
"The undertaker slowly works the shovel on the hill in evening light, unaware, steady humble motion, grass swaying, a crowd tiny far below",
"Warm lamplight flickers slowly over the closed brass pocket watch on the workbench, a faint gleam shifting, sawdust motes drifting",
"The undertaker slowly sets a steaming plate before the ragged old man, steam curling up, the old man lifting his eyes, warm lamplight flickering",
"The lawyer slowly raises the closed brass watch between two fingers, the sweating man's eyes fixing on it, lamplight flickering, the crowd leaning in",
"The lonely undertaker slowly lifts a spoon over his supper at the workbench, one lamp flickering, steam rising faintly, sawdust motes drifting",
"The undertaker breathes slowly, his large careful hands shifting on the bench, a slow patient blink, lamplight flickering warm on his face",
"The black wagon rolls slowly down the dusty street, mothers slowly drawing children close and turning away, dust drifting, wary faces",
"The undertaker steps slowly into the saloon and men fall quiet and drift from the bar, lamplight flickering, a cold hush settling",
"A slow drift across the frayed rusty coat on the big man's shoulders, threads stirring faintly, gray daylight shifting, poverty in the weave",
"The single lit window glows steady in the dark street, lamplight flickering within, faint dust moving on the wind, the building still and isolated",
"The young woman laughs softly and turns, honey hair stirring, warm golden light glowing, her freckled face bright with joy, a memory shimmer",
"The young woman lies still with eyes closed, candlelight flickering softly over her peaceful face, a thin curtain breathing, quiet and dim",
"The big man pushes the plane slowly along the board at midnight, shoulders bent, a tear falling into the sawdust, lamplight flickering low",
"The undertaker stands utterly still at the graveside in gray rain, hat off, head bowed, rain streaming down, coat heavy and dripping",
"Rain runs slowly down the undertaker's grieving face as his jaw sets and his eyes harden with quiet resolve, storm light shifting",
"The undertaker stands hat-off at a plain grave reading slowly into the dusk wind, grass swaying, long shadows stretching, reverent stillness",
"The undertaker slowly smooths clean linen into the pine coffin with careful hands, lamplight flickering, a gentle respectful motion",
"The undertaker slowly turns a few thin coins in his palm over the bench, worry deepening on his face, lamplight flickering, an empty tin",
"The frail old man shuffles slowly into the raw purple dusk, wind biting his patched coat, one far lamp glowing, dust drifting past",
"The well-fed man stands on the hotel porch, thumbs in his vest, eyes slowly appraising, a faint cold smile, silver buttons glinting",
"The town boss slowly turns surveying the main street he owns, cane in hand, a smug proprietary breath, dust drifting, silver buttons gleaming",
"The well-fed man gestures grandly to the small crowd, mouth moving in a speech, self-satisfied, coats stirring in the breeze, warm daylight",
"The smooth confident face holds a thin cold smile, a slow blink of utter indifference, silver buttons catching the light, still and chilling",
"The speculator's cold gaze fixes slowly across the street, contempt tightening his mouth, a ledger shifting under his arm, daylight steady",
"The well-fed man slowly gestures possessively across the hilltop slope, a greedy smile, coat and grass stirring in the dusk wind",
"The town boss leans slowly toward the seated council men, mouth moving, cane tapping the floor, lamplight flickering, scheming",
"The well-fed man slowly taps his silver cane on the boardwalk delivering a cold line, thin smile, evening light shifting, coat stirring",
"The small bent old man stands shaking in the raw wind, patched coat flapping, dust streaming past, purple dusk deepening, frail and still",
"The frail old man climbs slowly up the hotel steps gripping the rail, road-dust dripping, breath labored, hopeful, dusk light fading",
"The ragged old man stands humbly on the lit porch, hat turning slowly in his hands, mouth moving in a quiet plea, small in the doorway",
"The frail old man's lined face speaks softly, a slow hopeful blink, watery eyes catching porch lamplight, dignity in the stillness",
"The well-fed man's eyes travel slowly down the ragged old man head to toe with cold appraisal, a faint sneer forming, porch light steady",
"The town boss speaks down slowly with false sorrowful courtesy, a smooth cold smile, the old man taking it quietly, porch lamplight flickering",
"The well-fed man slowly gestures away toward the dark street, sending the old man off, cold and final, lamplight flickering on silver buttons",
"The frail old man slowly turns and shuffles down the steps into the dark, shoulders bowing lower, coat stirring, receiving it like weather",
"The old man warms his trembling hands at the stove as rough regulars smirk and mutter, firelight flickering, an unwelcome hush",
"The frail old man is slowly waved back from the barn doorway by a nervous stable hand, a lantern swaying, cold night, gently refused",
"The frail old man sits huddled on the dark steps, breath clouding, the one warm window glowing above him, night wind stirring dust",
"The undertaker slowly opens his lamplit door into the dark and stops, seeing the huddled old man, concern rising, warm light spilling out",
"The frail old man slowly lifts his face with a dry weary smile, a faint breath of a laugh, warm lamplight flickering, no self-pity",
"The old man on the doorstep slowly gestures toward the coffin-filled workshop with dark humor, the big man listening in the doorway, lamplight",
"The undertaker slowly steps aside and gestures a welcome into the warm firelight, a kind nod, night behind him, lamplight flickering",
"The undertaker slowly takes the stumbling old man by the arm and eases him over the threshold, tender and careful, warm light washing over them",
"The undertaker slowly sets a bowl of stew before the blanket-wrapped old man by the glowing stove, steam curling, warm gold light flickering",
"The undertaker and the old man sit quietly by the glowing stove, slow breaths, firelight flickering over two weary faces, gentle stillness",
"The old man talks slowly by the stove, firelight on his lined face, a wry flicker crossing his features, holding something back, warm glow",
"The undertaker's tired face slowly softens toward a faint smile as he listens by the stove, firelight flickering, something waking in him",
"The two weary men talk slowly by the low stove, slow nods, shared grief in the quiet, dim gold firelight wavering over their faces",
"The undertaker speaks slowly and haltingly by the stove, grief and relief crossing his face, firelight flickering, a long-held sorrow spoken",
"The frail old man listens intently by firelight, a slow understanding blink, saying nothing, deep quiet in his watery eyes, warm glow",
"The old man stares slowly into the stove fire, an old loss shadowing his face, a faint breath, firelight flickering, quiet grief",
"The old man's firelit face speaks a hard word slowly, a flicker of a former life behind his eyes, a weary regretful blink, warm glow",
"The frail old man's shaking hands slowly cradle the worn brass watch in firelight, a thumb brushing it, tender and sad, warm glow flickering",
"The old man slowly presses the brass watch into the undertaker's reluctant hands, firelight glinting off it, insistent and grave",
"The old man's earnest lined face speaks slowly pressing the gift, a wry grave look, firelight flickering, pale eyes fixed and certain",
"The undertaker slowly turns the small brass watch in his hand, moved and uncertain, firelight glinting, the old man's shape beside him",
"The undertaker slowly slips the brass watch into his vest pocket, a solemn breath, not opening it, lamplight flickering, quiet respect",
"Warm lamplight flickers slowly over the brass watch tucked in the worn vest pocket, a faint gleam shifting, shallow soft focus",
"The undertaker sits slowly leaning in by the cot, holding the failing old man's hand, the lamp flickering, a night vigil, still and tender",
"The undertaker slowly steadies the burning lamp by the sickbed, holding the frail hand in the dark, a slow breath, a warm pool of light",
"The frail old man's peaceful face on the pillow slowly turns up with love and gratitude, a soft blink, lamplight flickering, a last clear moment",
"The dying old man speaks his last words slowly from the pillow, gripping a hand, serene and certain, lamplight flickering, eyes softly shining",
"The frail thin hand slowly tightens around the big careful hand on the blanket, lamplight flickering, a quiet bond in the final moment",
"The frail old man lies slowly still with eyes closed, the low lamp flickering beside him, the big man's bowed head near, quiet and peaceful",
"The well-fed man slowly smirks and taps his cane in the saloon, mouth moving on a cruel joke, men laughing around him, harsh light flickering",
"The town boss holds forth slowly at the bar with a mocking grin, cane gesturing, the amused crowd shifting, warm harsh light wavering",
"The smug well-fed face slowly delivers a cruel line, a thin cold smile spreading, silver buttons glinting, contemptuous and still",
"The undertaker slowly runs his hand along the clear pine boards and lifts one, resolute and unhurried, lamplight flickering, ignoring the town",
"The undertaker pushes the plane slowly along the fine board, shavings curling and falling, lamplight flickering, careful loving strokes",
"The seamstress draws the needle slowly through the white linen, steady deft hands, lamplight flickering, a calm quiet warmth in her face",
"The undertaker speaks slowly across the bolt of white cloth, the seamstress lifting her steady eyes to his, a bond forming, warm light flickering",
"The seamstress slowly folds the white linen and presses it into the big man's hands, shaking her head gently, refusing pay, warm steady kindness",
"The undertaker slowly buttons his good coat onto the peaceful still old man, careful reverent hands, lamplight flickering softly",
"The undertaker slowly lowers the brass watch toward the coffin then draws it back, keeping his promise, a solemn breath, lamplight flickering",
"The undertaker slowly lifts a shovel of earth on the golden hilltop corner, the far creek shimmering, grass swaying, steady quiet labor",
"The well-fed man stands slowly gesturing down at the grave-hole scolding, the undertaker digging on unbothered, dusk wind stirring coats",
"The undertaker slowly leans on his shovel chest-deep in the grave and speaks plainly upward, quiet unshakable dignity, dusk light shifting",
"The undertaker slowly climbs up out of the finished grave, dirt on his hands, a resolute breath, the fresh mound and hill glowing behind",
"The undertaker slowly tips the last coins from the tin into his palm, all he has, a quiet resolute breath, lamplight glinting on them",
"Warm lamplight flickers slowly over the tipped tin and few worn coins on the bench, a faint gleam, poverty laid bare, soft focus",
"Hard daylight shifts slowly over the rough granite slab leaning in the dusty mason's yard, dust drifting, tools still, unclaimed and waiting",
"The undertaker slowly heaves the heavy granite slab onto the wagon bed, straining, determined, dust rising, wide frontier behind him",
"The undertaker slowly raises and taps the mallet on the chisel against the granite, tiny chips flaking, lamplight flickering, absorbed careful work",
]

def run():
    rows = list(csv.DictReader(open("UndertakersKindness-Scenes.csv")))[:100]
    assert len(rows) == len(MOTIONS) == 100, f"{len(rows)} scenes vs {len(MOTIONS)} motions"
    out = []
    for r, m in zip(rows, MOTIONS):
        sc = int(r["scene"]); a = r["in"]; b = r["out"]; d = float(r["dur_s"])
        out.append(f"SCENE {sc:03d} | {a}-{b} ({d:.1f}s)\n{m}")
    header = ("LANTERN & DUST — THE UNDERTAKER'S KINDNESS — ANIMATION PROMPTS (scenes 1-100)\n"
              "Each shot-list still is the START FRAME; the line below is MOTION ONLY.\n"
              "Render each clip to its scene duration. Slow, small motion. No em-dashes.\n"
              "Protect faces (Abel, Amos, Price, Adair, Cora, Lila) — regenerate warped takes.\n"
              "Deaths are peaceful-sleep framing; the stable hand is brave, never in peril.\n\n\n")
    open("UndertakersKindness-Animation-1-100.txt", "w").write(header + "\n\n\n".join(out) + "\n")
    durs = [float(r["dur_s"]) for r in rows]
    print(f"{len(rows)} animation prompts | covers {sum(durs)/60:.1f} min (to scene 100) | "
          f"shortest {min(durs):.1f}s longest {max(durs):.1f}s")

run()
