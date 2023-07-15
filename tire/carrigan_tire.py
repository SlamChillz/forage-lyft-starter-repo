from tire.tire import Tire


class CarriganTire(Tire):

    __wear_limit = 0.9

    def needs_service(self):
        if max(self.tire_wear_numbers) >= self.__wear_limit:
            return True
        return False
