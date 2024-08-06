# My Leetcode Solutions

![LeetCode](https://img.shields.io/badge/LeetCode-black?style=for-the-badge&logo=leetcode)  
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) ![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)

> Leetcode a day keeps unemployment away.
>
> -A wise man on the internet

A repository of my solutions to LeetCode problems in various languages, complete with short explanatory writeups.  

**DISCLAIMER: While the code has been vetted by LeetCode's online judge (unless specified otherwise), my write-ups may contain wrong information. I am not and don't claim to be an expert on theoretical computer science and algorithms.**

## Usage

All problems can be found under the `Problems` directory, where each problem has its own directory and under it, directories for each language.  
The directory name for each problem is formatted as `number. (difficulty) title`, where `number` is the problem number in 4 digits(left padded with 0s if it is shorter), `difficulty` a single uppercase letter(`E` for easy, `M` for medium, `H` for hard), and `title` the title of the problem.  
Code that has `solution` as the prefix in its filename is guaranteed to be accepted by LeetCode's online judge(at the time of commit); implementations that fail will be named as such depending on why they were rejected.  
If you ever decide to fork this repo to use it for yourself, a new problem or language can be added with `new_problem.sh` by supplying it with the problem number, difficulty, problem title as a string, and language, in that order. A directory to the problem implementation will be created if it does not exist, and the template `README_template_body.md` will be copied into it, as well as an empty file corresponding to the specified language, if it is supported.  

### Example
To add the problem [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/description/) using JavaScript:  
`./new_problem.sh 32 H "Longest Valid Parentheses"`  
Which will create the directory `./Problems/0032. (H) Longest Valid Parentheses/JavaScript` containing files `README.md` and `solution.js`  
