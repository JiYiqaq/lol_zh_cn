from sympy import symbols, Eq, solve

# 定义未知数
x, y, z, w, u, v, r, m, k, a, f = symbols('x y z w u v r m k a f')

# 定义方程组
equations = [
    Eq(x + y + z + w + u + v + r + m + k + a + f, 78),
    Eq(2*x + 3*y, 115),
    Eq(2*x + 2*y + 2*z + 2*w + 2*u + 2*v + 2*r + 6*k, 159),
    Eq(50*z, 50),
    Eq(10*m, 102),
    Eq(78*z, 78),
    Eq(10*a, 78),
    Eq(11*f, 11),
    Eq(128, 128),
    Eq(6*k, 53),
    Eq(2*y, 152)
]

# 求解方程组
solution = solve(equations)

print(solution)
