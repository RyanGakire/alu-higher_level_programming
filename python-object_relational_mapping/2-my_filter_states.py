#!/usr/bin/python3
"""Lists the states whose name matches the argument given.

This script builds its query with format, which makes it vulnerable to
SQL injection, as shown by the next task of the project.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' "
                   "ORDER BY states.id ASC".format(sys.argv[4]))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
