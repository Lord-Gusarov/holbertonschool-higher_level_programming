#!/usr/bin/python3
"""Lits all cities from a specified database
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect('localhost', *sys.argv[1:4])
    cur = db.cursor()
    # Now we are ready to Query
    cur.execute("""
        SELECT cities.id, cities.name, states.name from cities
        JOIN states ON states.id = cities.state_id
        ORDER BY cities.id
        """)
    for row in cur.fetchall():
        print(row)
    # Clean up
    cur.close()
    db.close()
