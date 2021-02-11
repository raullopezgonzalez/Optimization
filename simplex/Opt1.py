from scipy.optimize import linprog
c=[0.4,0.5]
A_nm=[[0.3,0.1],[-0.6,-0.4]]
B_nm=[2.7,6]
A_eq=[[0.5,0.5]]
B_eq=[6]
var=linprog(c,A_nm,B_nm,A_eq,B_eq,bounds=(0,None))

print(var)

print("optimal value",var.fun,"value of x",var.x)