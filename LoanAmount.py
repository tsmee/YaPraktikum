class LoanAmount:

    LIMIT_INCOME_SOURCE = {
        "PASSVIE_INCOME": 1,
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

    def __init__(self, income_source: str, credit_score: int,
                 requested_loan_amount: int, approved_loan_amount):
        self.income_source = income_source
        self.credit_score = credit_score
        self.requseted_loan_amount = requested_loan_amount
        self.approved_loan_amount = approved_loan_amount
        self.limits = []

    def calculate_approved_loan_amount(self):
        self.limits.append(self.LIMIT_INCOME_SOURCE[self.income_source])
        self.limits.append((self.LIMIT_CREDIT_SCORE[self.credit_score]))
        loan_limit = min(self.limits)
        if self.requseted_loan_amount < loan_limit:
            self.approved_loan_amount = self.requseted_loan_amount
        else:
            self.approved_loan_amount = loan_limit
