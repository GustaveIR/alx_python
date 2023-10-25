import MySQLdb
import sys

def sort_city_names(city_names):
  """Sorts city names alphabetically, but also groups together city names from the same state."""

  # Create a dictionary to store the city names grouped by state
  city_names_by_state = {}
  for city_name in city_names:
    # Check if the city name contains a comma
    if "," in city_name:
      state_name = city_name.split(",")[1]
    else:
      state_name = None

    # Add the city name to the dictionary, grouped by state
    if state_name not in city_names_by_state:
      city_names_by_state[state_name] = []
    city_names_by_state[state_name].append(city_name)

  # Concatenate the city names from each state into a single list
  sorted_city_names = []
  for state_name, city_names in city_names_by_state.items():
    sorted_city_names += city_names

  # Sort the city names alphabetically
  sorted_city_names.sort()

  return sorted_city_names

def main():
    database_name = sys.argv[3]
    username = sys.argv[1]
    password = sys.argv[2]
    statename = sys.argv[4]

    # Connecting to database in the localhost
    database = MySQLdb.connect(host='localhost', user=username, passwd=password, db=database_name, port=3306)

    # create a cursor
    cur = database.cursor()

    # using a parameterized query
    query = "SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE %s = states.name ORDER BY cities.id ASC"

    # Execute the query with name searched as parameter
    cur.execute(query, (statename,))

    # obtaining results
    results = cur.fetchall()

    # If there are no results, print an empty string
    if not results:
        print()
    else:
        city_names = ", ".join(row[0] for row in results)

        # Sort the city names alphabetically
        city_names = sort_city_names(city_names.split(", "))

        # Print the city names
        print(", ".join(city_names))

    # close cursor
    cur.close()

    # close database
    database.close()

if __name__ == '__main__':
    main()