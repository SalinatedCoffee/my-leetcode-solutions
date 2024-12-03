## 1280. (E) Students and Examinations

### `solution.sql`
We are given the tables `Students`, `Subjects`, and `Examinations`, each having the schema  

```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| student_name  | varchar |
+---------------+---------+
Primary key = student_id
```

```text
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| subject_name | varchar |
+--------------+---------+
Primary key: subject_name
```

```text
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| student_id   | int     |
| subject_name | varchar |
+--------------+---------+
```

Our task is to write a query that counts the number of times a student has attended an examination for each subject. The result should follow  the following format:  

```text
+------------+--------------+--------------+----------------+
| student_id | student_name | subject_name | attended_exams |
+------------+--------------+--------------+----------------+
```

First off, we know that we would want to count the student's number of attendences for each and every subject that exists. This tells us that we should first perform a cross join between the `Students` and `Subjects` table. Looking at the `Examinations` table we notice that it does not have a primary key, which means that it may contain duplicate rows - one for every time a student has taken an exam for a specific subject. It may also be the case that a student has not taken an exam for a subject at all. To account for both cases, we can perform a left outer join on the table resulting from the previous cross join. Since we want to join rows from the `Examinations` table to rows in the cross join table that match the student *and* the subject, we join the two tables on the `Students.student_id`, `Examinations.student_id` columns and the `Subjects.subject_name`, `Examinations.subject_name` columns. The next step is to count the number of rows for each subject per student, which can be done with the `COUNT()` fuction in conjunction with the `GROUP BY` clause. As we want counts for each subject for each student, we need to group the rows by `Students.student_id` *and* `Subjects.subject_name`. We also need to remember to call `COUNT` on *any* column from the `Examinations` table, since we want to include a count of `0` for subjects where a specific student has not taken an exam for. Finally, we sort the resulting rows as requested by the problem using the `ORDER BY` clause.  

#### Conclusion
\<Content\>  
  

