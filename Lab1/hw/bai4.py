from pymongo import MongoClient
uri='mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

client=MongoClient(uri)

db=client.get_database()

customers=db['customers']

customers_list=customers.find()
events=sum(i.get('ref') == 'events'for i in customers_list)
customers_list=customers.find()
ads=sum(a.get('ref') == 'ads'for a in customers_list)
customers_lists=customers.find()
wom=sum(b.get('ref') == 'wom'for b in customers_list)

from matplotlib import pyplot

ref_counts=[events,ads,wom]
ref_names=['Event','Ads','Word of Mouth']
pyplot.pie(ref_counts,labels=ref_names,autopct="%1f%%")
pyplot.axis('equal')
pyplot.title('Events vs Ads vs Word of Mouth')
pyplot.show()