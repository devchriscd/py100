
# Main scope
def set_foo():
    # Function scope
    foo = 'bar'

set_foo()
print(foo)

# The reason this raises an error is because we are executing code that
# is not part of 'foo' scope. 'foo' is created inside a function.