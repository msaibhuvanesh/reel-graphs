
## 📌 Project Overview

This project focuses on implementing classic graph algorithms using real-world data extracted from the IMDb dataset. You will build a graph-based network of movie professionals (actors and directors), and implement BFS, DFS, Dijkstra’s, and Kosaraju’s algorithms to traverse and analyze the graph.

## 🗂️ File Structure

- `graph_creation.py`  
  Contains code to build:
  - Title dictionary: `{nconst: [primaryTitles]}`
  - Profession dictionary: `{nconst: profession}`
  - Graph structure with nodes and edges based on rules
  - MovieNetwork class with methods: `add_node()`, `add_edge()`, `create_graph()`

- `graph_algorithms.py`  
  Implements:
  - `bfs(graph, start_node, search_node=None)`
  - `dfs(graph, start_node, visited=set(), path=[], search_node=None)`
  - `dijkstra(graph, start_node, end_node)`
  - `kosaraju(graph)`

- `graph_testcases.py`  
  Provided testing script (DO NOT MODIFY). Run this to verify correctness.

- `imdb_network.csv`  
  Dataset file including:
  - `tconst` – Unique ID for movies  
  - `nconst` – Unique ID for persons  
  - `primaryTitle`, `primaryName`, `primaryProfession`

## ✅ Test Cases Overview

| Test Case        | Description |
|------------------|-------------|
| `dictionary_test()` | Validates the correctness of the title and profession dictionaries |
| `movie_network_test()` | Verifies correct graph construction |
| `testcase_1_1()` to `1_3()` | Tests BFS traversal and search capabilities |
| `testcase_2_1()` to `2_3()` | Tests DFS traversal and search capabilities |
| `testcase_3()` | Verifies Dijkstra’s shortest path, distance, and hop count |
| `testcase_4()` | Validates strongly connected components from Kosaraju’s algorithm |

## 🧠 Key Implementation Rules

- **Edge Rules:**
  - Edge weight must be **> 2**
  - **Director ➝ Actor** edges are allowed; not the reverse
  - **Actor ↔ Actor** and **Director ↔ Director** edges must be **bi-directional**

- **Algorithm Requirements:**
  - BFS/DFS must restrict traversal within the start node's strongly connected component
  - Dijkstra returns: `[shortest_path_list, total_distance, hop_count]`
  - Kosaraju returns list of SCCs: `[[nconst1, nconst2, ...], [...], ...]`

## 🧪 How to Run

```bash
python graph_testcases.py
