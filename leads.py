import pandas as pd
import math
import pprint 

csv_file = 'leads.csv'

df = pd.read_csv(csv_file)
saved_column = df['dealer_zip'] #you can also use df['column_name']
saved_column2 = df['list_price']
saved_column3 = df['model']
saved_column4 = df['msrp']
saved_column5 = df['lead_date']
saved_column6 = df['lead_date']
names = df.dealer_zip
prices = df.list_price
models = df.model
msrp = df.msrp
leads = df.lead_date
print names[0]
print models[0]
priceList = prices.tolist()
modelList = models.tolist()
msrpList = msrp.tolist()
y = []
z = []

for i in range(1,100000):
	if math.isnan(priceList[i]) == False or math.isnan(msrpList[i]) == False:
		y.append( (modelList[i],priceList[i]) )
	loss = msrpList[i] * .85
	if loss > priceList[i]:
		amountloss = loss - priceList[i]
		z.append( (modelList[i],amountloss))
print z
print len(z)
print len(y)
print len(msrpList)

print 'percent is ' + str( (float(len(z)/float(len(y)))) * 100 )

