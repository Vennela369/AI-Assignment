from collections import deque

# People and their times
times = {'Amogh': 5, 'Ameya': 10, 'Grandmother': 20, 'Grandfather': 25}
people = list(times.keys())
max_time = 60

def is_goal(state):
    # Goal is everyone on the other side
    start_side, end_side, time, umbrella_side = state
    return len(start_side) == 0

def get_moves(state):
    start_side, end_side, time, umbrella_side = state
    moves = []
    if umbrella_side == 'start':
        # Move two people from start to end
        for i in range(len(start_side)):
            for j in range(i, len(start_side)):
                p1, p2 = start_side[i], start_side[j]
                cross_time = max(times[p1], times[p2])
                new_time = time + cross_time
                if new_time <= max_time:
                    new_start = list(start_side)
                    new_end = list(end_side)
                    new_start.remove(p1)
                    if p1 != p2:
                        new_start.remove(p2)
                        new_end += [p1, p2]
                    else:
                        new_end.append(p1)
                    moves.append((tuple(sorted(new_start)), tuple(sorted(new_end)), new_time, 'end', (p1, p2)))
    else:
        # Move one person from end to start
        for p in end_side:
            cross_time = times[p]
            new_time = time + cross_time
            if new_time <= max_time:
                new_start = list(start_side)
                new_end = list(end_side)
                new_end.remove(p)
                new_start.append(p)
                moves.append((tuple(sorted(new_start)), tuple(sorted(new_end)), new_time, 'start', (p,)))
    return moves

def bfs():
    start_state = (tuple(sorted(people)), tuple(), 0, 'start')
    queue = deque([(start_state, [])])
    visited = set()
    while queue:
        (state, path) = queue.popleft()
        if is_goal(state):
            return path
        if state in visited:
            continue
        visited.add(state)
        for next_state in get_moves(state):
            next_tuple = next_state[:4]
            if next_tuple not in visited:
                queue.append((next_tuple, path + [next_state[4]]))
    return None

def dfs():
    start_state = (tuple(sorted(people)), tuple(), 0, 'start')
    stack = [(start_state, [])]
    visited = set()
    while stack:
        (state, path) = stack.pop()
        if is_goal(state):
            return path
        if state in visited:
            continue
        visited.add(state)
        for next_state in get_moves(state):
            next_tuple = next_state[:4]
            if next_tuple not in visited:
                stack.append((next_tuple, path + [next_state[4]]))
    return None

def print_solution(solution):
    if not solution:
        print("No solution found within time limit.")
        return
    side = 'start'
    for move in solution:
        if len(move) == 2:
            print(f"{move[0]} and {move[1]} cross from {side} side")
            side = 'end' if side == 'start' else 'start'
        else:
            print(f"{move[0]} crosses from {side} side")
            side = 'end' if side == 'start' else 'start'

print("BFS Solution:")
bfs_solution = bfs()
print_solution(bfs_solution)

print("\nDFS Solution:")
dfs_solution = dfs()
print_solution(dfs_solution)
