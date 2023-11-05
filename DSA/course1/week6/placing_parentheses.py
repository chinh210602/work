
def MinAndMax(i, j, op, m, M):
    min_ = 100000
    max_ = -100000
    ops_map = {'+': lambda x, y: x + y,
               '-': lambda x, y: x - y,
               '*': lambda x, y: x * y,
               '/': lambda x, y: x / y}

    for k in range(i, j - 1):
        a = ops_map[op[k]](M[i][k], M[k + 1][j])
        b = ops_map[op[k]](M[i][k], m[k + 1][j])
        c = ops_map[op[k]](m[i][k], M[k + 1][j])
        d = ops_map[op[k]](m[i][k], m[k + 1][j])

        min_ = min(min_, a, b, c, d)
        max_ = max(max_, a, b, c, d)
        
    return min_, max_

def PlacingParentheses(d, op):
    m = [[0 for _ in range(len(d))] for _ in range(len(d))]
    M = [[0 for _ in range(len(d))] for _ in range(len(d))]
    n = len(d)
    for i in range(n):
        m[i][i], M[i][i] = d[i], d[i]

    for s in range(n):
        for i in range(n - s):
            j = i + s

            m[i][j], M[i][j] = MinAndMax(i, j, op, m, M)
    return M

d = [5, 8, 7, 4, 8, 9]
op = ['-', '+', '*', '-', '+']

print(PlacingParentheses(d, op))