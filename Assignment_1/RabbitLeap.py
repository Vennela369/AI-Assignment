from collections import deque

def is_goal(state):
    # Goal is rabbits swapped: '<' on left, '_' in middle, '>' on right
    return state == ['<', '<', '<', '_', '>', '>', '>']

def get_neighbors(state):
    neighbors = []
    empty_index = state.index('_')

    # Possible moves: rabbits can move forward 1 step or jump over 1 rabbit
    # For each rabbit next to empty or 2 spaces away, check valid moves

    for i, rabbit in enumerate(state):
        if rabbit == '_':
            continue
        # Move right (if east-bound '>' and empty is right)
        if rabbit == '>' and i + 1 < len(state):
            # move 1 step
            if i + 1 == empty_index:
                new_state = state.copy()
                new_state[i], new_state[i + 1] = new_state[i + 1], new_state[i]
                neighbors.append(new_state)
            # jump over one rabbit
            elif i + 2 == empty_index and state[i + 1] in ['<', '>']:
                new_state = state.copy()
                new_state[i], new_state[i + 2] = new_state[i + 2], new_state[i]
                neighbors.append(new_state)

        # Move left (if west-bound '<' and empty is left)
        if rabbit == '<' and i - 1 >= 0:
            # move 1 step
            if i - 1 == empty_index:
                new_state = state.copy()
                new_state[i], new_state[i - 1] = new_state[i - 1], new_state[i]
                neighbors.append(new_state)
            # jump over one rabbit
            elif i - 2 == empty_index and state[i - 1] in ['<', '>']:
                new_state = state.copy()
                new_state[i], new_state[i - 2] = new_state[i - 2], new_state[i]
                neighbors.append(new_state)

    return neighbors

def bfs(start):
    queue = deque([start])
    visited = set()
    visited.add(tuple(start))
    parent = {tuple(start): None}

    while queue:
        state = queue.popleft()
        if is_goal(state):
            # Reconstruct path
            path = []
            while state:
                path.append(state)
                state = parent[tuple(state)]
            return path[::-1]

        for neighbor in get_neighbors(state):
            t_neighbor = tuple(neighbor)
            if t_neighbor not in visited:
                visited.add(t_neighbor)
                parent[t_neighbor] = state
                queue.append(neighbor)
    return None

def dfs(start):
    stack = [start]
    visited = set()
    visited.add(tuple(start))
    parent = {tuple(start): None}

    while stack:
        state = stack.pop()
        if is_goal(state):
            # Reconstruct path
            path = []
            while state:
                path.append(state)
                state = parent[tuple(state)]
            return path[::-1]

        for neighbor in get_neighbors(state):
            t_neighbor = tuple(neighbor)
            if t_neighbor not in visited:
                visited.add(t_neighbor)
                parent[t_neighbor] = state
                stack.append(neighbor)
    return None

def print_path(path):
    for step in path:
        print(' '.join(step))
    print(f"Steps: {len(path)-1}")

if __name__ == "__main__":
    start = ['>', '>', '>', '_', '<', '<', '<']

    print("BFS Solution:")
    bfs_path = bfs(start)
    if bfs_path:
        print_path(bfs_path)
    else:
        print("No solution found with BFS")

    print("\nDFS Solution:")
    dfs_path = dfs(start)
    if dfs_path:
        print_path(dfs_path)
    else:
        print("No solution found with DFS")
