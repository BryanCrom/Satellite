from datetime import datetime

import logging

logger = logging.getLogger("satellite")

class Satellite:
    speed: float
    altitude: float

    def __init__(self, altitude, speed):
        self.altitude = altitude
        self.speed = speed

    def display_info(self):
        time_stamp = f"| speed: {self.speed} | altitude: {self.altitude}"
        logger.info(time_stamp)