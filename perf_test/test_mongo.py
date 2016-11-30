#!/usr/bin/python2

import random
import uuid
from time import time

from pymongo import MongoClient

data = []
for i in range(100000):
    data.append([uuid.uuid4(), random.randint(1, 10000)])

client = MongoClient()
db = client.test
collection = db.test

t_start = time()
for d in data:
    collection.insert_one({"name": d[0], "number": d[1]})

t_end = time()
print "time: {0} ms".format((t_end - t_start) * 1000)
