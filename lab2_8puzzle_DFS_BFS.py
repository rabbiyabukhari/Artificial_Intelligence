from collections import deque
import copy

def find_blank_index(grid, char):
    for row_index, row in enumerate(grid):
        if char in row:
            return [row_index, row.index(char)]
    return None
def generate_moves(grid):
    r_mov = [1, -1, 0, 0]
    c_mov = [0, 0, 1, -1]
    statelst = []
    blank_ind = find_blank_index(grid, 0) 
    move_descriptions = ['down', 'up', 'right', 'left']
    for i in range(4):
        new_r = blank_ind[0] + r_mov[i]
        new_c = blank_ind[1] + c_mov[i]
        if 0 <= new_r <= 2 and 0 <= new_c <= 2:
            grid2 = copy.deepcopy(grid)
            grid2[blank_ind[0]][blank_ind[1]], grid2[new_r][new_c] = grid2[new_r][new_c], grid2[blank_ind[0]][blank_ind[1]]
            statelst.append((grid2, move_descriptions[i]))
    return statelst

def dfs(start_state, goal_state):
    stack = [(start_state, [])]  
    visited = set()
    while stack:
        state, path = stack.pop()
        if state == goal_state:
            return path
        state_tuple = tuple(tuple(row) for row in state)
        if state_tuple not in visited:
            visited.add(state_tuple)
            for new_state, move_description in generate_moves(state):
                stack.append((new_state, path + [move_description]))
    return None

def bfs(start_state, goal_state):
    queue = deque([(start_state, [])]) 
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state == goal_state:
            return path
        state_tuple = tuple(tuple(row) for row in state)
        if state_tuple not in visited:
            visited.add(state_tuple)
            for new_state, move_description in generate_moves(state):
                queue.append((new_state, path + [move_description]))
    return None  

def print_solution(solution):
    if solution:
        print(f"Solution found in {len(solution)} moves:")
        for move in solution:
            print(f"Move: {move}")
    else:
        print("No solution found")

def main():
    eight_puzzle = [
        [0, 1, 2],
        [4, 3, 8],
        [5, 6, 7]
    ]
    goal_state = [
        [1, 2, 8],
        [4, 3, 0],
        [5, 6, 7]
    ]
    
    print("Starting BFS...")
    bfs_solution = bfs(eight_puzzle, goal_state)
    print_solution(bfs_solution)
    print()
    
    print("Starting DFS...")
    dfs_solution = dfs(eight_puzzle, goal_state)
    print_solution(dfs_solution)
    
main()
