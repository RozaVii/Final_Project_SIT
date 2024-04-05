import pandas

def get_coach(conn):
 return pandas.read_sql(
 '''
  SELECT * FROM coach
 ''', conn)

def get_coach_record(conn, coach_id, date_start, date_end):
 # записи на тренировку
 return pandas.read_sql('''
  SELECT schedule_date AS Date, record_time AS Time, service_name AS Service name, price AS Price
  FROM coach INNER JOIN schedule USING (coach_id)
  INNER JOIN schedule_date USING (schedule_id)
  INNER JOIN record USING (schedule_date_id)
  INNER JOIN service USING (service_id AND record_date >= :date_s AND record_date < :date_e
  ORDER BY record_date, record_time;
 ''', conn, params={"id": coach_id, "date_s": date_start, "date_e": date_end})