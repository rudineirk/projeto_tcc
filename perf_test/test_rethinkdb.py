#!/usr/bin/python2

import random
import uuid
from time import time

import rethinkdb as r

data = []
for i in range(500000):
    data.append([uuid.uuid4(), random.randint(1, 10000)])

r.connect().repl()
table = r.db('test').table('test')

t_start = time()
for d in data:
    table.insert({"name": d[0].hex, "number": d[1]}).run()

t_end = time()
print "time: {0} ms".format((t_end - t_start) * 1000)
