#How to use multiprocessing.Queue as a FIFO queue

from multiprocessing import Queue

customQueue = Queue(maxsize=3)
customQueue.put(145)
print(customQueue.get())