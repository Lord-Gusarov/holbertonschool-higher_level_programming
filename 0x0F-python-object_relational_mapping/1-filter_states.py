#!/usr/bin/python3
# List all states with a name Starting with 'N' from a specified database
import sys
import MySQLdb

if __name__ == '__main__':
    user, passwd, db_name = sys.argv[1:4]
    db = MySQLdb.connect('localhost', user, passwd, db_name)
    cur = db.cursor()
    # Now we are ready for a query
    cur.execute("SELECT * FROM states "
                "WHERE name LIKE 'N%' "
                "ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print("({}, '{}')".format(*row))
    # Clean up
    cur.close()
    db.close()
