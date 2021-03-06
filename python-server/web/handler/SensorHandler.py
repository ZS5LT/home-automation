import json
from datetime import datetime, timedelta

from typeguard import typechecked

from web.formatter.SensorsFormatter import SensorsFormatter
from web.handler.CorsHandler import CorsHandler
from web.security.secure import secure


class SensorHandler(CorsHandler):
    @typechecked()
    def initialize(self, sensors_formatter: SensorsFormatter):
        self.__sensors_formatter = sensors_formatter

    @secure
    def get(self, id):
        nr_days_behind = 7
        start_date = datetime.today() - timedelta(days=nr_days_behind)
        end_date = datetime.today()
        self.write(json.dumps(self.__sensors_formatter.get_sensor_values(id, start_date, end_date)))