from scipy.optimize import linprog
C = [-1.7,0.6]
A = [[-5,-4],[-5,6],[5,2]]
B = [5,30,10]
result = linprog(C,A,B,bounds=(0,None))
print(result)