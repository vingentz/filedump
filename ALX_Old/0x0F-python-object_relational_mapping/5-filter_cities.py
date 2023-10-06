#!/usr/bin/python3
"""Script takes in statename as argument and lists all cities in that state
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute('SELECT cities.name \
            FROM cities \
            JOIN states ON cities.state_id = states.id \
            WHERE states.name = %(name)s', {'name': sys.argv[4]})

    cities = cur.fetchall()
    citiesList = [item for city in cities for item in city]
    print(", ".join(citiesList))

    cur.close()
    db.close()
