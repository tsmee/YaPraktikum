from math import log

"""
Логика расчета процентной ставки, вынесена в отдельный класс.
Параметры и константы вынесены в отдельный блок, для удобства,
если систему нужно было бы поддерживать и модифицировать.
"""

class LoanStake:

    BASE_STAKE = 10.0

    MOD_LOAN_PURPOSE = {
        "MORTGAGE": -2.0,
        "BUSINESS": -0.5,
        "CONSUMER": 1.5,
        "AUTO": 0               # для автокредита модификатора ставки нет
    }

    MOD_CREDIT_SCORE = {
        -1: 1.5,
        0: 0.0,
        1: -0.25,
        2: -0.75
    }

    MOD_INCOME_SOURCE = {
        "PASSIVE_INCOME": 0.5,
        "EMPLOYEE": -0.25,
        "BUSINESS_OWNER": 0.25
    }

    def __init__(self, loan_purpose: str, credit_score: int, requested_loan_amount: float,
                 income_source: str, approved_loan_stake=None):
        self.loan_purpose = loan_purpose
        self.credit_score = credit_score
        self.requested_loan_amount = requested_loan_amount
        self.income_source = income_source
        self.approved_loan_stake = approved_loan_stake

    """
    Вычисление ставки с учетом параметров. Нужные параметры подтякиваются
    через словари, ключ к которым получили из клиентской анкеты
    """

    def calculate_stake(self):
        loan_purpose_mod = self.MOD_LOAN_PURPOSE[self.loan_purpose]
        credit_score_mod = self.MOD_CREDIT_SCORE[self.credit_score]
        requested_loan_amount_mod = round(log(self.requested_loan_amount, 10)) * -1
        income_source_mod = self.MOD_INCOME_SOURCE[self.income_source]
        self.approved_loan_stake = round((self.BASE_STAKE + loan_purpose_mod + credit_score_mod + \
                                   requested_loan_amount_mod + income_source_mod), 2)
        return self.approved_loan_stake
