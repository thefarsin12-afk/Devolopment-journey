class Mobile:

    brand:str

    size:str

    def call(self):
        print("Mobile is ringing")

    def message(self):
        print("Mobile using to message")

    def capture(self):
        print("Using camera capture")

iphone_instance = Mobile()    

samsung_instance = Mobile() 

motrola_instance = Mobile() 

motrola_instance.message()

iphone_instance.call()

