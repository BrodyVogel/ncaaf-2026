#!/usr/bin/env python3
"""Build a readable per-team qualitative primer from the grading dossiers
(snapshots/<Team>/unit_dossiers.md). Two dossier formats exist (G5 has an
'## As-played' header + '— planned N' unit headers; P4 puts the summary in the
intro paragraph and uses descriptive unit headers). We extract a clean team
'read' summary and a one-line note per unit, stripping the percentile shorthand.
Override teams get their manual-override rationale prepended. Output feeds the
Rating Explainer tab so the owner can see WHY a rating lands where it does."""
import re, json, os, glob, csv

UNITS = ['QB', 'RB', 'WRTE', 'OL', 'DL', 'LB', 'DB', 'ST']


def _clean(s):
    return re.sub(r'\s+', ' ', s).strip(' .,—-|;')


def _strip_tokens(s):
    """Remove the internal percentile shorthand (CODE 79.5 p70 / CODE p70 / p70 / |)."""
    s = s.replace('|', ' ')
    s = re.sub(r'\*+', '', s)
    s = re.sub(r'\b[A-Z][A-Z/]{1,5}\b\s*\d*\.?\d*\s*p\d+', '', s)   # CODE num pNN
    s = re.sub(r'\bp\d+\b', '', s)                                    # stray pNN
    s = re.sub(r'\b(PF|PA)\b', '', s)
    s = re.sub(r'\s*\)', ')', s)
    s = re.sub(r'\(\s*[,;:/—-]+\s*', '(', s)        # strip stranded punctuation left inside parens
    s = re.sub(r'[/;,]\s*\)', ')', s)
    s = re.sub(r'\(\s*\)', '', s)                    # drop now-empty parens
    s = re.sub(r'\s+([)/;,.])', r'\1', s)
    s = re.sub(r'\(\s+', '(', s)
    return _clean(s)


def _summary(txt):
    if '## As-played' in txt:                       # G5 format: prose in the As-played section
        m = re.search(r'## As-played[^\n]*\n(.*?)\n##', txt, re.S)
        body = m.group(1) if m else ''
        if 'Read:' in body:
            body = body.split('Read:', 1)[1]
        return _strip_tokens(body)
    # P4 format: prose intro before the first '## <unit>'
    head = txt.split('\n## ', 1)[0]
    head = head.split('\n', 1)[1] if '\n' in head else head          # drop the '# Team' title
    head = re.sub(r'Compiled[^.]*\.\s*', '', head)                    # drop the compile stamp
    head = re.split(r'2025 as-played|^Proxy|\nProxy|PROXY NOTES', head)[0]
    head = re.sub(r'[A-Z0-9]{2,3} offsets;.*$', '', head)            # drop trailing method note
    return _strip_tokens(head)


def _unit_notes(txt):
    notes = {}
    for u in UNITS:
        m = re.search(r'##\s*' + u + r'\b[^\n]*\n(.*?)(?=\n##\s|\Z)', txt, re.S)
        if not m:
            continue
        seg = m.group(1)
        room = re.search(r'Room:\s*(.*?)(?:\.\s|\n\n|Mechanical:|Bracket:)', seg, re.S)
        if room:
            note = room.group(1)
        else:                                                        # first bullet or first sentence
            b = re.search(r'^\s*[-*]\s*(.+?)(?:\.\s|\n\n)', seg, re.S | re.M)
            note = b.group(1) if b else seg.split('. ')[0]
        notes[u] = _strip_tokens(note)[:220]
    return notes


def _dossier_for(name, dir_by_team):
    d = dir_by_team.get(name)
    return os.path.join(d, 'unit_dossiers.md') if d else None


def build_primers(root='.'):
    dir_by_team = {}
    for d in glob.glob(os.path.join(root, 'snapshots/*/')):
        mp = os.path.join(d, 'META.json')
        if os.path.exists(mp):
            try:
                dir_by_team[json.load(open(mp))['team']] = d
            except Exception:
                pass
    ovr = {}
    op = os.path.join(root, 'data/manual_overrides_2026.csv')
    if os.path.exists(op):
        for r in csv.DictReader(open(op)):
            ovr[r['team']] = r
    primers = {}
    for name, d in dir_by_team.items():
        path = os.path.join(d, 'unit_dossiers.md')
        if not os.path.exists(path):
            continue
        txt = open(path).read()
        summ = _summary(txt)
        if len(summ) < 25:                                           # fallback: first unit note
            un = _unit_notes(txt)
            summ = next(iter(un.values()), '')
        p = {'summary': summ, 'units': _unit_notes(txt)}
        if name in ovr:                                              # override rationale takes precedence
            o = ovr[name]
            p['override'] = 'Rating manually set to %s%s. %s' % (
                ('+' if float(o['rating']) >= 0 else ''), o['rating'], o['note'])
        primers[name] = p
    return primers


if __name__ == '__main__':
    ps = build_primers()
    print('built %d primers' % len(ps))
    empty = [t for t, p in ps.items() if len(p['summary']) < 25]
    print('short/empty summaries: %d %s' % (len(empty), empty[:10]))
    for t in ['Ohio State', 'Wisconsin', 'Tulane', 'Alabama', 'North Dakota State', 'Boise State']:
        if t in ps:
            print('\n[%s] %s' % (t, ps[t]['summary'][:340]))
            if 'override' in ps[t]:
                print('   OVERRIDE: %s' % ps[t]['override'][:200])
