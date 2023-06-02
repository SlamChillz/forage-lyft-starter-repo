from tire.tire import Tire


class OctoprimeTire(Tire):

    __wear_limit = 3

    def needs_service(self):
        if sum(self.tire_wear_numbers) >= self.__wear_limit:
            return True
        return False