#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in the states
table of a specified table where name matches the argument
*(QUERY IS PROTECTED AGAINST SQL injection)
"""
import sys
import MySQLdb

if __name__ == '__main__':
    user, passwd, db_name, toMatch = sys.argv[1:5]
    db = MySQLdb.connect('localhost', user, passwd, db_name)
    cur = db.cursor()
    # Now we are ready for a Query
    cur.execute(
        """
        SELECT * FROM states
        WHERE BINARY name = %(toMatch)s
        ORDER BY id
        """, {'toMatch': toMatch})
    for row in cur.fetchall():
        print(row)
    # Clean up
    cur.close()
    db.close()
