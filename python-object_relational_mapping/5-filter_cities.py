#!/usr/bin/python3
import MySQLdb
import sys

"""
Module Documentation: Provide a brief description of what this module does.
"""

def get_cities_by_state(state_name):
    """
    Function Documentation: Describe what this function does.
    """
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

        # Execute the SQL query
        cur.execute(
            "SELECT GROUP_CONCAT(cities.name SEPARATOR ', ') "
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
            print(f"No cities found for the state: {state_name}")

    except MySQLdb.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        db.close()

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> <state_name>")
        sys.exit(1)
        
    state_name = sys.argv[4]
    get_cities_by_state(state_name)
