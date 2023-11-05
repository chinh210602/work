import numpy as np

def browmian_motion(t):
    n = 100
    T = float(t)
    times = np.linspace(0., T, n)
    dt = times[1] - times[0]
    
    dB = np.random.normal(size = (n-1,))
    B = np.cumsum(dB)
    
    return B[-1]

def sigma(t):
    return np.exp(browmian_motion(t)**2)

def ito_calculus(T, threshold = 10*(-3), n_simulation = 10**4):
    prev_result = 0
    for i in range(n_simulation):
        B = []
        Sigma = []
        times = list(np.linspace(0., T, i))
        for t in times:
            B.append(browmian_motion(t))
            Sigma.append(sigma(t))
        
        result = 0
        for j in range(i-1):
            result += Sigma[j]*(B[j+1] - B[j])
        
        if result - prev_result > threshold:
            prev_result = result
        else: 
            break
        
    return result

if __name__ == "__main__":
    
    T = 100
    print(ito_calculus(T))