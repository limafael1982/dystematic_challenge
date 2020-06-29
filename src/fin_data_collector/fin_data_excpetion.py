# -*- coding: utf-8 -*-


class FinDataException(Exception):
    """Base exception for FinDataCollector"""
    pass


class FinDataFetchExcpetion(FinDataException):
    """Exception when data fetch does not work"""

class FinDataPeriodFetchException(FinDataException):
    print('please give the correct date parameters YYYY-MM-DD')
