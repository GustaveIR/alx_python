import MySQLdb
import sys

def fetch_city_info(username, password, database, state):
    try:
        # Connect to MySQL server
        connection = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        
        cursor = connection.cursor()

        # Execute the query with parameters to avoid SQL injection
        query = "SELECT * FROM cities WHERE state = %s ORDER BY id ASC"
        cursor.execute(query, (state,))

        # Fetch all the results
        results = cursor.fetchall()

        # Display the results
        for row in results:
            print(row)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the connection
        cursor.close()
        connection.close()

# Check if all required arguments are provided
if len(sys.argv) != 5:
    print("Usage: python script.py <username> <password> <database> <state>")
    sys.exit(1)

# Retrieve arguments
username, password, database, state = sys.argv[1:]

# Call the function with the provided arguments
fetch_city_info(username, password, database, state)
