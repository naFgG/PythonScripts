import pandas as pd

######## 1
df = pd.DataFrame({'col1': ['b', 'a', 'c'], 'col2': [2, 1, 3]})
# sort_values()，字符串排序指定顺序
# 指定字符串的顺序
cat_type = pd.CategoricalDtype(['a', 'b', 'c'])
# 对col1列进行排序，并按照字符串顺序排列
# key 参数可以接收一个函数，该函数作用于每个元素，返回新的排序条件，这样就可以实现更加复杂的排序。
df_sorted = df.sort_values(by='col1', key=lambda x: x.astype(cat_type))


######## 2
df = pd.read_table(r'宽数据', sep='\t')
# id_vars参数指定的是标识变量，即指定的列不需要转换为行
# value_vars参数指定要转换为行的列，这些列的名称直接变成值
# var_name参数指定变量名列的名称，即这个新列的值是str，或者说在转换前，这个新列的值不是数值
# value_name参数指定新值列的名称，即这个新列的值是num，或者说在转换前，这个新列的值是数值
df = df.melt(id_vars=['ASV_ID', 'Test-Statistic', 'p-value'],
             value_vars=['Ctrl-1', 'Ctrl-2', 'Ctrl-3'],
             var_name='Sample', value_name='Abundance')
