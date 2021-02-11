# import the library pulp as p
import pulp as p

# Create a LP Minimization problem
Lp_prob = p.LpProblem('Problem', p.LpMinimize)

# Create problem Variables
R1 = p.LpVariable("R1", lowBound = 0)
R2 = p.LpVariable("R2", lowBound = 0)
R3 = p.LpVariable("R3", lowBound = 0)
R4 = p.LpVariable("R4", lowBound = 0)
I1 = p.LpVariable("I1", lowBound = 0)
I2 = p.LpVariable("I2", lowBound = 0)
I3 = p.LpVariable("I3", lowBound = 0)
I4 = p.LpVariable("I4", lowBound = 0)
B1 = p.LpVariable("B1", lowBound = 0)
B2 = p.LpVariable("B2", lowBound = 0)
B3 = p.LpVariable("B3", lowBound = 0)
B4 = p.LpVariable("B4", lowBound = 0)
S1 = p.LpVariable("S1", lowBound = 0)
S2 = p.LpVariable("S2", lowBound = 0)
S3 = p.LpVariable("S3", lowBound = 0)
S4 = p.LpVariable("S4", lowBound = 0)
D1 = p.LpVariable("D1", lowBound = 0)
D2 = p.LpVariable("D2", lowBound = 0)
D3 = p.LpVariable("D3", lowBound = 0)
D4 = p.LpVariable("D4", lowBound = 0)
C1 = p.LpVariable("C1", lowBound = 0)
C2 = p.LpVariable("C2", lowBound = 0)
C3 = p.LpVariable("C3", lowBound = 0)
C4 = p.LpVariable("C4", lowBound = 0)

# Objective Function
Lp_prob += 500 * ( R1 + R2 + R3 + R4 ) + 200 * ( I1 + I2 + I3 + I4 ) + 5000 * ( B1 + B2 + B3 + B4 ) - 3000 * ( S1 + S2 + S3 + S4 ) + 300 * ( D1 + D2 + D3 + D4 )

# Constraints:
#changed some equalities constraint to Inequalities

Lp_prob += R1 - B1 + S1 >= 2
Lp_prob += - R1 + B1 - S1 >= -2
Lp_prob += R2 - R1 - B2 + S2 >= 0
Lp_prob += - R2 + R1 + B2 - S2 >= 0

Lp_prob += R3 - R2 - B3 + S3 >= 0
Lp_prob += -R3 + R2 + B3 - S3 >= 0

Lp_prob += R4 - R3 - B4 + S4 >= 0
Lp_prob += -R4 + R3 + B4 - S4 >= 0

Lp_prob += I1 - D1 - C1 >= 600
Lp_prob += -I1 + D1 + C1 >= -600

Lp_prob += I2 - D2 - I1 + D1 - C2 >= 800
Lp_prob += -I2 + D2 + I1 - D1 + C2 >= -800

Lp_prob += I3 - D3 - I2 + D2 - C3 >= 500
Lp_prob += -I3 + D3 + I2 - D2 + C3 >= -500

Lp_prob += I4 - D4 - I3 + D3 - C4 >= 400
Lp_prob += -I4 + D4 + I3 - D3 + C4 >= -400

Lp_prob += R4 >= 2
Lp_prob += C1 - 200 * R1 <= 0
Lp_prob += C2 - 200 * R2 <= 0
Lp_prob += C3 - 200 * R3 <= 0
Lp_prob += C4 - 200 * R4 <= 0

Lp_prob += D4 >= 0
Lp_prob += -D4 >= 0

Lp_prob += B1 <= 2
Lp_prob += B2 <= 2
Lp_prob += B3 <= 2
Lp_prob += B4 <= 2

# Display the problem
print(Lp_prob)

status = Lp_prob.solve()   # Solver
print(p.LpStatus[status])   # The solution status

# Printing the final solution
print(p.value(R1), p.value(R2), p.value(R3), p.value(R4), p.value(I1), p.value(I2), p.value(I3),
       p.value(I4), p.value(B1), p.value(B2), p.value(B3), p.value(B4), p.value(S1), p.value(S2),
        p.value(S3), p.value(S4), p.value(D1), p.value(D2), p.value(D3), p.value(D4),p.value(C1),
         p.value(C2), p.value(C3), p.value(C4), p.value(Lp_prob.objective))
