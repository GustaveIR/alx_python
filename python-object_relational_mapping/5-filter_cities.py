import MySQLdb
import sys

def sort_city_names(city_names):
    """Sorts city names alphabetically, but also groups together city names from the same state."""
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
        city_names.sort()  # Sort city names within each state group
        sorted_city_names += city_names
    
    return sorted_city_names


def main():
    database_name = sys.argv[3]
    username = sys.argv[1]
    password = sys.argv[2]
    statename = sys.argv[4]

    database = MySQLdb.connect(host='localhost', user=username, passwd=password, db=database_name, port=3306)
    cur = database.cursor()

    query = "SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE %s = states.name ORDER BY cities.id ASC"

    cur.execute(query, (statename,))
    results = cur.fetchall()

    
    cur.close()
    database.close()

if __name__ == '__main__':
    main()
