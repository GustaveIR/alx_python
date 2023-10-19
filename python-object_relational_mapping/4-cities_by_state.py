import MySQLdb

def filter_cities_by_state(username, password, database, state_name):
  """Filters all cities in a given state.

  Args:
    username: The MySQL username.
    password: The MySQL password.
    database: The name of the MySQL database.
    state_name: The name of the state to filter by.

  Returns:
    A list of all cities in the given state, sorted by ID.
  """

  db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)
  cursor = db.cursor()

  # The SQL query to filter the cities by state and sort by ID.
  query = """
    SELECT name
    FROM cities
    WHERE state_id = (SELECT id FROM states WHERE name = %s)
    ORDER BY id ASC;
  """

  # Execute the query with the given state name as the parameter.
  cursor.execute(query, (state_name,))

  # Get the results of the query.
  results = cursor.fetchall()

  # Close the cursor and database connection.
  cursor.close()
  db.close()

  # Return the list of cities.
  return [city[0] for city in results]


def main():
  """The main function."""

  # Get the database credentials and state name from the user.
  username = input('Enter MySQL username: ')
  password = input('Enter MySQL password: ')
  database = input('Enter MySQL database name: ')
  state_name = input('Enter state name: ')

  # Filter the cities by state and display the results.
  cities = filter_cities_by_state(username, password, database, state_name)
  print(', '.join(cities))


if __name__ == '__main__':
  main()
