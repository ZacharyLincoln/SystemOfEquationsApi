from flask import Flask
from flask import request

from sympy import Eq, solve_linear_system, Matrix, solve, sympify
from numpy import linalg
import sympy as sp

app = Flask(__name__)

@app.route("/")
def test():
	return "default"


@app.route("/system_of_equation_matrix")
def sytem_of_equations():
	strVariables = str(request.args.get('variables'))
	strVariables = strVariables.replace("[", "")
	strVariables = strVariables.replace("\"", "")
	strVariables = strVariables.replace("\'", "")

	variables = strVariables.split(",")

	strMatrix = str(request.args.get('matrix'))

	strMatrix = strMatrix.replace("[", "")
	strMatrix = strMatrix.replace("\"", "")
	strMatrix = strMatrix.replace("\'", "")

	matrix = strMatrix.split("]")
	matrix.pop(len(matrix) -1 )

	equations = [[]]

	i = 0
	for row in matrix:
		for item in row.split(","):
			equations[i].append(float(item))
		i+=1
		equations.append([])
	equations.pop(len(equations) - 1)

	print(equations)

	if len(variables) == 2:
		x, y = sp.symbols(variables)
		system = Matrix((equations[0], equations[1]))
		print(str(solve_linear_system(system, x, y)))

		return(str(solve_linear_system(system, x, y)))
	if len(variables) == 3:
		x, y, z = sp.symbols(variables)
		system = Matrix((equations[0], equations[1], equations[2]))
		print(str(solve_linear_system(system, x, y, z)))

		return(str(solve_linear_system(system, x, y, z)))




	return "HUIH"



eq1 = sp.Function('eq1')
eq2 = sp.Function('eq2')


x,y = sp.symbols('Fa Fh')

# 2x - y = - 4
eq1 = Eq(2*x-y,-4)
# 3x - 1 = - 2
eq2 = Eq(3*x-1, -2)


row1 = [2,-1,-4]
row2 = [3,-1,-2]

sytem = Matrix((row1,row2))
print(sytem)
print(solve_linear_system(sytem,x,y))


# x + y = 8 + 20 + 12
# x + y = 40

# 4x + 8*2 = 12*2 + 4y
# 4x + 16 = 24 + 4y
# 4x - 4y = 8

# 8y = 16 + 80 + 72
# 8y = 168

#row1 = [0.873696508609309,0,-10]
#row2 = [0.48647138748738716,1,0]

#sytem = Matrix((row1,row2))

#print(solve_linear_system(sytem,x,y))

if __name__ == "__main__":
    app.run(threaded=False)