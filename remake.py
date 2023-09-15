import pandas as pd

mapp = pd.read_table('mapping.txt', sep='\t')[['Sample', 'Group']]
df = pd.read_table(r'result\6.Meta_Statistic\kruskal_wallis\family\diff_family_top10_boxplot.xls', sep='\t')
# id_vars参数指定的是标识变量，即指定的列不需要转换为行
# value_vars参数指定要转换为行的列，这些列的名称直接变成值
# var_name参数指定变量名列的名称，即这个新列的值是str，或者说在转换前，这个新列的值不是数值
# value_name参数指定新值列的名称，即这个新列的值是num，或者说在转换前，这个新列的值是数值
df = df.melt(id_vars=['ASV_ID', 'Test-Statistic', 'p-value', 'FDR_P', 'Bonferroni_P',
                      'Ctrl_mean', 'IBS-D_mean', 'Li05_mean'],
             value_vars=['Ctrl-1', 'Ctrl-2', 'Ctrl-3', 'Ctrl-5', 'Ctrl-6', 'Ctrl-7', 'Ctrl-8', 'Ctrl-9', 'IBS-D-2',
                         'IBS-D-3', 'IBS-D-6', 'IBS-D-7', 'IBS-D-8', 'IBS-D-9', 'IBS-D-10', 'IBS-D-11', 'Li05-1',
                         'Li05-3', 'Li05-4', 'Li05-5', 'Li05-6', 'Li05-7', 'Li05-8', 'Li05-9'],
             var_name='Sample', value_name='Abundance')
df.rename(columns={'ASV_ID': 'id'}, inplace=True)
df = df[['Sample', 'id', 'Abundance', 'Test-Statistic', 'p-value', 'FDR_P', 'Bonferroni_P',
         'Ctrl_mean', 'IBS-D_mean', 'Li05_mean']]
df = pd.merge(df, mapp, on='Sample')
df.to_csv(r'result\6.Meta_Statistic\kruskal_wallis\family\diff_family_top10_boxplot.txt', sep='\t', index=False)
