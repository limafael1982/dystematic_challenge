# -*- coding: utf-8 -*-

import unittest
import yfinance as yf
from .fin_data_collector import FinDataCollector
from .fin_data_excpetion import FinDataFetchExcpetion, FinDataPeriodFetchException


class TestFinDataCollector(unittest.TestCase):

    def setUp(self) -> None:
        self.fin_data_collect_obj = FinDataCollector()

    def tearDown(self) -> None:
        self.fin_data_collect_obj = None

    def test_should_have_correct_object(self):
        self.assertTrue(isinstance(self.fin_data_collect_obj, FinDataCollector))

    def test_ticker_obj_fetcher_should_not_work_with_incorrect_options(self):
        incorrect_option = 'a random string'
        self.assertRaises(FinDataFetchExcpetion, self.fin_data_collect_obj.fetch_ticker_obj, incorrect_option)

    def test_ticker_obj_fetcher_should_work_with_correct_options(self):
        options = ['FB', 'AAPL', 'NFLX', 'GOOG']
        for an_options in options:
            an_option = 'FB'
            self.fin_data_collect_obj.fetch_ticker_obj(an_option)
            self.assertTrue(isinstance(self.fin_data_collect_obj.ticker_obj, yf.Ticker))

    def test_should_return_exception_when_incorrect_date_parameters_are_passed_incorrectly(self):
        start_date = ''
        end_date = '2020-06-06'
        self.fin_data_collect_obj.fetch_ticker_obj('FB')
        self.assertRaises(FinDataPeriodFetchException,
                          self.fin_data_collect_obj.get_historical_data_given_ticker_obj,
                          start_date,
                          end_date)
        start_date = '2020-06-10'
        end_date = ''
        self.assertRaises(FinDataPeriodFetchException,
                          self.fin_data_collect_obj.get_historical_data_given_ticker_obj,
                          start_date,
                          end_date)

    def test_should_raise_exception_when_tick_is_not_fetched(self):
        start_date = '2020-06-10'
        end_date = '2020-06-20'
        self.assertRaises(FinDataFetchExcpetion,
                          self.fin_data_collect_obj.get_historical_data_given_ticker_obj,
                          start_date,
                          end_date)











