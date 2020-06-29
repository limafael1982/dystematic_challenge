# -*- coding: utf-8 -*-

import pandas as pd
import yfinance as yf
from fin_data_exception import FinDataFetchExcpetion


class FinDataCollector:

    def __init__(self):
        self._options = ['FB', 'AAPL', 'NFLX', 'GOOG']
        self.data_frame = pd.DataFrame()

    def fetch_data_frame(self, option='FB'):
        if option not in self._options:
            raise FinDataFetchExcpetion('Data cannot be fetched since {} is not available'.option)
        else:
            print('feching data from {}'.option)




