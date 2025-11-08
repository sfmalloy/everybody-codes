from io import TextIOWrapper
from lib.quest import app
from itertools import cycle, permutations


@app.parser(quest=7)
def parse(file: TextIOWrapper):
    ipt = file.readlines()
    segments = {}
    mp = {'+': 1, '-': -1, '=': 0}
    for line in ipt:
        key, vals = line.strip().split(':')
        vals = vals.split(',')
        segments[key] = [mp[v] for v in vals]
    return segments


@app.solver(quest=7, part=1)
def part1(segments: dict[str, list[str]]):
    lst = []
    for k, v in segments.items():
        tot = 0
        val = 10
        for s, _ in zip(cycle(v), range(10)):
            val += s
            tot += val
        lst.append((k, tot))
    return ''.join(k[0] for k in sorted(lst, key=lambda p: -p[1]))


@app.solver(quest=7, part=2)
def part2(segments: dict[str, list[str]]):
    def check_plan(plan: str, track):
        it = cycle(plan)
        tot = 0
        val = 10
        # for _ in range(len(track)*10):
        for s, t in zip(it, track * 10):
            if t == '-':
                s = -1
            elif t == '+':
                s = 1
            val += s
            tot += val
        return tot

    track = """S-=++=-==++=++=-=+=-=+=+=--=-=++=-==++=-+=-=+=-=+=+=++=-+==++=++=-=-=--
-                                                                     -
=                                                                     =
+                                                                     +
=                                                                     +
+                                                                     =
=                                                                     =
-                                                                     -
--==++++==+=+++-=+=-=+=-+-=+-=+-=+=-=+=--=+++=++=+++==++==--=+=++==+++-"""
    lst = []
    for k, v in segments.items():
        lst.append((k, check_plan(v, track)))
    return ''.join(k[0] for k in sorted(lst, key=lambda p: -p[1]))


@app.solver(quest=7, part=3)
def part3(segments: dict[str, list[str]]):
    def check_plan(plan: list[int], track: list[str]):
        tot = 0
        val = 10
        taken = []
        for s, t in zip(cycle(plan), track):
            if t == '-':
                s = -1
            elif t == '+':
                s = 1
            val += s
            taken.append(s)
            tot += val
        return tot

    def get_track(track_map: str):
        mp = [line for line in track_map.splitlines()]
        r = 0
        c = 1
        track = []
        prev = (0, 0)
        while mp[r][c] != 'S':
            track.append(mp[r][c])
            old = (r, c)
            if r + 1 < len(mp) and mp[r + 1][c] != ' ' and (r + 1, c) != prev:
                r += 1
            elif c + 1 < len(mp[r]) and mp[r][c + 1] != ' ' and (r, c + 1) != prev:
                c += 1
            elif r - 1 >= 0 and mp[r - 1][c] != ' ' and (r - 1, c) != prev:
                r -= 1
            elif c - 1 >= 0 and mp[r][c - 1] != ' ' and (r, c - 1) != prev:
                c -= 1
            prev = old
        track.append('S')
        return track

    track = get_track("""S+= +=-== +=++=     =+=+=--=    =-= ++=     +=-  =+=++=-+==+ =++=-=-=--
- + +   + =   =     =      =   == = - -     - =  =         =-=        -
= + + +-- =-= ==-==-= --++ +  == == = +     - =  =    ==++=    =++=-=++
+ + + =     +         =  + + == == ++ =     = =  ==   =   = =++=       
= = + + +== +==     =++ == =+=  =  +  +==-=++ =   =++ --= + =          
+ ==- = + =   = =+= =   =       ++--          +     =   = = =--= ==++==
=     ==- ==+-- = = = ++= +=--      ==+ ==--= +--+=-= ==- ==   =+=    =
-               = = = =   +  +  ==+ = = +   =        ++    =          -
-               = + + =   +  -  = + = = +   =        +     =          -
--==++++==+=+++-= =-= =-+-=  =+-= =-= =--   +=++=+++==     -=+=++==+++-""")

    plan = [1, 1, 1, 1, 1, -1, -1, -1, 0, 0, 0]
    track = track * len(plan)
    rival = check_plan(segments['A'], track)
    count = 0
    seen = set()
    for v in permutations(plan):
        if v in seen:
            continue
        seen.add(v)
        tot = check_plan(v, track)
        if tot > rival:
            count += 1
    return count
