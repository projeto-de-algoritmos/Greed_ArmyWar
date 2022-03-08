# Motoboy Problem
# problem link: https://www.beecrowd.com.br/judge/pt/problems/view/1286


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

while True:
  # number of orders
  n = int(input())

  # end conditino
  if n==0:
    break

  # max number of pizzas
  P = int(input())

  # init arrays
  time = []
  quan = []

  # read orders
  for i in range(n):
    # read time and quantity of order
    t, q = map(int, input().split())
    time.append(t)
    quan.append(q)
  
  # present knapsack result
  print("{} min.".format(knapSack(P, quan, time, len(time))))