## 577. (E) Employee Bonus

### `solution.sql`
Given the `Employee` table with the schema  

```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| empId       | int     |
| name        | varchar |
| supervisor  | int     |
| salary      | int     |
+-------------+---------+
Primary key: empId
```

and the `Bonus` table with the schema  

```text
+-------------+------+
| Column Name | Type |
+-------------+------+
| empId       | int  |
| bonus       | int  |
+-------------+------+
Primary key: empId
```

we are asked to write a query that returns a list of names of employees that received a bonus of less than `1000`, in the following format:  

```text
+------+-------+
| name | bonus |
+------+-------+
```

We can easily solve this problem by joining the two tables on the `empId` column. As MySQL implicity performs an outer join when processing a `LEFT JOIN` clause, the resulting list of rows will include employees that do not have a corresponding row in the `Bonus` table. To filter the list of employees, we may simply use the `WHERE` clause, making sure to include rows that have `null` as the value for the `bonus` column.  

  

