# -*- coding: utf-8 -*-

class FinDataException(Exception):
    """Base exception for FinDataCollector"""
    pass


class FinDataFetchExcpetion(FinDataException):
    """Exception when data fetch does not work"""