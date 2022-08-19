from tire.tire import Tire
from abc import ABC

class CarriganTire(Tire, ABC):
    def __init__(self, sensor_list):
        self.sensor_list = sensor_list

    def needs_service(self):
        sensor_list = self.sensor_list
        count = 0
        for sensor in sensor_list:
            if sensor >= 0.9:
                count += 1
        
        if count > 0:
            return True
        else:
            return False