# AOC 2024 :santa:
A repo containing my code for [AOC 2024](https://adventofcode.com/2024/about), created by the wonderful [Eric Wastl](https://was.tl/).

This is my 2nd year participating, and I look forward to solving the code challenges this year! Unfortunately, I will not be tracking leaderboard position or solve timings, partly due to the fact that I will be overseas (and unable to complete the problems daily) for a large chunk of December and also partly because I do not want to rush myself.

> [!IMPORTANT]
> Do check out my [AOC 2023](https://github.com/KrashKart/aoc-2023) repo!

# Challenge
As a challenge, I plan to use different languages to solve the problems (instead of only Python in AOC 2023). The languages I plan to use are:

- [x] Python (duh)
- [x] Java
- [x] Ruby
- [ ] C++

And the languages I plan to pick up are:

- [ ] Rust
- [ ] JavaScript
- [x] Go
- [x] Holy C (unfortunately could not get this to work because Strings are weird in HolyC)
- [ ] ??? idk :sweat_smile:

# Days
> [!NOTE]
>  * A completion of 2 stars will be noted as ( :star: :star: ) and 1 as ( :star: ).
>  * The programming language(s) used for each day will be displayed in *italics*.
>  * Day names contain clickable links to the AOC problems.

1. [**Historian Hysteria**](https://adventofcode.com/2024/day/1), *Python* and *Java* ( :star: :star: )
    * Part 1: A list difference problem -- compare the elements in 2 lists (arranged in ascending order) and find the sum of all their differences. (Trivial)
    * Part 2: A variation where for each unique number in list A, `A[i]`, the sum of `A[i] * freq(A[i] in B)` had to be found. (Trivial)
2. [**Red-Nosed Reports**](https://adventofcode.com/2024/day/2), *Python* and *Holy C* ( :star: :star: )
    * Part 1: Given a list of sequences of numbers, determine how many sequences are "safe". Safe sequences must either only ascend or descend and consecutive numbers must differ by `1 <= diff <= 3` (trivial)
    * Part 2: Same as Part 1, except removal of any one element is permitted for a sequence to be safe.
        * I had to brute force removing every element in the sequence to determine if this critera could be satisfied. Not elegant but works due to the small sequence length
    * I learnt the `zip(arr, arr[1:])` trick (in *Python*) for quickly comparing two consecutive elements in an array for all elements
3. [**Mull it Over**](https://adventofcode.com/2024/day/3), *Python* and *Go* ( :star: :star: )
    * Part 1: Typical regex question, parsing patterns of `mul(x,y)` and evaluating the sum of all `x * y` in long strings. (Trivial)
    * Part 2: Part 1 but with extra parsing of `do()` and `don't()` terms required, which enabled or disabled the `mul(x,y)` operations and affected the sum. (Trivial)
4. [**Ceres Search**](https://adventofcode.com/2024/day/4), *Python* and *Ruby* ( :star: :star: )
    * Part 1: A word search problem, having to find `XMAS` in a word search. Would say trivial but honestly I couldn't think of anything else other than brute-force dynamic programming.
    * Part 2: Same as Part 1 except `MAS` and `SAM` arranged in an "X" had to be found (see the problem I'm bad at explaining this one). Again trivial but brute-forced.
    * Glad to say the lessons learnt in AOC 2023 paid off. Used the `i + di, j + dj` method quite effectively here.
5. [**Print Queue**](https://adventofcode.com/2024/day/5), *Python* and *Java* ( :star: :star: )
    * Part 1: A very unique problem that required us to check the validity of sequences of numbers as defined by a ruleset (again visit the problem website, I'm bad at explaining this concisely). I was surprised at how unorthodox it was (but to be fair AOC 2023 was worse in this regard). Not trivial and enjoyed it!
    * Part 2: Same thing, except we have to correct the invalid sequences.
    * My initial solution worked but was too long, then I realised I could just use a custom comparator and check if the sequence was sorted, which reduced my solution length considerably. My first functools-based solution! 
6. [**Guard Gallivant**](https://adventofcode.com/2024/day/6), *Python* and *Ruby* ( :star: :star: )
    * Part 1: A typical traversal problem! Trivial but made many careless mistakes.
    * Part 2: Another typical traversal problem but with the choice to add an obstacle anywhere to induce a cyclic path. Brute-forced (which was ugly) but still trivial.
    * I got so pissed that I made a `gridutils.py` file that contained `Grid`, `Pos` and `Direction` classes, but found out that the runtime increased from 13s without parallelism ([without `gridutils`](./day_06/day_06_withoutGrid.py])) to 3.7 mins ([with `gridutils`](./day_06/day_06_withGrid.py))!!! 
    * Solution for part 2 was optimised by checking the grid positions involved in the path of the guard
7. [**Bridge Repair**](https://adventofcode.com/2024/day/7), *Python* and *Go* ( :star: :star: )
    * Part 1: Typical DP problem, simply try all combinations of `+` and `*` for all values.
    * Part 2: Surprisingly easy, DP again with an additional option of concatenation
    * :tada: First sub 20 min!!
8. [**Resonant Collinearity**](https://adventofcode.com/2024/day/8), *Python* ( :star: :star: )
    * Part 1: Interesting collinearity problem; to count outer collinear points, given a set of pairs `(x1, y1)` and `(x2, y2)`, at distance `(abs(x1 - x2), abs(y1 - y2))` from the points. Trivial but I messed up my vector math :cry:
    * Part 2: Same as part 1 but for all collinear points at intervals of `(abs(x1 - x2), abs(y1 - y2))` from the points. Trivial, but had trouble with combining parts 1 and 2 due to off by 2 errors (the original 2 points counted as 2 collinear points)
