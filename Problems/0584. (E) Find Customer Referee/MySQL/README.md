## 584. (E) Find Customer Referee

### `solution.py`
The `Customer` table has the following schema:  

```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| referee_id  | int     |
+-------------+---------+
Primary key: id
```
  
Our task is to write a query that returns a list of customer names that were not referred by the customer with id `2`. Because `referee_id` is nullable, we need to account for the case where `referee_id` is `null` when checking the `referee_id`.  

#### Conclusion
MySQL ['supposedly'](https://stackoverflow.com/questions/31098611/does-order-matter-in-mysql-for-short-circuiting-of-predicates) supports short circuiting when evaluating logical statements. If this is the case(which it very well may, considering the fact that our query only addresses a single table), the order of predicates in the `WHILE` clause may affect the performance of this query.  
  

