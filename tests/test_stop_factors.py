import pytest

from StopFactors import StopFactors
"""
Пример покрытия функциональных тестов на уровне юнитов.
Здесь: запускается проверка по анкете, с которой все ок (первая).
Затем по одному меняются значения аргументов, и срабатывают нужные стоп-факторы.
Формат: tuple, 
("F", 50, 1, 1, 10, -2, 8.75, 1.09, "BUSINESS_OWNER")
параметр крединого рейтинга поменялся на -2, поэтому в 
expected results ["LowCreditScore"]
"""

testcases = [(("F", 50, 1, 1, 10, -1, 8.75, 1.09, "BUSINESS_OWNER"), []),               #Все ок
             (("F", 60, 1, 1, 10, -1, 8.75, 1.09, "BUSINESS_OWNER"), ["TooOld"]),       #возраст превышает пенсионный возраст на момент возврата
             (("F", 50, 1, 1, 10, -2, 8.75, 1.09, "BUSINESS_OWNER"), ["LowCreditScore"]),#низкий кредитный рейтинг
             (("F", 50, 1, 1, 10, -1, 8.75, 1.09, "UNEMPLOYED"), ["IsUnemployed"]),     #UNEMPLOYED
             (("F", 50, 1, 4, 0.1, -1, 8.75, 1.09, "BUSINESS_OWNER"), ["SumIsTooBig", "PaymentIsTooBig"])] #Платежи сильно выше доходов




@pytest.mark.parametrize('test_input, expected', testcases)
class TestFactors:
    def test_factors(self, test_input, expected):
        newfactors = StopFactors(*test_input)
        reasons = newfactors.check_stop_factors()
        print(reasons)
        assert reasons == expected
