#!/usr/bin/python3
"""Lists the cities of the state given as argument.

The name of the state is passed to execute as a parameter, so no SQL
injection is possible, and the cities are printed on a single line.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities "
                   "JOIN states ON cities.state_id = states.id "
                   "WHERE states.name = %s ORDER BY cities.id ASC",
                   (sys.argv[4],))
    print(", ".join([row[0] for row in cursor.fetchall()]))
    cursor.close()
    db.close()
