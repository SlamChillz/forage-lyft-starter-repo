from battery.battery import Battery


class SpindlerBattery(Battery):

    __service_time_frame = 3

    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + self.__service_time_frame)
        return service_threshold_date < self.current_date
