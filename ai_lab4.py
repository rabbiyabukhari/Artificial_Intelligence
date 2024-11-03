import copy
import heapq
from itertools import chain

class AStarSolver: 
    def __init__(self, start_state, goal_state):
        self.start_state = start_state
        self.goal_state = goal_state

    def trace_solution(self, node):
        path = []
        while node.parent is not None:
            path.append((node.state, node.move))
            node = node.parent
        path.reverse()
        return path

    def is_solvable(self, state):
        inversions = 0
        flat_state = list(chain.from_iterable(state))
        flat_state.remove(0)
        for i in range(len(flat_state) - 1):
            for j in range(i + 1, len(flat_state)):
                if flat_state[i] > flat_state[j]:
                    inversions += 1
        return inversions % 2 == 0

    def solve(self):
        if not self.is_solvable(self.start_state):
            return False
        pq = []
        visited = set()
        root = PuzzleNode(self.start_state, None, None, 0, 0)
        root.calculate_heuristic(self.goal_state)
        heapq.heappush(pq, (root.f_cost, root))
        while pq:
            fn, curr_node = heapq.heappop(pq)
            curr_t = tuple(tuple(row) for row in curr_node.state)
            if curr_t in visited:
                continue
            visited.add(curr_t)
            if curr_node.state == self.goal_state:
                return self.trace_solution(curr_node)
            for child in curr_node.generate_children():
                child.calculate_heuristic(self.goal_state)
                child_t = tuple(tuple(row) for row in child.state)
                if child_t not in visited:
                    heapq.heappush(pq, (child.f_cost, child))
        return None


class PuzzleNode:
    def __init__(self, state, parent, move, g_cost, h_cost):
        self.state = state
        self.parent = parent
        self.move = move
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = g_cost + h_cost

    def find_blank_index(self, state, char=0):
        for i, row in enumerate(state):
            if char in row:
                return (i, row.index(char))

    def generate_children(self):
        children = []
        row_moves = [1, -1, 0, 0]
        col_moves = [0, 0, 1, -1]
        move_descriptions = ['down', 'up', 'right', 'left']
        blank_index = self.find_blank_index(self.state)
        for i in range(4):
            new_r = blank_index[0] + row_moves[i]
            new_c = blank_index[1] + col_moves[i]
            if 0 <= new_r <= 2 and 0 <= new_c <= 2:
                new_state = copy.deepcopy(self.state)
                new_state[blank_index[0]][blank_index[1]], new_state[new_r][new_c] = new_state[new_r][new_c], new_state[blank_index[0]][blank_index[1]]
                new_node = PuzzleNode(new_state, self, move_descriptions[i], self.g_cost + 1, 0)
                children.append(new_node)
        return children

    def calculate_heuristic(self, goal_state):
        self.h_cost = 0
        for i in range(3):
            for j in range(3):
                value = self.state[i][j]
                if value != 0:
                    goal_position = self.find_blank_index(goal_state, value)
                    self.h_cost += abs(i - goal_position[0]) + abs(j - goal_position[1])
        self.f_cost = self.g_cost + self.h_cost
    def __lt__(self, other):
        return self.f_cost < other.f_cost


def main():
  
    puzzle1 = [
        [0, 1, 2],
        [4, 3, 8],
        [5, 6, 7]
    ]
    goal_state = [
        [1, 2, 8],
        [0, 3, 7],
        [4, 5, 6]
    ]

    solver = AStarSolver(puzzle1, goal_state)
    solution = solver.solve()
    if solution:
        print("Solution found:")
        for state, move in solution:
            print(f"Move: {move}")
            for row in state:
                print(row)
            print()
    else:
        print("No solution found")

    print()
    print("2nd puzzle with 3 inversions:")

    puzzle2 = [
        [2, 0, 1],
        [4, 3, 8],
        [5, 6, 7]
    ]

    solver = AStarSolver(puzzle2, goal_state)
    solution = solver.solve()

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
