class Atm(object):
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin    
    def start(self):
        print("started")
    def check_balance(self):
        print("your balance is 50,000")

new_user= Atm(Card_number, pin_number)

#car1=Car("3","red","bmw",80)
#car1.start()