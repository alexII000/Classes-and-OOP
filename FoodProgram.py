import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {'trans1':['2/15/2023','The Lone Patty',17,569],
                'trans2':['2/15/2023','The Octobreakfast',18,569],
                'trans3':['2/15/2023','The Octoveg',16,570],
                'trans4':['2/15/2023','The Octoburger',20,570],
}

order_total = 0.0
discount_rate = .2

# #First program Run 
customer_id = 570
name = 'Danni Sellyar'
address = '97 Mitchell Way Hewitt Texas 76712'
email = 'dsellyarft@gmpg.org'
phone = '254-555-9362'
member_status = False

# Second Program Run
# customer_id = 569
# name = 'Aubree Himsworth'
# address = '1172 Moulton Hill Waco Texas 76710'
# email = 'ahimsworthfs@list-manage.com'
# phone = '254-555-2273'
# member_status = True

Customer = fc.Customer(customer_id, name, address, email, phone, member_status)
print(f'Customer name: {Customer.getName()}')
print(f'Phone: {Customer.getPhone()}')

for key in dict:
    Transaction = fc.Transaction(dict[key][0], dict[key][1], dict[key][2],dict[key][3])
    if Customer.getID() == dict[key][3]:
        print(f'Order Item: {Transaction.getItem()}  Price: ${Transaction.getCost():.2f}')
        order_total += Transaction.getCost()
print(f'Total Cost: ${order_total:.2f}')

discount_amt = order_total * discount_rate
member_price = order_total - discount_amt

if Customer.isMember() == True:
    print(f'Member Discount: ${discount_amt:.2f}')
    print(f'Total Cost after discount: ${member_price:.2f}')

print()
        


