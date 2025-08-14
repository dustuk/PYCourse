class Card:
    #-----------Attributes-----------
    def __init__(self, number, pin):
        self.number = number
        self.__pin = pin
        
    #------------Methods------------
    def get_pin(self):
        return self.__pin

    def set_pin(self, old_pin, new_pin):
        if self.__pin == old_pin:
            self.__pin = new_pin
            return True
        return False

