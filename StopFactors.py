class StopFactors:

    __pension_age = {"M": 65, "F": 60}

    def __init__(self, gender, age, loan_years, approved_loan_amount, annual_income,
                 credit_score, stake, approved_loan_annual_payment, rejection_reasons, income_source):
        self.gender = gender
        self.age = age
        self.loan_years = loan_years
        self.approved_loan_amount = approved_loan_amount
        self.annual_income = annual_income
        self.credit_score = credit_score
        self.stake = stake
        self.approved_loan_annual_payment = approved_loan_annual_payment
        self.rejection_reasons = rejection_reasons
        self.income_source = income_source

    def is_too_old(self):
        retire_age = self.__pension_age[self.gender]
        loan_repayed_age = self.age + self.loan_years
        if loan_repayed_age > retire_age:
            self.rejection_reasons.append("TooOld")

    def is_sum_too_big(self):
        if (self.approved_loan_amount/self.loan_years) > (self.annual_income/3):
            self.rejection_reasons.append("SumIsTooBig")

    def is_lowest_score(self):
        if self.credit_score == -2:
            self.rejection_reasons.append("LowCreditScore")

    def is_unemployed(self):
        if self.income_source == 'UNEMPLOYED':
            self.rejection_reasons.append("IsUnemployed")

    def is_payment_too_big(self):
        if self.approved_loan_annual_payment > self.annual_income/2:
            self.rejection_reasons.append("PaymentIsTooBig")

    def check_stop_factors(self):
        self.is_too_old()
        self.is_sum_too_big()
        self.is_lowest_score()
        self.is_unemployed()
        self.is_payment_too_big()
