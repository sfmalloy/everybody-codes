from collections import deque, defaultdict


def solve(tree: dict[str, list[str]]):
    q = deque([('RR', [], False, False)])
    paths = defaultdict(list)
    while len(q) > 0:
        key, path, ant, bug = q.popleft()
        if key == 'ANT':
            if ant:
                continue
            ant = True
        elif key == 'BUG':
            if bug:
                continue
            bug = True
        elif key == '@':
            path.append('@')
            paths[len(path)].append(path)
            continue
        if key in tree:
            for v in tree[key]:
                q.append((v, path+[key], ant, bug))
    for v in paths.values():
        if len(v) == 1:
            return ''.join([p[0] for p in v[0]])
