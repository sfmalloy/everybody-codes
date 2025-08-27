from itertools import cycle, permutations
from pathlib import Path

def solve(segments: dict[str, list[str]]):
    with open(Path('quest07') / 'track3.txt') as f:
        track = get_track(f.read().strip())

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
        if r+1 < len(mp) and mp[r+1][c] != ' ' and (r+1, c) != prev:
            r += 1
        elif c+1 < len(mp[r]) and mp[r][c+1] != ' ' and (r, c+1) != prev:
            c += 1
        elif r-1 >= 0 and mp[r-1][c] != ' ' and (r-1, c) != prev:
            r -= 1
        elif c-1 >= 0 and mp[r][c-1] != ' ' and (r, c-1) != prev:
            c -= 1
        prev = old
    track.append('S')
    return track
