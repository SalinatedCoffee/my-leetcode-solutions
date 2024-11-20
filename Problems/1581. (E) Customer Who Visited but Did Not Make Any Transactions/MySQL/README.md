## 1581. (E) Customer Who Visited but Did Not Make Any Transactions

### `solution.sql`
Given the table `Visits`, which has the schema  

```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| visit_id    | int     |
| customer_id | int     |
+-------------+---------+
Primary key: visit_id
```

and the table `Transactions`, which has the schema  

```text
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| transaction_id | int     |
| visit_id       | int     |
| amount         | int     |
+----------------+---------+
Primary key: transaction_id
```

we are asked to write a query that returns a list of customers who have visited but did not complete a transaction, along with their number of visits. The result should be in the following format:  

```text
+-------------+----------------+
| customer_id | count_no_trans |
+-------------+----------------+
```

There are multiple ways to approach this problem. In this solution, we will first perform an outer join to join the two tables on the `visit_id` column, including rows in `Visits` that do not have corresponding rows in `Tables`. From the resulting rows, we want to only include those that *do not* have a transaction attached to them. Because we have performed an outer join on the `Visits` table, the rows we want will have a value of `null` for the columns taken from the `Transactions` table. We can extract these rows by using the expression `Transactions.visit_id IS NULL` in the `WHERE` clause. Finally, we are asked to return the number of visits for each customer ID. We first group the rows by the `customer_id` column using the `GROUP BY` clause, after which we count the number of rows(visits) in each group by using the aggregate function `COUNT(*)` in the `SELECT` clause.  

#### Conclusion
We can also use the `NOT IN` or `EXISTS` operators to achieve the same result, with varying performance.  
  

