import pytest

from LoanAmount import LoanAmount
"""
Создаем экземпляр класса с логикой расчета суммы займа, 
и хотя бы по разу используем каждый из доступных параметров 
(Источник Дохода, Кредитный Рейтинг, Сумма займа.
"""
testcases = [('BUSINESS_OWNER', 2, 10),
             ('EMPLOYEE', 2, 10),
             ('PASSIVE_INCOME', 2, 10),
             ('UNEMPLOYED', 2, 10),
             ('BUSINESS_OWNER', 2, 10),
             ('BUSINESS_OWNER', 1, 10),
             ('BUSINESS_OWNER', 0, 10),
             ('BUSINESS_OWNER', -1, 10),
             ('BUSINESS_OWNER', -2, 10),
             ('BUSINESS_OWNER', 2, 0.1),
             ('BUSINESS_OWNER', 2, 4),
             ('BUSINESS_OWNER', 2, 8),
             ('BUSINESS_OWNER', 2, 9),
             ('BUSINESS_OWNER', 2, 9),
             ('BUSINESS_OWNER', 2, 10),
             ('BUSINESS_OWNER', 2, 1.2)]


@pytest.mark.parametrize('test_input', testcases)
class TestAmount:
    def test_amount(self, test_input):
        newloan = LoanAmount(*test_input)
        print(newloan.calculate_approved_loan_amount())
        assert True
