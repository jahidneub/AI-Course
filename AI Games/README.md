# 🎮 AI Game Collection (Python)

> 🤖 This project contains **three classic AI-based games** developed in Python — each powered by the **Minimax Algorithm** with **Alpha-Beta Pruning** and intelligent move selection.

---


## 🧠 Overview

This project demonstrates the use of **Artificial Intelligence search algorithms** in games.  
The main focus is on implementing:
- **Minimax Algorithm**
- **Alpha-Beta Pruning**
- **Heuristic Evaluation**
- **Depth-Limited Search**

Each game is designed with a simple GUI using `tkinter` or `pygame`, and all three share the same interface layout and logic flow.

---

## 🎯 Game 1 – Chess

**Description:**  
A simplified Chess AI that can predict the next move using search algorithms. It evaluates possible future positions of the board to make intelligent decisions.

**Algorithm Used:**  
- **Minimax Algorithm**
- **Alpha-Beta Pruning**
- **Depth-Limited Search**
- **Piece Value Evaluation Function**

**How It Works:**
1. AI generates all possible legal moves.
2. Evaluates board using a scoring function.
3. Uses Minimax to select the optimal move.
4. Alpha-Beta Pruning reduces unnecessary search.

---

## 🎯 Game 2 – Connect Four

**Description:**  
A 7×6 grid-based game where players drop colored discs into a column. The AI analyzes all possible moves to block the opponent or win.

**Algorithm Used:**  
- **Minimax Algorithm with Depth Limit**  
- **Alpha-Beta Pruning**  
- **Heuristic Evaluation** (based on number of connected discs)

**How It Works:**
1. The AI simulates possible column drops.
2. Each move is scored using heuristic evaluation.
3. The best score is selected using Minimax + Alpha-Beta pruning.

---

## 🎯 Game 3 – Tic Tac Toe

**Description:**  
A classic 3×3 grid game where the player competes against an AI that never loses. The AI uses **Minimax with Alpha-Beta Pruning** to predict the best move.

**Algorithm Used:**  
- **Minimax Algorithm:** Evaluates all possible moves and chooses the optimal one.  
- **Alpha-Beta Pruning:** Optimizes Minimax by skipping unnecessary branches.

**How It Works:**
1. The game board is represented as a 3×3 matrix.
2. AI simulates each move recursively.
3. Using Minimax, it chooses the move that maximizes its chance of winning.
4. Alpha-Beta pruning reduces the number of evaluated nodes.

---

## 🧰 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/AI-Game-Collection.git
cd AI-Game-Collection

# Install required libraries
pip install pygame
