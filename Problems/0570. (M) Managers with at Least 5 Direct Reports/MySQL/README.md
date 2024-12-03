## 570. (M) Managers with at Least 5 Direct Reports

### `solution.sql`
Given the `Employee` table having the schema  

```text
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
Primary key: id
```

where an employee cannot be their own manager, we are asked to return the name of employees who have at least 5 direct reports. We can immediately see that we would want to join the `Employee` table on itself, using the columns `id` and `managerId`. Because we ultimately want employees with at least 5 direct reports, we do not care about employees with 0 direct reports, eliminating the need for an outer join. Once the join is performed, we simply group the rows by the manager table's `id`s, using the `COUNT` function in the `HAVING` clause to filter out managers that have less than 5 direct reports.  


### `solution_2.sql`
A different approach involves utilizing a subquery and the `IN` keyword instead of a join. If we group rows using the `managerId` column, we can count the number of rows in each group using the `COUNT` function, which allows us to retrieve a list of `managerId`s that appear in at least 5 rows in the `Employee` table. Once this table is fetched using the subquery, we can use the `IN` keyword to retrieve the list of employee names that have an `id` that appears in the subquery result.  