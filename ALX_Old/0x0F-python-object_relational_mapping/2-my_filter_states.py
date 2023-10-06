#!/usr/bin/python3
"""script that takes in an argument and displays all values in states table
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states \
            WHERE CONVERT (name USING Latin1) \
            COLLATE Latin1_General_CS = '{}'".format(sys.argv[4]))

    states = cur.fetchall()
    [print(state) for state in states]

    cur.close()
    db.close()
