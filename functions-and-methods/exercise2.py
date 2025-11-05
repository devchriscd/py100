foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)

# Unlike the previous problem this prints because 'foo' is defined within
# the main scope.