import pandas

def get_coach(conn):
 return pandas.read_sql(
 '''
  SELECT * FROM coach
 ''', conn)

def get_client(conn):
 return pandas.read_sql(
 '''
  SELECT * FROM client
  ORDER BY client_full_name
 ''', conn)

def get_free_record_all_coach(conn, date_start, date_end):
 return pandas.read_sql(
 f'''
  SELECT coach_full_name, coach_id, record_date, record_time
  FROM coach INNER JOIN schedule USING (coach_id)
  INNER JOIN schedule_date USING (schedule_id)
  LEFT OUTER JOIN record USING (schedule_date_id)
  LEFT OUTER JOIN service USING (service_id)
  WHERE record.service_id IS NULL AND record_date >= '{date_start}' AND record_date <= '{date_end}'
 ''', conn)

def get_free_record(conn, coach_id, date_start, date_end):
 return pandas.read_sql(
 f'''
  SELECT coach_full_name, coach_id, record_date, record_time
  FROM coach INNER JOIN schedule USING (coach_id)
  INNER JOIN schedule_date USING (schedule_id)
  LEFT OUTER JOIN record USING (schedule_date_id)
  LEFT OUTER JOIN service USING (service_id)
  WHERE record.service_id IS NULL AND record_date >= '{date_start}' AND record_date <= '{date_end}' AND coach_id == {coach_id}
 ''', conn)

def execute_query(connection, query):
 cursor = connection.execute(query)
 try:
  cursor.execute(query)
  connection.commit()
  print("Query executed successfuly")
 except Error as e:
  print(f"The error '{e}' occured")


def add_record(conn, client_id, record_date, record_time, service_name, coach):
 added = f'''
   UPDATE record SET service_id = (
   SELECT service_id
   FROM service INNER JOIN client USING(client_id)
   WHERE client_id == {client_id} and service_name == '{service_name}'
  )
  WHERE record_time == '{record_time}' AND schedule_date_id == (
   SELECT schedule_date_id 
   FROM coach INNER JOIN schedule USING (coach_id)
   INNER JOIN schedule_date USING (schedule_id)
   INNER JOIN record USING (schedule_date_id)
   WHERE record_date == '{record_date}' AND record_time == '{record_time}' AND coach_id == {coach}
   LIMIT 1)
 '''
 execute_query(conn, added)
