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

        # Create a cursor object to interact with the database
        cur = db.cursor()

        # Execute the query to retrieve cities of the specified state
        state_name = sys.argv[4]
        cur.execute(
            "SELECT cities.name "
            "FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "WHERE states.name = %s "
            "ORDER BY cities.id",
            (state_name,)
        )

        # Fetch all the rows that match the query
        rows = cur.fetchall()


        # Close the cursor and database connection
        cur.close()
        db.close()
