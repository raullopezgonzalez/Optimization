
from scipy.optimize import linprog
c = [3,1]
A = [[1,1],[1,2]]
b = [6,10]
ans=linprog(c,A,b,bounds=(None,0))
print(ans)
