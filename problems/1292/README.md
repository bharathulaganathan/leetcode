# [1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold](https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/)

![Meduim](https://img.shields.io/badge/Medium%20-ffb700)

Given a `m x n` matrix `mat` and an integer `threshold`, return *the maximum side-length of a square with a sum less than or equal to* `threshold` *or return* `0` *if there is no such square*.

<br/>

**Example 1:**

![](extras/e1.png)

> **Input:** mat = \[[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4  
> **Output:** 2  
> **Explaination:** The maximum side length of square with sum less than 4 is 2 as shown.  

**Example 2:**

> **Input:** mat = \[[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1  
> **Output:** 0  

<br/>

<!-- Example -->
**Constraints:**

* `m == mat.length`
* `n == mat[i].length`
* `1 <= m, n <= 300`
* `0 <= mat[i][j] <= 10⁴`
* `0 <= threshold <= 10⁵`