from math import inf


class Minimax:
    def __init__(self, game_state):
        self.current_state=game_state
        
    def is_terminal(self, state):
        win_states=[
            [[0,0],[1,1],[2,2]],
            [[2,0],[1,1],[0,2]],
            [[1,0],[1,1],[1,2]],
            [[0,1],[1,1],[2,1]],   
            [[0,0],[1,0],[2,0]],
            [[0,2],[1,2],[2,2]],
            [[0,0],[0,1],[0,2]],
            [[2,0],[2,1],[2,2]]            
        ]
        for wst in win_states:
            if state[wst[0][0]][wst[0][1]]==state[wst[1][0]][wst[1][1]]==state[wst[2][0]][wst[2][1]]!=" ":
                return True
        return ' ' not in state
            
    def utility(self, state):
        win_states=[
            [[0,0],[1,1],[2,2]],
            [[2,0],[1,1],[0,2]],
            [[1,0],[1,1],[1,2]],
            [[0,1],[1,1],[2,1]],   
            [[0,0],[1,0],[2,0]],
            [[0,2],[1,2],[2,2]],
            [[0,0],[0,1],[0,2]],
            [[2,0],[2,1],[2,2]]            
        ]
        for wst in win_states:
            if state[wst[0][0]][wst[0][1]]==state[wst[1][0]][wst[1][1]]==state[wst[2][0]][wst[2][1]]=='X':
                return 1
            elif state[wst[0][0]][wst[0][1]]==state[wst[1][0]][wst[1][1]]==state[wst[2][0]][wst[2][1]]=='O':
                return -1
        return 0
    def get_available_moves(self, state):
        return [(i, j) for i in range(3) for j in range(3) if state[i][j] == " "]
    
    def minimax(self, state, depth, maximizing_player):
        if self.is_terminal(state):
            return self.utility(state)
        if maximizing_player:
            maxval=-(inf)
            for move in self.get_available_moves(state):
                state[move] = 'X'
                val = self.minimax(state, depth + 1, False)
                state[move] = ' '  
                maxval = max(maxval, val)
            return maxval   
        else:
            minval=inf
            for move in self.get_available_moves(state):
                state[move] = 'O'
                val = self.minimax(state, depth + 1, True)
                state[move] = ' '  
                minval = min(minval, val)
            return minval
        
    def best_move(self, state):
        best_val = -(inf)
        move = -1
        for i in self.get_available_moves(state):
            state[i[0]][i[1]] = 'X'  
            move_val = self.minimax(state, 3, False)
            state[i[0]][i[1]] = ' '  
            if move_val > best_val:
                best_val = move_val
                move = i
        return move
    

    
def main():
    initial_state = [['X', 'O', ' '],
                     ['O', 'X', ' '],
                     [' ', ' ', ' ']]

    print("Minimax:")
    m = Minimax(initial_state)
    best_move = m.best_move(initial_state)
    print('The best move is:', best_move)



main()
