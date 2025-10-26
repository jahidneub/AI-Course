# 🎮 AI Game Collection (Python)

> 🤖 This project contains **three classic AI-based games** developed in Python — each powered by the **Minimax Algorithm** with **Alpha-Beta Pruning** and intelligent move selection.

---

## 🧩 Table of Contents
1. [Overview](#overview)
2. [Game 1 – Tic Tac Toe](#game-1--tic-tac-toe)
3. [Game 2 – Connect Four](#game-2--connect-four)
4. [Game 3 – Chess](#game-3--chess)
5. [Algorithms Used](#algorithms-used)
6. [Applications](#applications)
7. [Complexity Analysis](#complexity-analysis)
8. [Installation](#installation)
9. [How to Run](#how-to-run)
10. [Screenshots](#screenshots)
11. [License](#license)

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

## 🎯 Game 1 – Tic Tac Toe

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

## 🎯 Game 3 – Chess

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

## ⚙️ Algorithms Used

| Algorithm | Description | Applications |
|------------|--------------|---------------|
| **Breadth-First Search (BFS)** | Explores all nodes level by level. | Pathfinding, network traversal |
| **Depth-First Search (DFS)** | Explores as deep as possible before backtracking. | Maze solving, backtracking |
| **Depth-Limited Search (DLS)** | DFS with a depth cutoff limit. | Game trees with limited depth |
| **Iterative Deepening Search (IDS)** | Combines BFS & DFS; increases depth gradually. | Optimal pathfinding |
| **Best-First Search** | Expands most promising nodes based on heuristic. | Route planning, A* Search |
| **Beam Search** | Similar to Best-First but with limited width. | Machine translation, speech recognition |
| **Bidirectional Search** | Searches from both start & goal nodes simultaneously. | Shortest path problems |
| **Hill Climbing** | Chooses moves that increase heuristic value. | Optimization problems |
| **Minimax Algorithm** | Predicts opponent’s move and selects best response. | Game AI |
| **Alpha-Beta Pruning** | Optimizes Minimax by skipping useless branches. | Game tree search |

---

## 🧩 Applications

- Game AI (Tic Tac Toe, Chess, Connect Four)
- Decision Making Systems
- Robotics Pathfinding
- Puzzle Solvers (8-puzzle, Sudoku)
- Optimization and Planning Problems

---

## 📊 Complexity Analysis

| Algorithm | Time Complexity | Space Complexity |
|------------|----------------|------------------|
| BFS | O(b^d) | O(b^d) |
| DFS | O(b^m) | O(bm) |
| DLS | O(b^l) | O(bl) |
| IDS | O(b^d) | O(bd) |
| Best-First | O(b^d) | O(b^d) |
| Beam Search | O(b × k) | O(b × k) |
| Bidirectional Search | O(b^(d/2)) | O(b^(d/2)) |
| Hill Climbing | O(b^m) | O(bm) |
| Minimax | O(b^m) | O(bm) |
| Alpha-Beta Pruning | O(b^(m/2)) | O(bm) |

Where:  
- **b** = branching factor  
- **d** = depth of goal node  
- **m** = maximum depth of tree  
- **k** = beam width  

---

## 🧰 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/AI-Game-Collection.git
cd AI-Game-Collection

# Install required libraries
pip install pygame
