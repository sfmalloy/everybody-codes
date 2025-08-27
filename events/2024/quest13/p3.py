from collections import defaultdict
from dataclasses import dataclass, field
from queue import PriorityQueue

from .model import Vec


@dataclass(eq=True, frozen=True, order=True)
class Node:
    curr: Vec = field(compare=False)
    dist: int
    path: list = field(default_factory=list, compare=False)


def solve(_: Vec, end: Vec, grid: list[list[int]]):
    q: PriorityQueue[Node] = PriorityQueue()
    for r in range(len(grid)):
        if r == 0 or r == len(grid)-1:
            for c in range(len(grid[r])):
                q.put(Node(Vec(r, c), 0, []))
        else:
            q.put(Node(Vec(r, 0), 0, []))
            q.put(Node(Vec(r, len(grid[r])-1), 0, []))
    
    dists = defaultdict(lambda: float('inf'))
    visited = set()
    neighbor_deltas = [Vec(1, 0), Vec(-1, 0), Vec(0, 1), Vec(0, -1)]
    while not q.empty():
        node = q.get()
        curr = node.curr
        dist = node.dist
        path = node.path

        if curr in visited:
            continue
        visited.add(curr)
        curr_cost = grid[curr.r][curr.c]
        for delta in neighbor_deltas:
            neighbor = curr + delta
            if not valid_neighbor(neighbor, grid):
                continue
            neighbor_cost = grid[neighbor.r][neighbor.c]
            a = abs(neighbor_cost - curr_cost)
            b = abs((max(curr_cost, neighbor_cost)-10) - min(neighbor_cost, curr_cost))
            curr_dist = dist + min(a, b) + 1
            dists[neighbor] = min(curr_dist, dists[neighbor])
            if neighbor not in visited:
                q.put(Node(neighbor, curr_dist, path + [neighbor]))
    return dists[end]


def valid_neighbor(v: Vec, grid: list[list[str]]):
    return v.r < len(grid) and v.r >= 0 and v.c < len(grid[0]) and v.c >= 0 and grid[v.r][v.c] >= 0
