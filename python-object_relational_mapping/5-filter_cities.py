import MySQLdb
import sys


def get_cities_by_state(state_name):
    """Returns a list of all cities in the given state, sorted in ascending order by their ID."""

    database = MySQLdb.connect(host='localhost', user='mysql_username', passwd='mysql_password', db='hbtn_0e_4_usa', port=3306)
    cursor = database.cursor()

    # Use a parameterized query to avoid SQL injection.
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = ?
        ORDER BY cities.id ASC
    """

    cursor.execute(query, (state_name,))
    results = cursor.fetchall()

    # Close the cursor and database connection.
    cursor.close()
    database.close()

    # Return the list of city names.
    city_names = [row[0] for row in results]
    return city_names


def main():
    # Get the state name from the command line arguments.
    state_name = sys.argv[4]

    # Get the list of cities in the given state.
    city_names = get_cities_by_state(state_name)

    # Print the list of city names, sorted in ascending order.
    for city_name in city_names:
        print(city_name)


if __name__ == '__main__':
    main()
import MySQLdb
import sys


def get_cities_by_state(state_name):
    """Returns a list of all cities in the given state, sorted in ascending order by their ID."""

    database = MySQLdb.connect(host='localhost', user='mysql_username', passwd='mysql_password', db='hbtn_0e_4_usa', port=3306)
    cursor = database.cursor()

    # Use a parameterized query to avoid SQL injection.
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = ?
        ORDER BY cities.id ASC
    """

    cursor.execute(query, (state_name,))
    results = cursor.fetchall()

    # Close the cursor and database connection.
    cursor.close()
    database.close()

    # Return the list of city names.
    city_names = [row[0] for row in results]
    return city_names


def main():
    # Get the state name from the command line arguments.
    state_name = sys.argv[4]

    # Get the list of cities in the given state.
    city_names = get_cities_by_state(state_name)

    # Print the list of city names, sorted in ascending order.
    for city_name in city_names:
        print(city_name)


if __name__ == '__main__':
    main()
