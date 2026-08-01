#!/usr/bin/python3
"""Lists all the states of a database.

This script connects to a MySQL server running on localhost at port
3306 and displays every row of the states table, sorted by id.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
