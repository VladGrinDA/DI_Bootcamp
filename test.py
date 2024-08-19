import timeit

# Example 1: Loop with a simple if statement
setup = "x = 10"
stmt = """
for i in range(1000000):
    if x > 5:
        pass
"""
time = timeit.timeit(stmt, setup=setup, number=100)
print(f"Time with if statement: {time:.5f} seconds")

# Example 2: Loop without an if statement
stmt_no_if = """
for i in range(1000000):
    pass
"""
time_no_if = timeit.timeit(stmt_no_if, setup=setup, number=100)
print(f"Time without if statement: {time_no_if:.5f} seconds")


# Example 2: Loop without an if statement
stmt_if_func = """
def my_func(x):
    return x > 5
for i in range(1000000):
    if my_func(x):
        pass
"""
time_no_if = timeit.timeit(stmt_if_func, setup=setup, number=100)
print(f"Time without if statement: {time_no_if:.5f} seconds")

