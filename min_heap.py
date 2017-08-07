class MinHeap:
  def __init__(self):
    self.heapList = [0]
    self.currentSize = 0

  def insert(self, val):
    self.heapList.append(val)
    self.currentSize += 1
    self.heapifyUp(self.currentSize)

  def heapifyUp(self, i):
    while i // 2 > 0:
      if self.heapList[i] < self.heapList[i // 2]:
        self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
      i //= 2

  def heapifyDown(self, i):
    while i * 2 <= self.currentSize:
      minChild = self.minChild(i)
      if self.heapList[i] > self.heapList[minChild]:
        self.heapList[i], self.heapList[minChild] = self.heapList[minChild], self.heapList[i]
      i = minChild

  def minChild(self, i):
    if i * 2 + 1 > self.currentSize:
      return i * 2
    else:
      if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
        return i * 2
      else:
        return i * 2 + 1

  def deleteMin(self):
    deleted = self.heapList[1]
    self.heapList[1] = self.heapList[self.currentSize]
    self.heapList.pop()
    self.currentSize -= 1
    self.heapifyDown(1)
    return deleted

  def isEmpty():
    return self.currentSize == 0

  def size():
    return self.currentSize

  def buildHeap(self, arr):
    i = len(arr) // 2
    self.currentSize = len(arr)
    self.heapList = [0] + arr
    while (i > 0):
      self.heapifyDown(i)
      i -= 1

def main():
  h = MinHeap()
  h.insert(3)
  h.insert(5)
  h.insert(6)
  h.insert(4)
  h.insert(10)
  h.insert(7)
  h.insert(45)
  h.insert(2) 
  print(h.heapList)
  print("Current size of min-heap is", str(h.currentSize) + ".")
main()