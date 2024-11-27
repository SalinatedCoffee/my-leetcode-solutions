SELECT
  machine_id,
  ROUND(SUM(CASE WHEN activity_type='start' THEN -1*timestamp ELSE timestamp END) /
    (SELECT COUNT(DISTINCT process_id)), 3) processing_time
FROM Activity
GROUP BY machine_id;

