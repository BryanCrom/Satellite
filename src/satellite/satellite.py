
import logging

logger = logging.getLogger("satellite")

class Satellite:
    speed: float
    altitude: float

    def __init__(self, altitude, speed):
        self.altitude = altitude
        self.speed = speed

    def get_telemetry(self):
        return f"| speed: {self.speed} | altitude: {self.altitude}"

    def set_speed(self, new_speed):
        self.speed = new_speed

    def set_altitude(self, new_altitude):
        self.altitude = new_altitude