
def make_greeting(name, age=None): 
    if age is None: 
        return f"Howdy {name}!" 
    else: 
        return f"Whoa {name}! {age} already, you are growing up!"

a = make_greeting('Coronel')
print(a)
# 'make_greeting' returned 'Howdy Coronel!' 


b = make_greeting('Coronel', age=20)
print(b)
# 'make_greeting' returned 'Whoa Coronel! 20 already, you are growing up!'