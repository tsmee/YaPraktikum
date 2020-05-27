
import json
from LoanAmount import LoanAmount
from LoanStake import LoanStake
from StopFactors import StopFactors


class LoanRequest(LoanStake, LoanAmount, StopFactors):
    def __init__(self, age: int, gender: str, income_source: str, annual_income: int, credit_score: int,
                 requested_loan_amount: int, loan_years: int, loan_purpose: str):
        self.age = age
        self.gender = gender
        self.income_source = income_source
        self.annual_income = annual_income
        self.credit_score = credit_score
        self.requested_loan_amount = requested_loan_amount
        self.loan_years = loan_years
        self.loan_purpose = loan_purpose
        self.approved_loan_stake = None
        self.approved_loan_amount = None
        self.approved_loan_annual_payment = None
        self.rejection_reasons = []
        self.scoring_result = {}

        LoanStake.__init__(self, loan_purpose, credit_score,
                 requested_loan_amount, income_source, self.approved_loan_stake)
        LoanAmount.__init__(self, income_source, credit_score, requested_loan_amount,
                            self.approved_loan_amount)

        StopFactors.__init__(self, gender, age, loan_years, self.approved_loan_amount, annual_income,
                 credit_score, self.approved_loan_stake, self.approved_loan_annual_payment, self.rejection_reasons, income_source)


    def calculate_annual_payment(self):
        self.approved_loan_annual_payment = (self.approved_loan_amount * (1.0 + (float(self.loan_years) * (self.approved_loan_stake/100.0)))) / (float(self.loan_years))
        self.approved_loan_annual_payment = round(self.approved_loan_annual_payment, 2)
        print(self.approved_loan_annual_payment)

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
        app_json = json.dumps(self.scoring_result)
        print(app_json)
        return self.scoring_result


req1 = LoanRequest(35, "F", "EMPLOYEE", 2, -1, 4, 12, "CONSUMER")

req1.start_scoring()









