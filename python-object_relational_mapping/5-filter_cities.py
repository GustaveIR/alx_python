#!usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host="localhost", user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], port=3306)

        # Create a cursor object to interact with the database
        cur = db.cursor()

        # Execute the query to retrieve cities of the specified state
        cur.execute("""SELECT cities.name FROM 
                       cities INNER JOIN states ON state_id = cities.states.id 
                       WHERE states.name = %s """, (sys.argv[4],))

        # Fetch all the rows that match the query
        rows = cur.fetchall()

        # Print the results
        if rows:
            city_names = ', '.join(row[0] for row in rows)
            print(city_names)
        else:
            print(f"No cities found for the specified state: {sys.argv[4]}.")

    except MySQLdb.Error as e:
        print(f"MySQL Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the cursor and database connection
        cur.close()
        db.close()
