
# Chess with AI (Python Pygame)

A **fully functional Chess game** built with **Python** and **Pygame**, featuring an AI opponent. The game includes Unicode chess symbols, highlights valid moves, shows game status, and automatically handles check, checkmate, and pawn promotion.

---

## 🎮 Game Description

This is a classic **Chess game** where a human player (White) competes against an AI (Black). Features include:

- Full chess rules including **pawn promotion, check, and checkmate**  
- Visual **board highlights** for selected pieces and valid moves  
- Unicode symbols with fallback to text if font support is unavailable  
- Status bar showing **turn, game status, and symbol mode**  
- **Restart functionality** after game over  

---

## 🖥️ How to Run

1. Make sure **Python 3.x** is installed: [Download Python](https://www.python.org/downloads/)

2. Install **Pygame** (if not already installed):

```bash
pip install pygame
````

3. Clone or download this repository:

```bash
git clone https://github.com/yourusername/chess-ai-pygame.git
cd chess-ai-pygame
```

4. Run the game:

```bash
python chess_ai_game.py
```

> The game window will open. White moves are controlled with the mouse. The AI automatically plays Black.

---

## ⚙️ Requirements

* **Python 3.x**
* **Pygame**
  No additional libraries are required.

---

## 🕹️ How to Play

1. Click on a piece to select it (highlighted in **yellow**)
2. Valid moves are highlighted in **green**
3. Click on a valid square to move the piece
4. The AI will respond automatically for Black
5. The game ends on **checkmate** or **stalemate**
6. Press **R** to restart after game over

---

## 🧠 AI Algorithm

The AI uses a **Minimax algorithm with Alpha-Beta pruning**:

* **Minimax:** Searches possible moves and evaluates the board to choose the optimal move
* **Alpha-Beta Pruning:** Reduces unnecessary search for efficiency
* **Evaluation Function:** Assigns point values to pieces and favors central positions for stronger AI decisions

> AI depth is currently set to 2 for faster moves. Increase depth for a stronger AI at the cost of longer computation time.

---

## 🎨 Design & Features

* **Board:** 8x8 chessboard with light and dark squares
* **Pieces:** Unicode symbols with text fallback
* **Highlights:** Yellow for selected piece, green for valid moves
* **Status Bar:** Shows turn, check/checkmate status, and symbol usage
* **Restart:** Press R to reset the game
* **Responsive Graphics:** Adapts to window size

---

## 📸 Screenshots

![Chess Screenshot](screenshot1.png)

*Board with highlighted moves and AI opponent.*

---

## 📝 Notes

* Unicode symbols may not render on all systems; the game will automatically switch to text symbols
* The AI depth can be changed in `ChessAI.depth` to adjust difficulty
* Supports standard chess rules except for **en passant** and **castling** (optional future improvement)

---


**Enjoy playing Chess against AI!**

