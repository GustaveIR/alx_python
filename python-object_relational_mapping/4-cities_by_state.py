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

    # Get the state name from command line argument
    state_name = sys.argv[4]

    # Execute the query to retrieve cities with their corresponding states
    cur.execute(
        "SELECT cities.name "
        "FROM cities JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id",
        (state_name,)
    )

    # Fetch all the rows that match the query
    rows = cur.fetchall()

    # Print the results
    for row in rows:
        print(row[0])

    cur.close()
    db.close()
