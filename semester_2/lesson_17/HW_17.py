# Написать логику zip функции самому в этом примере:

# def zip_with(fn, a1=[10,10,10,10], a2=[1,2,3,4,5]): 
#     result = [] 
#     print(list(zip(a1, a2)))
#     r = list(zip(a1, a2))
#     for i in r: 
#         result.append( fn(i[0], i[1]) ) 
        
#     return result

# zip_with(max)


def zip_probnik(*args):
    tom = []
    for y in args:
        tom.append(len(y))
    min_tom = min(tom)
    tommi = []
    for x in args:
        total = []
        tommi.append(total)
        for lol in x:
            total.append(lol)
            if len(total) == min_tom:
                break
        result = []
    for i in range(min_tom):
        res = []
        result.append(res)
        for k in tommi:
            res.append(k[i])
    return result

a = [1,2,3]
b = [4,5]
c = [6,7,8,9]
d = 'ABCD'
print(zip_probnik(a,b,c,d))

