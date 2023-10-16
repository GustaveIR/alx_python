#!/usr/bin/python3
import mysql.connector
import sys

if __name__ == '__main__':
    try:
        db = mysql.connector.connect(
            host='localhost',
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3],
            port=3306
        )

        cursor = db.cursor()

        state_name = sys.argv[4]
        cursor.execute(
            "SELECT cities.name "
            "FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "WHERE states.name = %s "
            "ORDER BY cities.id",
            (state_name,)
        )

        rows = cursor.fetchall()

        if rows:
            city_names = ', '.join(row[0] for row in rows)
            print(city_names)
        else:
            print("No cities found for the state: {}".format(state_name))

    except mysql.connector.Error as e:
        print("MySQL Error: {}".format(e))
    except Exception as e:
        print("Error: {}".format(e))
    finally:
        cursor.close()
        db.close()
