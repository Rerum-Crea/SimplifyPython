from SimplifyPython import sjson
from time import time

sjson.new("data")
data = sjson.open()
data['time'] = time()
sjson.save(data)


