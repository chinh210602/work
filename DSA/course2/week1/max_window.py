import collections

def max_window(array, m):
    result = []
    q = collections.deque()
    l = r = 0

    while r < len(array):
        #pop smaller values from q
        while q and array[q[-1]] < array[r]:
            q.pop()
            
        q.append(r)
        
        #remove left val from window
        if l > q[0]:
            q.popleft()
            
        if (r + 1) >= m:
            result.append(array[q[0]])
            l += 1
        r += 1
    return result
        
if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))
    m = int(input())
    
    result = max_window(array, m)
    
    for a in result:
        print(a, end = " ")