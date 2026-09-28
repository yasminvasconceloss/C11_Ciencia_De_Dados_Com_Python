import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from Cap6_Matplotlib_Seaborn.Seaborn import ds_tips

#BOXPLOT
ds_tips = sns.load_dataset("tips")

#traçando um boxplot
sns.boxplot(
    data=ds_tips,
    x = 'day',
    y = 'tip',
    hue = 'sex'
)

plt.show()

#REGPLOT
sns.regplot(
    data=ds_tips,
    x = "total_bill",
    y = "tip",
    line_kws = {"color":"red"}
)
plt.show()

#HEATMAP

#selcionando as colunas que quero identificar uma correlacao
corr = ds_tips[["total_bill", "tip", "size"]].corr()

#traçando o heatmap
sns.heatmap(
    corr,
    annot= True,
    fmt = '.2f',

)

plt.show()