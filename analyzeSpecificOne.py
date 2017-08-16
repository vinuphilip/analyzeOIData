import sys
import pandas as pd


def pct_change(df):
    df_filtered_data['CHG_IN_OI_PCT'] = 100 * ( (df_filtered_data.OPEN_INT  -   df_filtered_data.iloc[0].OPEN_INT) / df_filtered_data.OPEN_INT )
    return df_filtered_data


#pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

stockTickerName = sys.argv[1]

df = pd.read_csv('final.csv', delimiter=',' , index_col=False)

df_filtered_data = df[ df.SYMBOL == stockTickerName ]

df_filtered_data = df_filtered_data.groupby('SYMBOL').apply(pct_change)

df_filtered_data = df_filtered_data.sort_values(by=['TIMESTAMP'], ascending=[False])

df_filtered_data = df_filtered_data[['SYMBOL', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'SETTLE_PR', 'CONTRACTS', 'VAL_INLAKH', 'OPEN_INT', 'CHG_IN_OI', 'CHG_IN_OI_PCT', 'SETTLE_PR', 'TIMESTAMP']]

print df_filtered_data.to_string(index=False)



#dateValue = filtered_data.iloc[2,14]

#df_sub = filtered_data[["SYMBOL","CONTRACTS","VAL_INLAKH","OPEN_INT","CHG_IN_OI","TIMESTAMP"]].groupby('SYMBOL').sum()
#df_sub['TIMESTAMP'] = dateValue

outputFileName = stockTickerName + ".csv"

df_filtered_data.to_csv(outputFileName, index = False)

 


