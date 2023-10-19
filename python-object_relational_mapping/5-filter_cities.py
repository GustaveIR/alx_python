#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host='localhost',
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
        )

        # Create a cursor object
        cur = db.cursor()

        # Get the state name from command line arguments
        state_name = sys.argv[4]

        # Execute the SQL query
        cur.execute(
            "SELECT cities.name "
            "FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "WHERE states.name = %s "
            "ORDER BY cities.id",
            (state_name,)
        )

        # Fetch the results
        rows = cur.fetchall()

        # Print the results
        if rows:
            city_names = ', '.join(row[0] for row in rows)
            print(city_names)
        else:
            print("No cities found for the state: {}".format(state_name))

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
    except Exception as e:
        print("Error: {}".format(e))
    finally:
        cur.close()
        db.close()
