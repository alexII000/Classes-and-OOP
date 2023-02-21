class Customer:

    def __init__(self, customer_id, name, address, email, phone, member_status):
        
        self.__customer_id = customer_id
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__member_status = member_status

    def getID(self):
        return self.__customer_id
    def getName(self):
        return self.__name
    def getAddress(self):
        return self.__address
    def getEmail(self):
        return self.__email
    def getPhone(self):
        return self.__phone
    def isMember(self):
        return self.__member_status

class Transaction:
    def __init__(self, date, item_name, cost, customer_id):
        self.__date = date
        self.__item_name = item_name
        self.__cost = float(cost)
        self.__customer_id = customer_id

    def getDate(self):
        return self.__date
    def getItem(self):
        return self.__item_name
    def getCost(self):
        return self.__cost
    def getID(self):
        return self.__customer_id

    


