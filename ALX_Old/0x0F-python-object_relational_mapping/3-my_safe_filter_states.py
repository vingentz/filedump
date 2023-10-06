#!/usr/bin/python3
"""Script takes in args and shows matching args in states
Argument must be safe from SQL injection
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %(name)s",
                {'name': sys.argv[4]})
    # cur.execute("SELECT * FROM states WHERE name = %s", (sys.argv[4],))
    states = cur.fetchall()
    [print(state) for state in states]

    cur.close()
    db.close()
