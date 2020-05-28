import pytest

from LoanStake import LoanStake

"""
Инстанцируем класс с логикой расчета Ставки с разными параметрами, и 
проверяем, что ставка совпадает с ожидаемой.
Формат тесткейса - tuple, (('CONSUMER', -1, 0.1, 'PASSIVE_INCOME'), 14.5)
Тесткейсы тут покрывают условие, что каждый из вариантов был хотя бы раз
"""
testcases = [(('CONSUMER', -1, 0.1, 'PASSIVE_INCOME'), 14.5), (('BUSINESS', -1, 0.1, 'PASSIVE_INCOME'), 13.5),
             (('MORTGAGE', -1, 0.1, 'PASSIVE_INCOME'), 11.0), (('CONSUMER', 0, 0.1, 'PASSIVE_INCOME'), 13.0),
             (('CONSUMER', -2, 0.1, 'PASSIVE_INCOME'), 13.0), (('CONSUMER', 1, 0.1, 'PASSIVE_INCOME'), 12.75),
             (('CONSUMER', 2, 0.1, 'PASSIVE_INCOME'), 12.25), (('CONSUMER', -1, 0.4, 'PASSIVE_INCOME'), 13.5),
             (('CONSUMER', -1, 3.27, 'PASSIVE_INCOME'), 12.5), (('CONSUMER', -1, 10.0, 'PASSIVE_INCOME'), 12.5),
             (('CONSUMER', -1, 0.1, 'BUSINESS_OWNER'), 14.25), (('CONSUMER', -1, 0.1, 'UNEMPLOYED'), 14.0),
             (('CONSUMER', -1, 0.1, 'EMPLOYEE'), 13.75)]



@pytest.mark.parametrize('test_input, expected', testcases)
class TestStake:
    def test_stake(self, test_input, expected):
        new_stake = LoanStake(*test_input)
        stake_val = new_stake.calculate_stake()
        print(stake_val)
        assert stake_val == expected

