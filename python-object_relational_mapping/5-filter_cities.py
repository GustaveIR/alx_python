#!/usr/bin/python3
"""
Script that lists all cities from a specific state in the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Connect to the MySQL server
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the query to retrieve cities of the specified state
    cur.execute(
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id",
        (sys.argv[4],)
    )

    # Fetch all the rows that match the query
    rows = cur.fetchall()

    # Print the results
    if rows:
        city_names = ', '.join(row[0] for row in rows)
        print(city_names)
    else:
        print("No cities found for the specified state.")

    # Close the cursor and database connection
    cur.close()
    db.close()