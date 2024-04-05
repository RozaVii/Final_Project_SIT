import pandas

def get_client(conn):
 return pandas.read_sql(
 '''
  SELECT * FROM client
 ''', conn)

def get_need_record(conn, client_id, date_record, time_record):
 return pandas.read_sql(
 '''
  SELECT record_date AS Date, record_time AS Time, client_name AS 'Client name'
  FROM schedule
  INNER JOIN schedule_date USING (schedule_id)
  INNER JOIN record USING (schedule_date_id)
  LEFT OUTER JOIN client USING (client_id)
  WHERE record_date == :date AND record_time == :time AND client_id == :id;
 ''', conn, params={"date": date_record, "time": time_record, "id":client_id})

def execute_query(connection, query):
 cursor = connection.execute(query)
 try:
  cursor.execute(query)
  connection.commit()
  print("Query executed successfuly")
 except Error as e:
  print(f"The error '{e}' occured")

def cancel_record1(conn, client_id, date_record, time_record):
 cancel = f'''
  UPDATE record SET service_id = NULL
  WHERE record_id == (
  SELECT record_id
  FROM coach INNER JOIN schedule USING (coach_id)
  INNER JOIN schedule_date USING (schedule_id)
  INNER JOIN record USING (schedule_date_id)
  INNER JOIN service USING (service_id)
  INNER JOIN client USING (client_id)
  WHERE client_id == {client_id} AND record_date == '{date_record}' AND record_time == '{time_record}'
  LIMIT 1
  )
 '''
 execute_query(conn, cancel)

