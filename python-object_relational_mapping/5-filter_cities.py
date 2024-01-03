import MySQLdb
import sys

def sort_city_names(city_names):
    city_names_by_state = {}

    for city_name in city_names:
        if "," in city_name:
            state_name = city_name.split(",")[1].strip()
        else:
            state_name = None

        if state_name not in city_names_by_state:
            city_names_by_state[state_name] = []
        city_names_by_state[state_name].append(city_name)

    sorted_city_names = []
    for state_name, city_names in city_names_by_state.items():
        city_names.sort(key=lambda x: x.lower())  # Sort city names case-insensitively within each state group
        sorted_city_names.extend(city_names)  # Use extend instead of +=
    
    return sorted_city_names



def main():
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    statename = sys.argv[4]

    database = MySQLdb.connect(host='localhost', user=username, passwd=password, db=database_name, port=3306)
    cur = database.cursor()

    query = "SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC"

    cur.execute(query, (statename,))
    results = cur.fetchall()

    if not results:
        print()
    else:
        city_names = [row[0] for row in results]
        print(", ".join(city_names))

    cur.close()
    database.close()

if __name__ == '__main__':
    main()