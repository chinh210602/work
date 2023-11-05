# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])
class MinHeap():
    def __init__(self, array):
        self.heap = array
        self.size = len(array)
    def LeftChild(self, i):
        return 2*i + 1
    def RightChild(self, i):
        return 2*i + 2
    def Parent(i):
        return (i - 1) // 2
    def SiftDown(self, i, array):
        minIndex = i
        leftChild = self.LeftChild(i)
        if leftChild < self.size and array[leftChild][1] < array[minIndex][1]:
            minIndex = leftChild
        elif leftChild < self.size and array[leftChild][1] == array[minIndex][1]:
            if array[leftChild][0] < array[minIndex][0]:
                minIndex = leftChild
            
        rightChild = self.RightChild(i)
        if rightChild < self.size and array[rightChild][1] < array[minIndex][1]:
            minIndex = rightChild
        elif rightChild < self.size and array[rightChild][1] == array[minIndex][1]:
            if array[rightChild][0] < array[minIndex][0]:
                minIndex = rightChild
            
        if i != minIndex:
            array[minIndex], array[i] = array[i], array[minIndex]
            self.SiftDown(minIndex, array)
        
    def ReturnHeap(self):
        return self.heap
    
    def ReturnMin(self):
        return self.heap[0]
    
    def Modify(self, job):
        self.heap[0][1] += job
        self.SiftDown(0, self.heap)


def assign_jobs(n_workers, jobs):

    result = []
    next_free_time = []
    for i in range(n_workers):
        next_free_time.append([i, 0])
    next_free_time = MinHeap(next_free_time)
    for job in jobs:
        next_worker = next_free_time.ReturnMin()
        result.append(AssignedJob(next_worker[0], next_worker[1]))
        next_free_time.Modify(job)

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()