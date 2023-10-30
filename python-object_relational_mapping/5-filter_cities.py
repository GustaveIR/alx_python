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

    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()

if __name__ == '__main__':
    main()
