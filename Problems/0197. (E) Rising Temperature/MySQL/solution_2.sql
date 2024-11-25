SELECT id
FROM (
  SELECT
    id, recordDate, temperature,
    -- sort by recordDate column, and access potential 'yesterday row'
    -- adding the row's temperature and date to each row
    LAG(temperature, 1) OVER (ORDER BY recordDate) PrevTemperature,
    LAG(recordDate, 1) OVER (ORDER BY recordDate) PrevRecordDate
  FROM
    Weather
  ) PrevWeatherData
WHERE temperature > PrevTemperature AND
  -- check if the two rows actually are exactly 1 day apart
  recordDate = DATE_ADD(PrevRecordDate, INTERVAL 1 DAY);

