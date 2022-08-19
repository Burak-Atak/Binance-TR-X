import numpy as np
import talib


class Indicator:

    @staticmethod
    def trix(prices, timeperiod=15) -> np.ndarray:
        """
        Return TRIX of given price array

        :param prices:
        :type prices: np.ndarray
        :param timeperiod:
        :type timeperiod: int
        :return: Return TRIX of given price array
        """

        # Calculation EMA1, EMA2, EMA3 of given price array

        ema1 = talib.EMA(np.array(prices, dtype=float), timeperiod=timeperiod)
        ema2 = talib.EMA(np.array(ema1), timeperiod=timeperiod)
        ema3 = talib.EMA(np.array(ema2), timeperiod=timeperiod)

        # Calculate for every number in price array the difference between EMA3 and EMA3 of yesterday
        # and divide by EMA3 of yesterday and multiply by 10000
        # if yesterday price is nan, sets it to nan
        trix = np.array(
            [
                round((ema3[index] - ema3[index - 1]) / ema3[index - 1] * 10000, 2)
                if not np.isnan(ema3[index - 1]) else np.nan
                for index in range(len(ema3))
            ]
        )
        return trix
