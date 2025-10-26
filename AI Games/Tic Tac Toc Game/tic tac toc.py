import pygame
import sys
import random
import time

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 700
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
TEXT_COLOR = (255, 255, 255)
BUTTON_COLOR = (52, 152, 219)
BUTTON_HOVER_COLOR = (41, 128, 185)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)

# Game state
board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
player = 'X'  # Human is X, AI is O
game_over = False
winner = None

# Fonts
font = pygame.font.SysFont('Arial', 40)
small_font = pygame.font.SysFont('Arial', 30)

def draw_lines():
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT - 100), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT - 100), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                # Draw X
                pygame.draw.line(screen, CROSS_COLOR, 
                                (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                ((col + 1) * SQUARE_SIZE - SPACE, (row + 1) * SQUARE_SIZE - SPACE), 
                                CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, 
                                ((col + 1) * SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE),
                                (col * SQUARE_SIZE + SPACE, (row + 1) * SQUARE_SIZE - SPACE), 
                                CROSS_WIDTH)
            elif board[row][col] == 'O':
                # Draw O
                pygame.draw.circle(screen, CIRCLE_COLOR, 
                                  (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                                  CIRCLE_RADIUS, CIRCLE_WIDTH)

def draw_status():
    # Draw status area
    pygame.draw.rect(screen, LINE_COLOR, (0, HEIGHT - 100, WIDTH, 100))
    
    if game_over:
        if winner == 'X':
            text = font.render('You Win!', True, TEXT_COLOR)
        elif winner == 'O':
            text = font.render('AI Wins!', True, TEXT_COLOR)
        else:
            text = font.render('Game Draw!', True, TEXT_COLOR)
    else:
        if player == 'X':
            text = font.render('Your Turn (X)', True, TEXT_COLOR)
        else:
            text = font.render('AI Thinking...', True, TEXT_COLOR)
    
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT - 80))

def draw_restart_button():
    button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT - 50, 200, 40)
    
    # Check if mouse is over button
    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, BUTTON_HOVER_COLOR, button_rect, border_radius=10)
    else:
        pygame.draw.rect(screen, BUTTON_COLOR, button_rect, border_radius=10)
    
    text = small_font.render('Restart Game', True, TEXT_COLOR)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT - 45))
    
    return button_rect

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] is None

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] is None:
                return False
    return True

def check_win():
    # Check rows
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            return board[row][0]
    
    # Check columns
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    
    return None

def minimax(board, depth, is_maximizing):
    winner = check_win()
    
    # If AI wins
    if winner == 'O':
        return 1
    # If human wins
    elif winner == 'X':
        return -1
    # If it's a tie
    elif is_board_full():
        return 0
    
    if is_maximizing:
        best_score = -float('inf')
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] is None:
                    board[row][col] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[row][col] = None
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] is None:
                    board[row][col] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[row][col] = None
                    best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -float('inf')
    move = None
    
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] is None:
                board[row][col] = 'O'
                score = minimax(board, 0, False)
                board[row][col] = None
                if score > best_score:
                    best_score = score
                    move = (row, col)
    
    if move:
        mark_square(move[0], move[1], 'O')
        return True
    return False

def restart_game():
    global board, player, game_over, winner
    board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    player = 'X'
    game_over = False
    winner = None
    screen.fill(BG_COLOR)
    draw_lines()
    draw_status()

# Draw the initial board
draw_lines()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            
            # Check if click is on the board
            if mouseY < HEIGHT - 100:
                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE
                
                if available_square(clicked_row, clicked_col) and player == 'X':
                    mark_square(clicked_row, clicked_col, player)
                    
                    # Check for win or draw
                    winner = check_win()
                    if winner:
                        game_over = True
                    elif is_board_full():
                        game_over = True
                    
                    player = 'O'
        
        # Handle restart button click
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT - 50, 200, 40)
            if button_rect.collidepoint((mouseX, mouseY)):
                restart_game()
    
    # AI's turn
    if not game_over and player == 'O':
        # Add a small delay to make AI thinking visible
        pygame.display.update()
        time.sleep(1)
        
        if best_move():
            winner = check_win()
            if winner:
                game_over = True
            elif is_board_full():
                game_over = True
            
            player = 'X'
    
    # Draw everything
    draw_figures()
    draw_status()
    button_rect = draw_restart_button()
    
    pygame.display.update()