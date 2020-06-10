"""
Класс с логикой для расчета доступной к получению суммы.
Для каждого валидируемого параметра отдельный метод.
Один общий, который запускает все проверки, и возвращает либо True, если все ок,
либо список ошибок при валидации.
"""
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
            e = sys.exc_info()[0]
            self.data_errors.append(e)
        return self.data_errors

    def is_dictionary(self):
        assert isinstance(self.payload, dict)

    def validate_keys(self):
        assert set(self.payload.keys()) == set(self.__KEYS)
