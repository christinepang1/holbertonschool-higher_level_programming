#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.arg[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id")

    results = cur.fetchall()

    for i in results:
        print(i)

    cur.close()
    db.close()

