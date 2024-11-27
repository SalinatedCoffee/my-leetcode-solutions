## 1661. (E) Average Time of Process per Machine

### `solution.sql`
Given the table `Activity`, which has the schema  

```text
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| machine_id     | int     |
| process_id     | int     |
| activity_type  | enum    |
| timestamp      | float   |
+----------------+---------+
Primary key: (machine_id, process_id, activity_type)
activity_type: ["start", "end"]
```

we are asked to write a query that computes the average time(up to 3 decimal places) it takes for each machine to complete a single process. The resulting table should follow the format  

```text
+------------+-----------------+
| machine_id | processing_time |
+------------+-----------------+
```

We first begin by breaking down the problem into smaller steps. To compute the average of the time it takes to complete each process for each machine, we first need to compute the time required to complete a single process, do this for all processes running on the same machine, divide the sum of all values by the number of unique `process_id`s, and the perform this for all machines. Instead of using conditionals to determine how the `timestamp` of a row should be used to compute the process completion time, we can use the `CASE` statement to modify the value of `timestamp` accordingly. If the row's `activity_type` is `"start"`, we simply multiply `timestamp` by `-1.0`. This way, we have the added benefit of not having to compute the processing time for each process - we can simply take the `timestamp` for all rows with the same `machine_id`, and add all of them together to get the total amount of time it took for the machine to complete all processes assigned to it(assuming the data is properly formed). We may then count the number of unique processes by using the `COUNT()` function, dividing the value from the previous step by the result before rounding the value to 3 decimal points. As we want to perform these steps for each `machine_id`, we should use the aggregate function `SUM()` along with the `GROUP BY` clause.  
  


### `solution_2.sql`
We may also solve this problem by using an implicit join to join the `Activity` table on itself, taking rows with the same `machine_id` and `process_id` and concatenating the row with `"start"` as the `activity_type` with that having `"end"` as the `activity_type`. The query would look something like this:  

```sql
SELECT
  *
FROM
  Activities a, Activities b 
WHERE
  a.machine_id = b.machine_id AND
  a.process_id = b.process_id AND
  a.activity_type = 'start' AND
  b.activity_type = 'end'
;
```

Now that we have the timestamps for the start and end times of each unique process in a single row, we want to compute the total time a machine took to process all processes to compute the average. Because in this case, a single row corresponds to a single unique process, we can use the aggregate function `AVG()` to compute the average time for each machine by combining it with the `GROUP BY` clause.  

