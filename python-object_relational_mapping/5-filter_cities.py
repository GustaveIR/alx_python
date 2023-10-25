import MySQLdb
import sys

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
        city_names = sorted(city_names)

        # Print the city names
        print(", ".join(city_names))

    # close cursor
    cur.close()

    # close database
    database.close()

if __name__ == '__main__':
    main()