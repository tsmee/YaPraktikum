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
        except:
            _, _, tb = sys.exc_info()
            traceback.print_tb(tb)  # Fixed format
            tb_info = traceback.extract_tb(tb)
            filename, line, func, text = tb_info[-1]
            e = ('An error occurred on line {} in statement {}'.format(line, text))
            self.data_errors.append(e)
            exit(1)
        return self.data_errors

    def is_dictionary(self):
        assert isinstance(self.payload, dict)

    def validate_keys(self):
        assert set(self.payload.keys()) == set(self.__KEYS)
