## 1148. (E) Article Views I

### `solution.sql`
Given the table `Views`, which has the schema  

```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
Private key: none
```

We are asked to return the list of unique `author_id`s of authors that have read their own articles in ascending order in the following format:    

```text
+------+
| id   |
+------+
```

Because `Views` does not have a primary key, the table may contain duplicate rows. Since we want the list of unique `author_id`s, we would want to use the `DISTINCT` keyword in our `SELECT` clause. We also need to give the `author_id` column an alias in the `SELECT` clause, as the output format asks us to return this column with the name `id` instead of `author_id`. A row represents an author reading their own article if the values of `author_id` and `viewer_id` are equal, and this can be trivially implemented by adding an equality expression in the `WHERE` clause. Finally, we sort the resulting rows by adding an `ORDER BY` clause to the query.  
  
