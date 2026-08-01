#!/usr/bin/python3
"""Lists the states whose name starts with an upper N.

This script connects to a MySQL server running on localhost at port
3306 and displays the matching rows of the states table, sorted by id.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' "
                   "ORDER BY states.id ASC")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
