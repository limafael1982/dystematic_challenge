# -*- coding: utf-8 -*-


import pandas as pd
import yfinance as yf
from datetime import datetime
from .fin_data_excpetion import FinDataFetchExcpetion, FinDataPeriodFetchException


class FinDataCollector:

    def __init__(self):
        self._options = ['FB', 'AAPL', 'NFLX', 'GOOG']
        self.data_frame = pd.DataFrame()
        self.ticker_obj = None

    def fetch_ticker_obj(self, option=''):
        if option not in self._options:
            raise FinDataFetchExcpetion('Data cannot be fetched since {} is not available'.format(option))
        print('feching data from {} ...'.format(option))
        ticker_obj = yf.Ticker(option)
        self.ticker_obj = ticker_obj

    def fetch_historical_data_given_ticker_obj(self, start_date, end_date):
        if start_date is None or start_date == '':
            print('start_date was not provided')
            raise FinDataPeriodFetchException
        if end_date is None or end_date == '':
            print('end_date was not provided')
            raise FinDataPeriodFetchException
        if self.ticker_obj is None:
            raise FinDataFetchExcpetion('Fetch ticker object first. Call fetch_ticker_obj() method.')















