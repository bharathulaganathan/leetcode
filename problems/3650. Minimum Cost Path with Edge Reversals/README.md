# [3650. Minimum Cost Path with Edge Reversals](https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/)

![Meduim](https://img.shields.io/badge/Medium%20-ffb700)

You are given a directed, weighted graph with `n` nodes labeled from 0 to `n - 1`, and an array `edges` where `edges[i] = [uᵢ, vᵢ, wᵢ]` represents a directed edge from node `uᵢ` to node `vᵢ` with cost `wᵢ`.

Each node `uᵢ` has a switch that can be used **at most once**: when you arrive at uᵢ and have not yet used its switch, you may activate it on one of its incoming edges `vᵢ → uᵢ` reverse that edge to `uᵢ → vᵢ` and **immediately** traverse it.

The reversal is only valid for that single move, and using a reversed edge costs `2 * wᵢ`.

Return the **minimum** total cost to travel from node 0 to node `n - 1`. If it is not possible, return -1.

<br/>

**Example 1:**

> **Input:** n = 4, edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]  
> **Output:** 5  
> **Explaination:**  
> ![](extras/e1drawio.png)
> * Use the path `0 → 1` (cost 3).  
> * At node 1 reverse the original edge `3 → 1` into `1 → 3` and traverse it at cost `2 * 1 = 2`.  
> * Total cost is `3 + 2 = 5`.  

**Example 2:**

> **Input:** n = 4, edges = [[0,2,1],[2,1,1],[1,3,1],[2,3,3]]  
> **Output:** 3  
> **Explaination:**  
> * No reversal is needed. Take the path `0 → 2` (cost 1), then `2 → 1` (cost 1), then `1 → 3` (cost 1).  
> * Total cost is `1 + 1 + 1 = 3`.

<br/>

**Constraints:**

* `2 <= n <= 5 * 10⁴`
* `1 <= edges.length <= 10⁵`
* `edges[i] = [uᵢ, vᵢ, wᵢ]`
* `0 <= uᵢ, vᵢ <= n - 1`
* `1 <= wᵢ <= 1000`
