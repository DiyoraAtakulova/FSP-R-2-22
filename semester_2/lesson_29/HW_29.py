"""
      Name     Shares      Price     Change 
---------- ---------- ---------- ---------- 
        AA        100      39.91       7.71 
       IBM         50     106.11      15.01 
       CAT        150      78.58      -4.86 
      MSFT        200      30.47     -20.76 
        GE         95      37.38      -2.99 
      MSFT         50      30.47     -34.63 
       IBM        100     106.11      35.67
"""

file = open("tablisa.txt", "w+")
def tablisa(*a):
    total=''
    for x in a:
        keygan=''
        valgan=''
        # spisok=[]
        for key,value in x.items():
            keygan+=f'{key:>10}'
            for x in value:
                
                valgan+=f'{x:>10}'
            valgan+='\n'
        keygan+='\n'
        valgan+='\n'
        tab=(("-")*10+' ')*4+'\n'
        total+=keygan+tab+valgan
    # print(total)
    file.write(total)

home={
    'name': ['apple',2,3,4],
    'share': ['huawei',6,7,8],
    'price': ['samsung',10,11,12],
    'change': ['xiaomi',14,15,16],
}
tablisa(home)
file.close()
