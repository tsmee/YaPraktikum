from LoanRequest import LoanRequest
from tests.random_test import generate_tests
import pytest

testcases = generate_tests(5000)

"""
Тесты для класса LoanRequest и запуска скоринга.
В модуле random_tests генерируются случайные валидные данные, 
с ними запускается скоринг. Результат прогоняется через 
is_valid(), там любые проверки.
Инструмент для поиска неочевидных багов с комбинаторикой.
Ошибки в отчете выглядят так:
FAILED [  2%]('M', 20, 20, 'BUSINESS_OWNER', 9.71, 112, 'CONSUMER', 2)
result = {'Amount': 9.71, 'Annual Payment': 1.46, 'Decision': 'Approved', 'Stake': 10.0}
assert result['Amount'] <= 9
assert 9.71 <= 9
"""


def is_valid(result):
    assert result['Decision'] in ['Approved', 'Rejected']
    if result['Decision'] == 'Approved':
        assert result['Amount'] > 0
        assert result['Amount'] <= 9                # Чтобы иногда фейлились кейсы с > 9
        assert result['Stake'] <= 14.5
    if result['Decision'] == 'Rejected':
        assert result['RejectionReasons']
    return True

def idfn(val):
    return val


@pytest.mark.parametrize('test_input', testcases, ids=idfn)
class TestFactors:
    def test_loan_request(self, test_input):
        print(test_input)
        newrequest = LoanRequest(*test_input)
        newrequest.start_scoring()
        responce = newrequest.scoring_result
        assert is_valid(responce)




