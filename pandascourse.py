import pandas as pd
import numpy as np
path = "titanic_data.csv"

dates = pd.date_range("20240513",periods = 6)
print(dates)
#df=pd.read_csv(path)
# df = pd.DataFrame(np.random.randn(6,5), index=dates, columns=list("ABCDE"))
# print(df)

df=pd.read_csv(path)
print(df)


