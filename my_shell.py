from my_app.models import Customer, Account, Work
import json

with open('data.json') as f:
    data = json.load(f)

for i in data:
    customer = Customer(name=i['name'], phone=i['phone'], email=i['email'])
    customer.save()
    work = Work(address=i['address'], city=i['city'], company=i['company'], postalZip=i['postalZip'], customer=customer)
    account = Account(pin=i['pin'], acc_num=i['acc_num'], pan=i['pan'], cvv=i['cvv'], customer=customer)
    work.save()
    account.save()







