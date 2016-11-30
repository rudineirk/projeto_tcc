#!/usr/bin/python2

import random
import uuid
from time import time

import MySQLdb

data = []
for i in range(500000):
    data.append([uuid.uuid4(), random.randint(1, 10000)])

db = MySQLdb.connect(
    host='127.0.0.1',
    port=3306,
    user='test',
    passwd='test',
    db='test',
)
cur = db.cursor()

t_start = time()
for d in data:
    cur.execute(
        "INSERT INTO `test` (`name`, `number`) VALUES ('{0}', {1});"
        .format(*d)
    )
    db.commit()

t_end = time()
db.close()
print "time: {0} ms".format((t_end - t_start) * 1000)
