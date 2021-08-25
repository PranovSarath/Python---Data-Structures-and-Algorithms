from collections import deque


customQueue = deque(maxlen=3)
print(customQueue)

customQueue.append(1)
customQueue.append(2)
customQueue.append(243)

print(customQueue)

customQueue.append(500)
print(customQueue)

print(customQueue.popleft())
print(customQueue)

print(customQueue.clear())
print(customQueue)