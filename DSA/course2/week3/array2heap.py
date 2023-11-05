class MinHeap():
    def __init__(self, array):
        self.track = []
        self.heap = self.BuildHeap(array)
    def LeftChild(self, i):
        return 2*i + 1
    def RightChild(self, i):
        return 2*i + 2
    def Parent(i):
        return (i - 1) // 2
    def SiftDown(self, i, array):
        minIndex = i
        leftChild = self.LeftChild(i)
        if leftChild < self.size and array[leftChild] < array[minIndex]:
            minIndex = leftChild
            
        rightChild = self.RightChild(i)
        if rightChild < self.size and array[rightChild] < array[minIndex]:
            minIndex = rightChild
            
        if i != minIndex:
            array[minIndex], array[i] = array[i], array[minIndex]
            self.track.append(i)
            self.track.append(minIndex)
            self.SiftDown(minIndex, array)

    def BuildHeap(self, array):
        self.size = len(array)
        for i in range(self.size//2, -1, -1):
            self.SiftDown(i, array)
        
    def ReturnHeap(self):
        return self.heap
    
if __name__ == "__main__" :
    n = int(input())
    array = list(map(int, input().split()))
    tracks = MinHeap(array).track
    print(len(tracks) // 2)
    for i, track in enumerate(tracks):
        if i % 2 == 0:
            print(track, end = " ")
        else:
            print(track)