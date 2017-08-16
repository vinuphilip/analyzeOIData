import sys
import pandas as pd

dateTobeAnalyzed = sys.argv[1]

#df = pd.read_csv('fo11AUG2017bhav.csv', delimiter=',')
df = pd.read_csv(dateTobeAnalyzed, delimiter=',')

filtered_data = df[df.INSTRUMENT == 'FUTSTK' ]
#print filtered_data

dateValue = filtered_data.iloc[2,14]
#print dateValue

df_sub = filtered_data[["SYMBOL","CONTRACTS","VAL_INLAKH","OPEN_INT","CHG_IN_OI","TIMESTAMP"]].groupby('SYMBOL').sum().reset_index()
df_sub['TIMESTAMP'] = dateValue
#print df_sub

df_selectiveFirstMonth = filtered_data[["SYMBOL", "OPEN" , "HIGH", "LOW", "CLOSE", "SETTLE_PR"]].groupby('SYMBOL').first().reset_index()
#print df_selectiveFirstMonth

#df_merged = pd.merge(df_selectiveFirstMonth, df_sub)
df_merged = pd.merge(df_selectiveFirstMonth, df_sub, on='SYMBOL', how='outer')
df_merged = df_merged[['SYMBOL', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'SETTLE_PR', 'CONTRACTS', 'VAL_INLAKH', 'OPEN_INT', 'CHG_IN_OI','SETTLE_PR', 'TIMESTAMP']]

#print df_merged

#print list(df_merged.columns.values)

# run it only the first time to get headers if you don't want to manully push in the headers
#df_merged.to_csv('final.csv',index = False)
df_merged.to_csv('final.csv', mode='a', header=False, index = False)


 


