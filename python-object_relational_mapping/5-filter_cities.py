#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    try:
        db = MySQLdb.connect(
            host='localhost',
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
        )

        cur = db.cursor()

        state_name = sys.argv[4]
        cur.execute(
            "SELECT cities.name "
            "FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "WHERE states.name = %s "
            "ORDER BY cities.name",  # Changed to order by city names
            (state_name,)
        )

        rows = cur.fetchall()

        if rows:
            city_names = ', '.join(row[0] for row in rows)
            print(city_names)
        else:
            print("No cities found for the state: {}".format(state_name))

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
    except Exception as e:
        print("Error: {}".format(e))
    finally:
        cur.close()
        db.close()
