#!/usr/bin/python3
# List all states from a specified database
import sys
import MySQLdb

if __name__ == '__main__':
    user, passwd, db_name = sys.argv[1:4]
    db = MySQLdb.connect('localhost', user, passwd, db_name, 3306)
    cur = db.cursor()

    # Now we are ready for a query
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print("({}, '{}')".format(*row))
    # Clean up
    cur.close()
    db.close()
