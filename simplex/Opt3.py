from scipy.optimize import linprog
c = [-3,-1]
A = [[1,1],[1,2]]
b = [6,10]
ans=linprog(c,A,b,bounds=(0,None))
print(ans)

#c = [-0.7,-1]
#A_ub = [[1,1],[1,2]]
#b_ub = [6,10]
#ans=linprog(c,A_ub,b_ub,bounds=(0,None))
#print(ans)

#c = [-0.4,-1]
#A_ub = [[1,1],[1,2]]
#b_ub = [6,10]
#ans=linprog(c,A_ub,b_ub,bounds=(0,None))
#print(ans)