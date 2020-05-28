"""
Класс с логикой для расчета доступной к получению суммы.
"""

class LoanAmount:

    LIMIT_INCOME_SOURCE = {
        "PASSIVE_INCOME": 1,
        "EMPLOYEE": 5,
        "BUSINESS_OWNER": 10,
        "UNEMPLOYED": 0
    }

    LIMIT_CREDIT_SCORE = {
        -2: 0,
        -1: 1,
        0: 5,
        1: 10,
        2: 10
    }

    def __init__(self, income_source, credit_score, requested_loan_amount, approved_loan_amount=0):

        self.income_source = income_source
        self.credit_score = credit_score
        self.requested_loan_amount = requested_loan_amount
        self.approved_loan_amount = approved_loan_amount
        self.limits = []


    """
    Вычисляем все приминимые ограничения на сумму. Если сумма заявки
    не больше ее, заявка одобряется полностью.
    Если больше, то одобряется сумма лимита.
    Если условия-блокеры, лимит будет 0.
    """
    def calculate_approved_loan_amount(self):
        self.limits.append(self.LIMIT_INCOME_SOURCE[self.income_source])
        self.limits.append((self.LIMIT_CREDIT_SCORE[self.credit_score]))
        loan_limit = min(self.limits)
        if self.requested_loan_amount < loan_limit:
            self.approved_loan_amount = self.requested_loan_amount
        else:
            self.approved_loan_amount = loan_limit
        return self.approved_loan_amount
