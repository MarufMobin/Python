""" namespace , scope """
""" 
    namespace are allow same name multiple parpuss using facalities 

    Scope means a variable access ability. 
    it's three type 
    1. Global
    2. Local 
    3. Block / functional 

    this concept flow a rule it's call LEGB rule 
    L = local
    E = Enclosed ( nested function scope )
    G = Global 
    B = Builtin
"""

""" Local Scope """
s = "I am Global"

def f():
    s = "I am Local"
    print( s )

# f()
# print( s )

""" Enclosed Scope """
def outer_scope():
    s = "I am Local" # Outer Scope Local Scope 
    def inner_scope():
        s = "I am enclosed"
        print(s)
    inner_scope()

# outer_scope()

"""  
    Local Scope 
    Global Scope
    Builtin Scope 
    Enclosed Scope
"""
from math import pi
# pi = 34.11
def outer_scope():
    # pi = 33.11
    def inner_scope():
        # pi = 3.345
        print( pi )
    inner_scope()
outer_scope()
print(pi)

""" 
    Working Procedural are here 
    enclosed > local > global > builtin 
"""
    
    
