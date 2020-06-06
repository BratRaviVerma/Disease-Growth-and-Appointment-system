import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dboperation.dbconnection import DatabaseConnection as dbc

fgdframe = pd.read_sql("select diseaseid from disease", dbc.createconnection())
fgdlist = fgdframe["diseaseid"]
print(fgdlist)
growing = pd.read_sql("select diseaseid from patient", dbc.createconnection())
y_pos = np.arange(len(fgdframe))
print(y_pos)
print(growing)

plt.bar(y_pos, fgdframe, align="center", alpha=0.5)
plt.xticks(y_pos, growing)
plt.ylabel("usage")
plt.xlabel("language")
plt.title("popularity of language")
plt.show()
