## 1683. (E) Invalid Tweets

### `solution.sql`
Given the table `Tweets` which has the schema  

```text
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| tweet_id       | int     |
| content        | varchar |
+----------------+---------+
```

we are asked to return the list of `tweet_id`s of invalid tweets. A tweet is invalid if its contents are strictly less than 15 characters long.  
This problem can be trivially solved by using MySQL's `LENGTH()` function in the `WHERE` clause, which takes a string as an argument and returns its length.  

