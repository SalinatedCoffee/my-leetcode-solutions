## 1378. (E) Replace Employee ID With The Unique Identifier

### `solution.sql`
We are given the tables `Employees` and `EmployeeUNI`, with `Employees` having the schema  

```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
Primary key: id
```

and `EmployeeUNI`  

```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| unique_id     | int     |
+---------------+---------+
Primary key: (id, unique_id)
```

Our task is to write a query that shows the `unique_id` for each user in `Employees` in the following format:  

```text
+-----------+----------+
| unique_id | name     |
+-----------+----------+
```

Because `EmployeeUNI` has a composite key as its PK which includes the `unique_id` column, we know that `unique_id` is not nullable. Thus, a user will not have a unique id if the row in `Employees` corresponding to the user does not have a corresponding row in `EmployeeUNI`. Since we are asked to include users that are missing a unique id in the result, we want to perform an outer join on the table of employees on the `id` column of both tables.  

#### Conclusion
The number of rows are not specified for both tables, meaning that the order of the join does not matter as long as we specify the correct table for the outer join.  
  

