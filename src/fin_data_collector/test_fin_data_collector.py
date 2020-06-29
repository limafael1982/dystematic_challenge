# -*- coding: utf-8 -*-

import unittest
from .fin_data_collector import FinDataCollector
from .fin_data_excpetion import FinDataFetchExcpetion


class TestFinDataCollector(unittest.TestCase):

    def setUp(self) -> None:
        self.fin_data_collect_obj = FinDataCollector()

    def test_should_have_correct_object(self):
        self.assertTrue(isinstance(self.fin_data_collect_obj, FinDataCollector))

    def test_ticker_obj_fetcher_should_not_work_with_incorrect_options(self):
        incorrect_option = 'a random string'
        self.assertRaises(FinDataFetchExcpetion, self.fin_data_collect_obj.fetch_ticker_obj(incorrect_option))

   # def test_ticker_obj_fetcher_should_work_with_correct_options(self):
   #     an_option = 'FB'




