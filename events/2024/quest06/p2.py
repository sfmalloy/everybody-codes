from collections import deque, defaultdict


def solve(tree: dict[str, list[str]]):
    q = deque([('RR', [])])
    paths = defaultdict(list)
    while len(q) > 0:
        key, path = q.popleft()
        if key == '@':
            path.append('@')
            paths[len(path)].append(path)
            continue
        if key in tree:
            for v in tree[key]:
                q.append((v, path+[key]))
    for v in paths.values():
        if len(v) == 1:
            return ''.join([p[0] for p in v[0]])
