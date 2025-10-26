Here’s a **professional README.md** for your Tic Tac Toe game with AI implemented in Python using Pygame:

---

# Tic Tac Toe with AI

A simple **Tic Tac Toe** game implemented in **Python** using **Pygame**, where the player competes against an AI using the **Minimax algorithm**.

---

## 🎮 Game Description

This project is a graphical Tic Tac Toe game:

* Player plays as **X** (human) and AI plays as **O**.
* The AI uses the **Minimax algorithm** to make optimal moves.
* The game detects **win, loss, or draw** conditions.
* Includes a **restart button** to start a new game.

---

## 🖥️ Features

* Interactive **GUI** with Pygame.
* **Minimax AI** opponent.
* Highlights game **status** (Your Turn, AI Thinking, Winner).
* **Restart button** for replay.
* Visual representation of **X** and **O** with colors and symbols.
* Detects **draw** when the board is full.

---

## ⚙️ Software Requirements

* Python 3.8 or higher
* Pygame library

### Install Pygame

```bash
pip install pygame
```

---

## 📂 How to Run

1. Clone the repository or download the project files.
2. Open a terminal in the project directory.
3. Run the game using:

```bash
python tic_tac_toe.py
```

4. The game window will open. Click on an empty square to place your **X**. AI will respond automatically.

---

## 🎯 How to Play

1. The **player always starts first** as X.
2. Click on a square to place your X.
3. The AI (O) will make its move automatically.
4. The game status at the bottom will indicate:

   * **Your Turn (X)**
   * **AI Thinking…**
   * **You Win / AI Wins / Draw**
5. Click **Restart Game** to play again.

---

## 🧠 Algorithm Used

**Minimax Algorithm:**

* A recursive algorithm used for decision making in zero-sum games.
* AI evaluates **all possible moves** and chooses the optimal move.
* Scores:

  * `1` for AI win
  * `-1` for player win
  * `0` for draw
* AI always plays optimally and tries to maximize its score.

---

## 📸 Screenshots
screenshot1.png
screenshot2.png
*(Include screenshots of the game window, X/O placements, win/draw screen, and restart button.)*

---

## 📝 Notes

* The AI will never lose if it plays first or second optimally.
* The game has a **visible AI thinking delay** for better user experience.
* Board and UI sizes are **600x700 pixels** with status and button areas.

---

## 🔄 Restarting the Game

* Click the **Restart Game** button at the bottom of the screen.
* Board and game state will reset automatically.

---

## 🖌️ Colors Used

* Background: `#1CA99C`
* Lines: `#179187`
* X: `#424242`
* O: `#EFE7C8`
* Status & Buttons: Blue shades with hover effects

---



