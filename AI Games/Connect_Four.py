import tkinter as tk
from tkinter import messagebox
import random
import math

ROWS = 6
COLUMNS = 7
EMPTY = " "
PLAYER_PIECE = "X"
COMPUTER_PIECE = "O"

def create_board():
    return [[EMPTY for _ in range(COLUMNS)] for _ in range(ROWS)]

def is_valid_location(board, col):
    return board[0][col] == EMPTY

def get_next_open_row(board, col):
    for r in range(ROWS - 1, -1, -1):
        if board[r][col] == EMPTY:
            return r
    return None

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def winning_move(board, piece):
    for c in range(COLUMNS - 3):
        for r in range(ROWS):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    for c in range(COLUMNS):
        for r in range(ROWS - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    for c in range(COLUMNS - 3):
        for r in range(ROWS - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    for c in range(COLUMNS - 3):
        for r in range(3, ROWS):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
    return False

def get_valid_locations(board):
    return [col for col in range(COLUMNS) if is_valid_location(board, col)]

def is_terminal_node(board):
    return winning_move(board, PLAYER_PIECE) or winning_move(board, COMPUTER_PIECE) or len(get_valid_locations(board)) == 0

def evaluate_window(window, piece):
    score = 0
    opp_piece = PLAYER_PIECE if piece == COMPUTER_PIECE else COMPUTER_PIECE
    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 10
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 5
    if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
        score -= 80
    return score

def score_position(board, piece):
    score = 0
    center_array = [board[r][COLUMNS // 2] for r in range(ROWS)]
    center_count = center_array.count(piece)
    score += center_count * 6
    for r in range(ROWS):
        row_array = [board[r][c] for c in range(COLUMNS)]
        for c in range(COLUMNS - 3):
            window = row_array[c:c + 4]
            score += evaluate_window(window, piece)
    for c in range(COLUMNS):
        col_array = [board[r][c] for r in range(ROWS)]
        for r in range(ROWS - 3):
            window = col_array[r:r + 4]
            score += evaluate_window(window, piece)
    for r in range(ROWS - 3):
        for c in range(COLUMNS - 3):
            window = [board[r + i][c + i] for i in range(4)]
            score += evaluate_window(window, piece)
    for r in range(3, ROWS):
        for c in range(COLUMNS - 3):
            window = [board[r - i][c + i] for i in range(4)]
            score += evaluate_window(window, piece)
    return score

def minimax(board, depth, alpha, beta, maximizingPlayer):
    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, COMPUTER_PIECE):
                return (None, 100000000000000)
            elif winning_move(board, PLAYER_PIECE):
                return (None, -10000000000000)
            else:
                return (None, 0)
        else:
            return (None, score_position(board, COMPUTER_PIECE))
    if maximizingPlayer:
        value = -math.inf
        best_col = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            temp_board = [r[:] for r in board]
            drop_piece(temp_board, row, col, COMPUTER_PIECE)
            new_score = minimax(temp_board, depth - 1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                best_col = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_col, value
    else:
        value = math.inf
        best_col = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            temp_board = [r[:] for r in board]
            drop_piece(temp_board, row, col, PLAYER_PIECE)
            new_score = minimax(temp_board, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                best_col = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return best_col, value

class ConnectFourGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect Four")
        self.board = create_board()
        self.buttons = []
        self.labels = [[None for _ in range(COLUMNS)] for _ in range(ROWS)]
        self.create_widgets()
        self.game_over = False

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack()
        # Create column buttons
        for col in range(COLUMNS):
            btn = tk.Button(frame, text=str(col+1), width=4, height=2, command=lambda c=col: self.player_move(c))
            btn.grid(row=0, column=col)
            self.buttons.append(btn)
        # Create board labels
        for r in range(ROWS):
            for c in range(COLUMNS):
                lbl = tk.Label(frame, text=" ", width=4, height=2, borderwidth=2, relief="ridge", font=("Arial", 18))
                lbl.grid(row=r+1, column=c)
                self.labels[r][c] = lbl

    def player_move(self, col):
        if self.game_over or not is_valid_location(self.board, col):
            return
        row = get_next_open_row(self.board, col)
        drop_piece(self.board, row, col, PLAYER_PIECE)
        self.update_board()
        if winning_move(self.board, PLAYER_PIECE):
            self.game_over = True
            messagebox.showinfo("Game Over", "You win!")
            self.reset_game()
            return
        elif len(get_valid_locations(self.board)) == 0:
            self.game_over = True
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset_game()
            return
        self.root.after(500, self.computer_move)

    def computer_move(self):
        if self.game_over:
            return
        col = minimax(self.board, 4, -math.inf, math.inf, True)[0]
        if col is not None and is_valid_location(self.board, col):
            row = get_next_open_row(self.board, col)
            drop_piece(self.board, row, col, COMPUTER_PIECE)
            self.update_board()
            if winning_move(self.board, COMPUTER_PIECE):
                self.game_over = True
                messagebox.showinfo("Game Over", "Computer wins!")
                self.reset_game()
                return
            elif len(get_valid_locations(self.board)) == 0:
                self.game_over = True
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
                return

    def update_board(self):
        for r in range(ROWS):
            for c in range(COLUMNS):
                piece = self.board[r][c]
                if piece == PLAYER_PIECE:
                    self.labels[r][c].config(text="X", fg="red")
                elif piece == COMPUTER_PIECE:
                    self.labels[r][c].config(text="O", fg="blue")
                else:
                    self.labels[r][c].config(text=" ")

    def reset_game(self):
        self.board = create_board()
        self.update_board()
        self.game_over = False

if __name__ == "__main__":
    root = tk.Tk()
    game = ConnectFourGUI(root)
    root.mainloop()