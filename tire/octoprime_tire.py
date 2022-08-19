from tire.tire import Tire
from abc import ABC

class OctoprimeTire:
    def __init__(self, sensor_list):
        self.sensor_list = sensor_list

    def needs_service(self):
        sensor_list = self.service_list
        count = 0
        for sensor in sensor_list:
            count += sensor

        if count >= 3:
            return True
        else:
            return False