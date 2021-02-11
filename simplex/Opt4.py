from scipy.optimize import linprog
c = [-0.4,-1]
A = [[1,1],[1,2]]
b = [6,10]
ans=linprog(c,A,b,bounds=(0,None))
print(ans)
