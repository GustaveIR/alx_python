#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Connect to the MySQL server
    db = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the query to retrieve states starting with 'N' (case-sensitive)
    cur.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' "
        "COLLATE utf8mb4_bin ORDER BY id;"
    )

    # Fetch all the rows that match the query
    rows = cur.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
