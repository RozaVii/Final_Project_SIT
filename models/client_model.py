import pandas

def get_client(conn):
 return pandas.read_sql(
 '''
  SELECT * FROM client
  ORDER BY client_full_name
 ''', conn)

def get_client_record(conn, client_id):
 # записи на тренировку клиентов
 return pandas.read_sql('''
  SELECT record_date AS Date, record_time AS Time, service_name AS Service name, price AS Price
  FROM coach INNER JOIN schedule USING (coach_id)
  INNER JOIN schedule_date USING (schedule_id)
  INNER JOIN record USING (schedule_date_id)
  INNER JOIN service USING (service_id)
  WHERE service.client_id = :id
  ORDER BY record_date, record_time;
 ''', conn, params={"id": client_id})

def get_date_record(conn,  date_record):
 # поиск записей на определенную дату
 return pandas.read_sql('''
  SELECT record_date AS Date, record_time AS Time, client_name AS Client name, phone_number AS 'Phone number', service_name AS Service name, coach_full_name AS 'Coach name'
  FROM coach INNER JOIN schedule USING (coach_id)
  INNER JOIN schedule_date USING (schedule_id)
  INNER JOIN record USING (schedule_date_id)
  INNER JOIN service USING (service_id)
  INNER JOIN client USING (client_id)
  WHERE record_date = :date
  ORDER BY record_time;
 ''', conn, params={"date": date_record})
