#!/usr/bin/python3
"""Lists the states whose name matches the argument given, safely.

The value searched is passed to execute as a parameter, so the database
driver escapes it and no SQL injection is possible.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY %s "
                   "ORDER BY states.id ASC", (sys.argv[4],))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
