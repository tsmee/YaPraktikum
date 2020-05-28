from LoanRequest import LoanRequest
from tests.random_test import moar
import pytest

testcases = moar()

"""
Тесты для класса LoanRequest и запуска скоринга.
В модуле random_tests генерируются случайные валидные данные, 
с ними запускается скоринг. 
Фаззинг-тул для поиска неочевидных багов с комбинаторикой.

"""

@pytest.mark.parametrize('test_input', testcases)
class TestFactors:
    def test_loan_request(self, test_input):
        newrequest = LoanRequest(*test_input)
        newrequest.start_scoring()
        assert newrequest.scoring_result

