import pandas as pd

df = pd.read_table(r'宽数据', sep='\t')
# id_vars参数指定的是标识变量，即指定的列不需要转换为行
# value_vars参数指定要转换为行的列，这些列的名称直接变成值
# var_name参数指定变量名列的名称，即这个新列的值是str，或者说在转换前，这个新列的值不是数值
# value_name参数指定新值列的名称，即这个新列的值是num，或者说在转换前，这个新列的值是数值
df = df.melt(id_vars=['ASV_ID', 'Test-Statistic', 'p-value'],
             value_vars=['Ctrl-1', 'Ctrl-2', 'Ctrl-3'],
             var_name='Sample', value_name='Abundance')
