class Bank:
    def __init__(self,name,account_number):
        self._name=name
        self._account_number=account_number
    #creating a getter for the class 
    @property
    def name(self):
        return self._name
    @name.setter
    def getter_name(self,name):
        self._name=name

    @property
    def account_number(self):
        return self._account_number
    @account_number.setter
    def getter_number(self,number):
        self._account_number=number
    def displaying(self):
        print("name of the user is {} and acount number of the user is {}".format(self.name,self.account_number))
    
bank=Bank("aswin",12344)
#setter method
bank._name="arun"
print(bank.name)
bank.displaying()
