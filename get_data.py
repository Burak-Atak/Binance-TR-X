import time
from binance.spot import Spot

from helper import Helper


class GetKlines:
    # create the Binance client, no need for api key
    client = Spot()

    # setup the max limit

    @classmethod
    def get_klines(cls, symbol, interval, limit=500, start_str=None, end_str=None):
        """
        Get Historical Klines from Binance

        :param symbol: Name of symbol pair e.g BNBBTC
        :type symbol: str
        :param interval: Biannce Kline interval
        :type interval: str
        :param limit: Limit the number of entries (default: 500)
        :type limit: int
        :param start_str: Start date string in UTC format
        :type start_str: str
        :param end_str: optional - end date string in UTC format
        :type end_str: str

        :return: list of OHLCV values

        """

        # init our list
        output_data = []

        # convert interval to useful value in seconds
        timeframe = Helper.interval_to_milliseconds(interval)

        # convert our date strings to milliseconds
        start_timestamp = None
        if start_str:
            start_timestamp = Helper.date_to_milliseconds(start_str)

        # if an end time was passed convert it
        end_timestamp = None
        if end_str:
            end_timestamp = Helper.date_to_milliseconds(end_str)

        request_count = 0
        while True:
            temp_data = cls.client.klines(
                symbol=symbol,
                interval=interval,
                limit=limit,
                startTime=start_timestamp,
                endTime=end_timestamp
            )

            output_data += temp_data
            if not temp_data or len(temp_data) < limit:
                break

            start_timestamp = temp_data[-1][0] + timeframe

            request_count += 1

            if request_count % 3 == 0:
                time.sleep(1)

        return output_data
