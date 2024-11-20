## 1068. (E) Product Sales Analysis I

### `solution.sql`
The `Sales` table has the following schema:

```text
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+
Primary key: (sale_id, year)
```

and the `Product` table,  

```text
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
+--------------+---------+
Primary key: product_id
```

Our task is to write a query that returns the `product_name`, `year`, and `price` for each `sale_id` in the `Sales` table.  
As we are asked to include columns across multiple tables in our query, we would obviously want to join the two tables. Both tables contain the column `product_id`, which means that we should be joining the tables on the `product_id` column. Since both tables include the `product_id` column in their primary keys, both `product_id` columns are not nullable.  

