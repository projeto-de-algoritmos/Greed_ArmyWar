# 0-1 Knapsack Problem
# Problem link: https://onlinejudge.u-aizu.ac.jp/problems/DPL_1_B

# knap sack algorithm implementation
def knapSack(W, wt, val, n): 
    K = [[0 for x in range(W + 1)] for x in range(n + 1)] 
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] 
                          + K[i-1][w-wt[i-1]],   
                              K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
    return K[n][W]

# read number of elements and max weight
N, W = map(int, input().split())

# init arrays
values = []
weights = []

# read elements
for i in range(N):
  v, w = map(int, input().split())
  values.append(v)
  weights.append(w)

# present knap sack result
print(knapSack(W, weights, values, N))