#!/usr/bin/python3
""" Your comments Here """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", username=sys.argv[1], password=sys.argv[2], database=sys.argv[3], port=3306)
    c = db.cursor()

    c.execute("SELECT * FROM states")
    rows = c.fetchall()

    for row in rows:
        print(row)

    c.close()
    db.close()

   
   
    