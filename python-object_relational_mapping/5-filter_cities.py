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

        # Insert states and cities
        cur.execute('''
            INSERT INTO states (name) VALUES 
            ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada")
        ''')

        cur.execute('''
            CREATE TABLE IF NOT EXISTS cities ( 
                id INT NOT NULL AUTO_INCREMENT, 
                state_id INT NOT NULL,
                name VARCHAR(256) NOT NULL,
                PRIMARY KEY (id),
                FOREIGN KEY(state_id) REFERENCES states(id)
            )
        ''')

        cur.execute('''
            INSERT INTO cities (state_id, name) VALUES 
            (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore"),
            (2, "Page"), (2, "Phoenix"),
            (3, "Dallas"), (3, "Houston"), (3, "Austin"),
            (4, "New York"),
            (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City")
        ''')

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

        # Print the results
        if rows:
            city_names = ', '.join(row[0] for row in rows)
            print(city_names)
        else:
            print(f"No cities found for the state: {state_name}")

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
    except Exception as e:
        print("Error: {}".format(e))
    finally:
        # Close the cursor and database connection
        cur.close()
        db.close()
