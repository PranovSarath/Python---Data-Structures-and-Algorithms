import queue as q

customQueue = q.Queue(maxsize=3)
print(customQueue.qsize())
customQueue.put(100)
customQueue.put(256)
customQueue.put(180)

print(customQueue.qsize())
print(customQueue.full())

print(customQueue.get())
print(customQueue.qsize())