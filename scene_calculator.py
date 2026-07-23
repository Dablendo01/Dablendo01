#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LANTERN & DUST — SCENE CALCULATOR
Turns a voiceover into a timed scene sheet so each image/animation lasts exactly
as long as the narration it covers. No manual nudging to match the VO.

TWO MODES
  A) SRT MODE (most accurate): you export captions from your VO tool as .srt
     (ElevenLabs, CapCut, Descript, Whisper, or YouTube auto-captions all do this).
     python3 scene_calculator.py captions.srt
     -> uses the REAL spoken timestamps. Zero drift.

  B) SCRIPT MODE (no captions yet): plain script text + the total VO runtime.
     python3 scene_calculator.py script.txt --seconds 2308
     -> estimates timing from words-per-second. Good, but SRT is exact.

OPTIONS
  --target 10     aim for ~10s per scene (default 10; try 8 for faster cutting)
  --min 5         never cut a scene shorter than this
  --max 16        force a cut if a scene runs longer than this
  --out scenes.csv  also write a CSV you can open in a spreadsheet

OUTPUT (per scene): number | IN timecode | OUT | duration | word count |
the exact narration it covers | a blank IMAGE PROMPT line to fill.
Each scene = one image. Its duration is already correct for the VO.
"""

import sys, re, csv, argparse

SENT_END = re.compile(r'[.!?]["”’)]*\s*$')

def tc(seconds):
    ms = int(round((seconds - int(seconds)) * 1000))
    s = int(seconds) % 60
    m = (int(seconds) // 60) % 60
    h = int(seconds) // 3600
    return f"{h:01d}:{m:02d}:{s:02d}.{ms:03d}"

def parse_srt_time(t):
    t = t.strip().replace(',', '.')
    h, m, rest = t.split(':')
    s = float(rest)
    return int(h)*3600 + int(m)*60 + s

def read_srt(path):
    """Return list of cues: (start_s, end_s, text)."""
    blocks = re.split(r'\n\s*\n', open(path, encoding='utf-8').read().strip())
    cues = []
    for b in blocks:
        lines = [l for l in b.splitlines() if l.strip()]
        if len(lines) < 2:
            continue
        timeline = next((l for l in lines if '-->' in l), None)
        if not timeline:
            continue
        a, bb = timeline.split('-->')
        text = ' '.join(l for l in lines if '-->' not in l and not l.strip().isdigit())
        cues.append((parse_srt_time(a), parse_srt_time(bb), text.strip()))
    return cues

def scenes_from_srt(cues, target, mn, mx):
    scenes = []
    cur_start = None
    cur_text = []
    cur_end = None
    for (a, b, txt) in cues:
        if cur_start is None:
            cur_start = a
        cur_text.append(txt)
        cur_end = b
        dur = cur_end - cur_start
        joined = ' '.join(cur_text)
        at_sentence = bool(SENT_END.search(joined))
        if (dur >= target and at_sentence) or dur >= mx:
            scenes.append((cur_start, cur_end, joined))
            cur_start, cur_text, cur_end = None, [], None
    if cur_text:
        scenes.append((cur_start, cur_end, ' '.join(cur_text)))
    # merge any runt shorter than mn into the previous scene
    merged = []
    for sc in scenes:
        if merged and (sc[1] - sc[0]) < mn:
            ps, pe, pt = merged[-1]
            merged[-1] = (ps, sc[1], (pt + ' ' + sc[2]).strip())
        else:
            merged.append(list(sc))
    return [tuple(x) for x in merged]

def split_sentences(text):
    # collapse whitespace, keep [SECTION]/(re-hook) markers out of the timing
    text = re.sub(r'\[[^\]]*\]', ' ', text)
    text = re.sub(r'\((?:re-hook)[^)]*\)', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    parts = re.split(r'(?<=[.!?])\s+', text)
    return [p.strip() for p in parts if p.strip()]

def scenes_from_script(path, total_seconds, target, mn, mx):
    text = open(path, encoding='utf-8').read()
    sents = split_sentences(text)
    total_words = sum(len(s.split()) for s in sents)
    wps = total_words / total_seconds if total_seconds else 2.9
    scenes = []
    t = 0.0
    cur_words = 0
    cur_text = []
    cur_start = 0.0
    for s in sents:
        w = len(s.split())
        cur_text.append(s)
        cur_words += w
        dur = cur_words / wps
        if dur >= target or dur >= mx:
            end = cur_start + dur
            scenes.append((cur_start, end, ' '.join(cur_text)))
            cur_start = end
            cur_words = 0
            cur_text = []
    if cur_text:
        scenes.append((cur_start, total_seconds, ' '.join(cur_text)))
    return scenes, wps, total_words

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('input')
    ap.add_argument('--seconds', type=float, help='total VO runtime (SCRIPT mode only)')
    ap.add_argument('--target', type=float, default=10.0)
    ap.add_argument('--min', type=float, default=5.0, dest='mn')
    ap.add_argument('--max', type=float, default=16.0, dest='mx')
    ap.add_argument('--out', help='write CSV here')
    args = ap.parse_args()

    if args.input.lower().endswith('.srt'):
        cues = read_srt(args.input)
        scenes = scenes_from_srt(cues, args.target, args.mn, args.mx)
        note = f"SRT mode — exact timing from {len(cues)} caption cues"
    else:
        if not args.seconds:
            print("SCRIPT mode needs --seconds (total VO runtime). "
                  "e.g. --seconds 2308 for 38:28")
            sys.exit(1)
        scenes, wps, tw = scenes_from_script(args.input, args.seconds, args.target, args.mn, args.mx)
        note = f"SCRIPT mode — estimated at {wps:.2f} words/sec ({tw} words / {args.seconds:.0f}s)"

    rows = []
    print(f"\n{note}")
    print(f"{len(scenes)} scenes  |  target ~{args.target:.0f}s each\n")
    for i, (a, b, txt) in enumerate(scenes, 1):
        dur = b - a
        wc = len(txt.split())
        print(f"SCENE {i:03d}  {tc(a)} -> {tc(b)}  ({dur:4.1f}s, {wc}w)")
        print(f"  VO: {txt}")
        print(f"  IMAGE PROMPT: ______________________________________________\n")
        rows.append({"scene": i, "in": tc(a), "out": tc(b),
                     "dur_s": round(dur, 2), "words": wc, "narration": txt})

    if args.out:
        with open(args.out, 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=["scene","in","out","dur_s","words","narration","image_prompt"])
            w.writeheader()
            for r in rows:
                r["image_prompt"] = ""
                w.writerow(r)
        print(f"CSV written: {args.out}  (add an image_prompt per row, one image per scene)")

    durs = [b - a for a, b, _ in scenes]
    print(f"\nTotals: {len(scenes)} images | {sum(durs)/60:.1f} min covered | "
          f"shortest {min(durs):.1f}s, longest {max(durs):.1f}s")

if __name__ == "__main__":
    main()
