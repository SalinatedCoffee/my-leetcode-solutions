## 197. (E) Rising Temperature

### `solution.sql`
Given the `Weather` table with the schema  

```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
Primary key: id
All values in the `recordDate` columns are guaranteed to be unique.
```

we are asked to write a query that returns the table of rows that have a higher temperature than the previous day. The most straightforward method would be to identify the row that has a difference of 1 day in the `recordDate` column, and only select rows where the temperature of the later day is higher than the previous day. This can be achieved by joining the `Weather` table on itself using the `DATEDIFF()` function. One thing to note here is that the result of the `DATEDIFF()` function depends on the order of its input - because the second parameter is subtracted from the first parameter, the order of the arguments used here would affect the expression used in the `WHERE` clause that follows.  


### `solution_2.sql`
A more advanced solution involves the use of the window function `LAG`.  Because it is guaranteed that the `recordDate` column only contains unique values, we could easliy access the row potentially corresponding to the previous day of another row if we were to sort the rows by the `recordDate` column. Of course, the `recordDate` column is not guaranteed to be 'continuous'. That is, it may be the case that a gap longer than 1 day exists between two adjacent rows after sorting by `recordDate`. To handle this situation, we check the date difference between rows in the `WHILE` clause by using the `DATE_ADD()` function.  


