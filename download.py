import datetime
import time
import schedule
import requests
import os



currentWorkingDirectory = os.getcwd() + "/"


day=datetime.datetime.today().strftime("%d")
#day="14"
#month=datetime.now().date().strftime ("%m")
month=datetime.datetime.today().strftime("%m")
list_of_months = ['justPaddingItAround','JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
month_in_words = list_of_months[int(month)]



#url='http://www.nseindia.com/content/historical/DERIVATIVES/2017/{}/fo{}{}2017bhav.csv.zip'
url="http://www.nseindia.com/content/historical/DERIVATIVES/2017/" + month_in_words + "/fo" + day + month_in_words + "2017bhav.csv.zip"

file_name="fo" + day + month + "2017bhav.zip"

r = requests.get(url)
with open(os.path.join(currentWorkingDirectory, file_name), "wb") as code: 
    code.write(r.content)

print url

cmd="unzip " +  file_name
os.system(cmd)


cmd="rm " +  file_name
os.system(cmd)

csv_file_name="fo" + day + month_in_words + "2017bhav.csv"


cmd="python parseAndMergeCSV.py " +  csv_file_name
os.system(cmd)
