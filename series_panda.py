import pandas as pd
x=[1,2,3,4,5]
var=pd.Series(x,dtype="float")
print(var)
print(var[2])
print()
y={"NAME":["A","B","C"],"AGE":[20,25,30]}
print(pd.DataFrame(y))
print()
print(pd.Series(y))