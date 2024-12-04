# AOC 2024
A repo containing my code for [AOC 2024](https://adventofcode.com/2024/about), created by the wonderful [Eric Wastl](https://was.tl/).

This is my 2nd year participating, and I look forward to solving the code challenges this year! Unfortunately, I will not be tracking leaderboard position or solve timings, partly due to the fact that I will be overseas (and unable to complete the problems daily) for a large chunk of December and also partly because I do not want to rush myself.

> [!IMPORTANT]
> Do check out my [AOC 2023](https://github.com/KrashKart/aoc-2023) repo!

# Challenge
As a challenge, I plan to use different languages to solve the problems (instead of only Python in AOC 2023). The languages I plan to use are:
* Python (duh)
* Java
* Ruby
* C++

And the languages I plan to pick up are:
* Rust
* ??? idk
* JavaScript

# Days
> [!NOTE]
>  * A completion of 2 stars will be noted as (**) and 1 as (*).
>  * The programming language(s) used for each day will be displayed in *italics*.
>  * Day names contain clickable links to the AOC problems.

1. [**Historian Hysteria**](https://adventofcode.com/2024/day/1) in *Java* and *Python* (**)
    * Part 1: A list difference problem -- compare the elements in 2 lists (arranged in ascending order) and find the sum of all their differences. (Trivial)
    * Part 2: A variation where for each unique number in list A, `A[i]`, the sum of `A[i] * freq(A[i] in B)` had to be found. (Trivial)
2. [**Red-Nosed Reports**](https://adventofcode.com/2024/day/2) in *Python* (**)
    * Part 1: Given a list of sequences of numbers, determine how many sequences are "safe". Safe sequences must:
        * Contain consecutive elements that differ by not more than 3 and not less than 1
        * Contain elements in either ascending or descending order
    * Part 2: Same as Part 1, except removal of any one element is permitted for a sequence to be safe.
        * I had to brute force removing every element in the sequence to determine if this critera could be satisfied.
        * As the length of the sequences was quite small, I felt that this was a reasonably fast way to compute the solution.
    * I learnt the `zip(arr, arr[1:])` trick (in *Python*) for quickly comparing two consecutive elements in an array for all elements
3. [**Mull it Over**](https://adventofcode.com/2024/day/3) in *Python* and *Go* (**)
    * Part 1: Typical regex question, parsing patterns of `mul(x,y)` and evaluating the sum of all `x * y` in long strings. (Trivial)
    * Part 2: Part 1 but with extra parsing of `do()` and `don't()` terms required, which enabled or disabled the `mul(x,y)` operations and affected the sum. (Trivial)
    * Testing my regex I see!
4. [**Ceres Search**](https://adventofcode.com/2024/day/3) in *Python* and *Ruby* (**)
    * Part 1: A word search problem, having to find `XMAS` in a word search. Would say trivial but honestly I couldn't think of anything else other than brute-force.
    * Part 2: Same as Part 1 except `MAS` and `SAM` arranged in an "X" had to be found (see the problem I'm bad at explaining this one). Again trivial but brute-forced.