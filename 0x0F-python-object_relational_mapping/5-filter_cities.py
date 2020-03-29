#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT cities.name FROM cities, states \
    WHERE state_id=states.id AND states.name = %s \
    ORDER by cities.id", (sys.argv[4],))
    results = cur.fetchall()

    list = []
    for i in results:
        list.append(i[0])
    print(", ".join(list))

    cur.close()
    db.close()
