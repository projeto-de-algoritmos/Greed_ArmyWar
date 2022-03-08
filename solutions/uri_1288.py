# Canhão de Destruição Problem
# problem link: https://www.beecrowd.com.br/judge/pt/problems/view/1288


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

# number of test cases
N = int(input())

for _ in range(N):
  # number of cannon balls
  n = int(input())

  # init arrays
  damage = []
  weight = []

  # read cannon balls
  for i in range(n):
    x, y = map(int, input().split())
    damage.append(x)
    weight.append(y)
  cannon = int(input())
  castle = int(input())

  # get knap sack result
  totalDamage = knapSack(cannon, weight, damage, n)

  # check if total damage is enough for the mission
  if totalDamage >= castle:
    print("Missao completada com sucesso")
  else:
    print("Falha na missao")