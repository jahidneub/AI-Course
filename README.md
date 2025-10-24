<!-- ──────────────────────────────────────────────── -->
<h1 align="center">🤖 Artificial Intelligence Course Project</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/AI-Algorithms-orange?logo=openai&logoColor=white" alt="AI Badge"/>
  <img src="https://img.shields.io/badge/Status-Completed-success?style=flat-square" alt="Status Badge"/>
  <img src="https://img.shields.io/github/license/fahimahaque01/Ai-Course?color=green" alt="License Badge"/>
</p>

<p align="center">
  <b>✨ A course project showcasing key Artificial Intelligence algorithms with real-world game implementations.</b><br>
  <i>Developed under the supervision of North East University Bangladesh.</i>
</p>

---

## 🎯 Course Purpose
This course was designed to provide a deep understanding of **Artificial Intelligence search algorithms** and **decision-making techniques**.  
It focused on both theoretical learning and practical implementation through structured lessons and projects.

---

## 📘 What I Learned
- Implemented various AI search algorithms  
- Understood key concepts: **A\***, **AO\***, **Minimax**, **Alpha-Beta Pruning**  
- Built multiple mini-projects using AI search strategies  
- Enhanced problem-solving and programming skills through coding exercises  

---

## ⏱️ Course Duration
**🕒 Total Duration:** 6 Months

---

## 👨‍🏫 Supervisor
**Course Conducted By:** *Razorshi Prozzwal Talukder*  
**Supervised By:** *North East University Bangladesh*

---

## ⚙️ Algorithms Overview

| Algorithm | Description |
|------------|-------------|
| **A\*** | Uses cost + heuristic to find the shortest path |
| **AO\*** | Solves AND/OR graphs using best-first search |
| **Beam Search** | Explores only top-k best nodes at each level |
| **Bidirectional Search** | Searches simultaneously from start and goal |
| **Alpha-Beta Pruning** | Optimizes Minimax by pruning irrelevant branches |
| **Minimax** | Decision rule for minimizing possible losses |
| **BFS** | Explores nodes level-by-level |
| **DFS** | Explores as deep as possible before backtracking |

---

## 🚀 Applications of Algorithms

| Algorithm | Real-world Applications |
|------------|-------------------------|
| **A\*** | GPS Navigation, Pathfinding in Games |
| **AO\*** | Problem Solving in Logic Systems |
| **Beam Search** | Natural Language Processing (e.g., Translation) |
| **Bidirectional Search** | Puzzle Solving, Network Routing |
| **Alpha-Beta Pruning** | Chess, Tic-Tac-Toe, Strategy Games |
| **Minimax** | Competitive AI Decision Making |
| **BFS** | Finding Shortest Path in Unweighted Graphs |
| **DFS** | Maze Solving, Topological Sorting |

---

## 🧠 AI Game Implementations

Each of the following mini-projects demonstrates how AI algorithms work in real-world decision-making and problem-solving.

---
###  📚 Libraries Required: pygame, numpy

## ♟️ **Chess AI**

**Algorithm Used:** Alpha-Beta Pruning  
**Libraries Required:** `pygame`, `numpy`

### 🕹️ How to Play:
1. Launch the game using the command below:  
   ```bash
   python chess_ai.py

2. Player (White) moves first.
3. AI (Black) responds with an optimal move using pruning.
4. Click on any piece to move it.
5. The AI will calculate and respond intelligently.

   
-----

## ❌⭕ Tic-Tac-Toe (Minimax Algorithm)

### Algorithm Used: Minimax

### Libraries Required: tkinter

### 🕹️ How to Run:
	```bash
	python tictactoe.py	

## 🎮 How to Play:

- A simple GUI will appear.
- Click any cell to make your move.
- The AI instantly responds with its turn.
- The game ends when someone wins 🏆 or the board is full.

 ------

## 🧩 Number Caching (Puzzle Solver)

	### Algorithm Used: A* Search
	### Libraries Required: heapq, numpy
	
## ⚙️ How to Run:

		python puzzle_solver.py

## 🧠 How to Play:

1. Open the script and set your initial and goal states.
2. The algorithm will calculate the optimal steps to reach the goal.
3. Watch the step-by-step output directly in your terminal.


## 🧮 Algorithm Performance Summary

## 📊 Algorithm Time & Space Complexity

| 🧠 Algorithm | ⏱️ Time Complexity | 💾 Space Complexity | 📘 Notes |
|:-------------|:------------------:|:------------------:|:--------|
| **A\*** | `O(b^d)` | `O(b^d)` | b = branching factor, d = goal depth |
| **AO\*** | Exponential (worst) | Exponential (worst) | Depends on graph structure |
| **Beam Search** | `O(b × k)` | `O(b × k)` | k = beam width |
| **Bidirectional Search** | `O(b^(d/2))` | `O(b^(d/2))` | Efficient when goal depth known |
| **Alpha-Beta Pruning** | `O(b^d)` / `O(b^(d/2))` | `O(b × d)` | Best-case with perfect pruning |
| **Minimax** | `O(b^d)` | `O(b × d)` | Used in decision-making games |
| **BFS** | `O(b^d)` | `O(b^d)` | Complete but memory-heavy |
| **DFS** | `O(b^m)` | `O(b × m)` | m = max depth |



	
