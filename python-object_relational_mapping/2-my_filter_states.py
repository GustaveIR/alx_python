#!/usr/bin/python3
"""
Script that takes an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
from sys import argv

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
    c = db.cursor()


    # Execute the query to retrieve states matching the provided name
    c.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' BY id;"
        .format(sys.argv[4]0)
        
    )

    # Fetch all the rows that match the query
    rows = c.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    c.close()
    db.close()

   