"""
Класс с логикой для расчета доступной к получению суммы.
"""
import traceback
import sys


class DataValidation:

    __KEYS = ['gender', 'age', 'loan_years', 'income_source', 'loan_amount', 'annual_income', 'loan_purpose',
              'credit_score']

    def __init__(self, payload):
        self.payload = payload
        self.data_errors = []

    def validate(self):
        try:
            self.is_dictionary()
            self.validate_keys()
        except Exception:
            print("noes")
            # traceback.print_exc()
            pass
        return self.data_errors

    def is_dictionary(self):
        assert isinstance(self.payload, list)

    def validate_keys(self):
        assert set(self.payload.keys()) == set(self.__KEYS)
