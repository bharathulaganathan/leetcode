# [3634. Minimum Removals to Balance Array](https://leetcode.com/problems/minimum-removals-to-balance-array/)

![Meduim](https://img.shields.io/badge/Medium%20-ffb700)

You are given an integer array `nums` and an integer `k`.

An array is considered **balanced** if the value of its **maximum** element is **at most** `k` times the **minimum** element.

You may remove **any** number of elements from `nums​​​​​​​` without making it **empty**.

Return the **minimum** number of elements to remove so that the remaining array is balanced.

**Note:** An array of size 1 is considered balanced as its maximum and minimum are equal, and the condition always holds true.

<br/>

**Example 1:**

> **Input:** nums = [2,1,5], k = 2  
> **Output:** 1  
> **Explaination:**  
> * Remove `nums[2] = 5` to get `nums = [2, 1]`.  
> * Now `max = 2`, `min = 1` and `max <= min * k` as `2 <= 1 * 2`. Thus, the answer is 1.  

**Example 2:**

> **Input:** nums = [1,6,2,9], k = 3  
> **Output:** 2  
> **Explaination:**  
> * Remove `nums[0] = 1` and `nums[3] = 9` to get `nums = [6, 2]`.  
> * Now `max = 6`, `min = 2` and `max <= min * k` as `6 <= 2 * 3`. Thus, the answer is 2.  

**Example 3:**

> **Input:** nums = [4,6], k = 2  
> **Output:** 0  
> **Explaination:**  
> * Since `nums` is already balanced as `6 <= 4 * 2`, no elements need to be removed.  

<br/>

**Constraints:**

* `1 <= nums.length <= 10⁵`
* `1 <= nums[i] <= 10⁹`
* `1 <= k <= 10⁵`
