import copy
import heapq

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

def manhattan_distance(state, goal_state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0: 
                goal_position = find_blank_index(goal_state, value)
                distance += abs(i - goal_position[0]) + abs(j - goal_position[1])
    return distance
def best_first_search(start_state, goal_state):
    priority_queue = []
    visited = set()
    start_tuple = tuple(tuple(row) for row in start_state)
    goal_tuple = tuple(tuple(row) for row in goal_state)
    heapq.heappush(priority_queue, (manhattan_distance(start_state, goal_state), [], start_state))
    while priority_queue:
        heuristic_cost, path, current_state = heapq.heappop(priority_queue)
        current_state_tuple = tuple(tuple(row) for row in current_state)
        if current_state_tuple in visited:
            continue
        visited.add(current_state_tuple)
        if current_state == goal_state:
            return path
        for new_state, move_description in generate_moves(current_state):
            new_state_tuple = tuple(tuple(row) for row in new_state)
            if new_state_tuple not in visited:
                new_path = path + [(new_state, move_description)]
                new_heuristic_cost = manhattan_distance(new_state, goal_state)
                heapq.heappush(priority_queue, (new_heuristic_cost, new_path, new_state))
    return None

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
    print("Starting Best-First Search...")
    solution = best_first_search(eight_puzzle, goal_state)
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
