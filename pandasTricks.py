import pandas as pd

df = pd.DataFrame({'col1': ['b', 'a', 'c'], 'col2': [2, 1, 3]})
# sort_values()，字符串排序指定顺序
# 指定字符串的顺序
cat_type = pd.CategoricalDtype(['a', 'b', 'c'])
# 对col1列进行排序，并按照字符串顺序排列
# key 参数可以接收一个函数，该函数作用于每个元素，返回新的排序条件，这样就可以实现更加复杂的排序。
df_sorted = df.sort_values(by='col1', key=lambda x: x.astype(cat_type))

