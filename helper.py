import dateparser
import numpy as np


class Helper:
    @staticmethod
    def interval_to_milliseconds(interval):
        """Convert a Binance interval string to milliseconds

        :param interval: Binance interval string 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w
        :type interval: str

        :return:
             None if unit not one of m, h, d or w
             None if string not in correct format
             int value of interval in milliseconds
        """
        ms = None
        seconds_per_unit = {
            "m": 60,
            "h": 60 * 60,
            "d": 24 * 60 * 60,
            "w": 7 * 24 * 60 * 60
        }

        unit = interval[-1]
        if unit in seconds_per_unit:
            try:
                ms = int(interval[:-1]) * seconds_per_unit[unit] * 1000
            except ValueError:
                pass
        return ms

    @staticmethod
    def date_to_milliseconds(date: str) -> int:
        """
        Convert date to milliseconds

        :param date: Date string in format "YYYY-MM-DD"
        :return: Integer of milliseconds
        """
        date = dateparser.parse(date)
        return int(date.timestamp() * 1000)

    @staticmethod
    def prepare_price_for_indicators(klines_data: list, price_type: str) -> np.ndarray:
        """
        Gets klines_data and desired price type and return array of prices

        :param klines_data:
        :param price_type: Price type string -> open, high, low, close, volume
        :return: np.ndarray of prices
        """

        if price_type == "open":
            return np.array([data[1] for data in klines_data])
        elif price_type == "high":
            return np.array([data[2] for data in klines_data])
        elif price_type == "low":
            return np.array([data[3] for data in klines_data])
        elif price_type == "close":
            return np.array([data[4] for data in klines_data])
        elif price_type == "volume":
            return np.array([data[5] for data in klines_data])
