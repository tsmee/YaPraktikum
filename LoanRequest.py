from LoanAmount import LoanAmount
from LoanStake import LoanStake
from StopFactors import StopFactors

"""
Основной класс. Через него происходит инициализация данными заявки на кредит,
запуск остальных классов, и запуск процесса скоринга
"""

class LoanRequest(LoanStake, LoanAmount, StopFactors):
    def __init__(self, gender, age, loan_years, income_source, loan_amount,
                 annual_income, loan_purpose, credit_score):
        self.age = age
        self.gender = gender
        self.income_source = income_source
        self.annual_income = annual_income
        self.credit_score = credit_score
        self.requested_loan_amount = loan_amount
        self.loan_years = loan_years
        self.loan_purpose = loan_purpose
        self.approved_loan_stake = 0
        self.approved_loan_amount = 0
        self.approved_loan_annual_payment = 0
        self.rejection_reasons = []
        self.scoring_result = {}

        LoanStake.__init__(self, loan_purpose, credit_score,
                           loan_amount, income_source, self.approved_loan_stake)

        LoanAmount.__init__(self, self.income_source, credit_score, loan_amount,
                            self.approved_loan_amount)

        StopFactors.__init__(self, gender, age, loan_years, self.approved_loan_amount, annual_income, credit_score,
                             self.approved_loan_stake, self.approved_loan_annual_payment, income_source)

    """
    
    Метод для расчета Годового платежа по кредиту 
    <сумма кредита> * (1 + <срок погашения> * (<базовая ставка> + <модификаторы>))) / <срок погашения>
    """
    def calculate_annual_payment(self):
        self.approved_loan_annual_payment = (self.approved_loan_amount * (1.0 + (float(self.loan_years) * (self.approved_loan_stake/100.0)))) / (float(self.loan_years))
        self.approved_loan_annual_payment = round(self.approved_loan_annual_payment, 2)
        print(self.approved_loan_annual_payment)

    """
    Метод, запускающий скоринг. Процесс идет последовательно: 
    1) Расчитывается максимально доступная сумма (теоретически)
    2) Расчитывается ставка
    3) Вычисляется ежегодный платеж
    4) Запускается проверка стоп-факторов, при которых всегда отказ. Если 
    список rejection_reasons вернулся пустым - кредит одобрен. Если есть одна или  несколько 
    - отказ.
    """
    def start_scoring(self):
        self.calculate_approved_loan_amount()
        self.calculate_stake()
        self.calculate_annual_payment()
        self.check_stop_factors()
        if self.rejection_reasons:
            self.scoring_result['Decision'] = "Rejected"
            self.scoring_result['RejectionReasons'] = self.rejection_reasons

        else:
            self.scoring_result['Decision'] = "Approved"
            self.scoring_result['Amount'] = self.approved_loan_amount
            self.scoring_result['Stake'] = self.approved_loan_stake
            self.scoring_result['Annual Payment'] = self.approved_loan_annual_payment
        return self.scoring_result

"""
Примеры работы скоринга (отказ с причинами и одобрение с условиями продукта.
{"Decision": "Rejected", "RejectionReasons": ["LowCreditScore", "IsUnemployed"]}
{"Decision": "Approved", "Amount": 1.35, "Stake": 7.0, "Annual Payment": 0.24}
"""














