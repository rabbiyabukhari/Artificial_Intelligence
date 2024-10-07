import copy
def find_blank_index(grid, char):
    result = [[row_index, row.index(char)]
              for row_index, row in enumerate(grid) 
              if char in row]
    return result[0] 
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


def depth_limited_search(state, goal_state, depth_limit, path, visited):
    state_tuple = tuple(tuple(row) for row in state)
    if state == goal_state:
        return path
    if depth_limit <= 0:
        return None
    visited.add(state_tuple)
    for new_state, move_description in generate_moves(state):
        new_state_tuple = tuple(tuple(row) for row in new_state)
        if new_state_tuple not in visited:
            result = depth_limited_search(new_state, goal_state, depth_limit - 1, path + [(new_state, move_description)], visited)
            if result is not None:
                return result  
    visited.remove(state_tuple)
    return None 
def iddfs(start_state, goal_state):
    depth = 0
    while True:
        visited = set() 
        result = depth_limited_search(start_state, goal_state, depth, [], visited)
        if result is not None:
            return result
        print(f"Increasing depth to {depth}")  
        depth += 1  


def main():
    eight_puzzle = [
        [0, 1, 2],
        [4, 3, 8],
        [5, 6, 7]
    ]
    goal_state = [
        [1, 2, 8],
        [0, 3, 7],
        [4, 5, 6]
    ]
    print("Starting the search...")
    solution = iddfs(eight_puzzle, goal_state)
    if solution:
        print("Solution found:")
        for state, move in solution:
            print(f"Move: {move}")
            for row in state:
                print(row)
            print()
    else:
        print("No solution found")
main()
