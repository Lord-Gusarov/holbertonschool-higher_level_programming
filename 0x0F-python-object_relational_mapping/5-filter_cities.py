#!/usr/bin/python3
"""
-Takes in the name of a state as an argument and lists all cities of
that state, using a specified database.
-The Script takes 4 arguments: mysql username, mysql password, database name
and state name (SQL injection free!)
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect('localhost', *sys.argv[1:4])
    toMatch = sys.argv[4]
    cur = db.cursor()
    # Now we ready for a Query
    cur.execute("""
        SELECT name FROM cities
        WHERE state_id = (
            SELECT id FROM states
            WHERE name = %(toMatch)s )
        ORDER BY id
        """, {'toMatch': toMatch})
    cities = list()
    for city in cur.fetchall():
        cities.append(*city)
    print(', '.join(cities))
    # Clean up
    cur.close()
    db.close()
