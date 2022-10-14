# zipWith( Math.pow, [10,10,10,10], [0,1,2,3] )      =>  [1,10,100,1000]

# ДЗ - 1
# написать алгоритм zip по этому примеру:
def zipWith(func, a1=[10,10,10,10], a2=[0,1,2,3,5]):
    new_result = []
    print(list(zip(a1, a2)))
    result = list(zip(a1, a2))
    for val in result:
        new_result.append(func(val[0], val[1]))

    return new_result

zipWith(max)


# a = lambda a: a + 3 # return a+3
# print(a(5))


# ДЗ - 2
# pip freeze
# pip install -r file_name (requirements.txt)


# mro
class A:
    def get_name(self):
        print("A.method() called")
    
class B:
    def get_name(self):
        print("B.method() called")

class C(A):
    pass

class D(C, B):
    pass

d = D()
d.get_name()
print( D.mro() )