import pandas

def execute_query(connection, query):
 cursor = connection.execute(query)
 try:
  cursor.execute(query)
  connection.commit()
  print("Query executed successfuly")
 except Error as e:
  print(f"The error '{e}' occured")


def add_service(conn, service_name, service_price):
 cursor = conn.cursor()
 cursor.execute(
 f'''
  INSERT INTO client (service_name, price)
  VALUES ('{service_name}', '{service_price}')
 ''')
 conn.commit()
 return cursor.lastrowid