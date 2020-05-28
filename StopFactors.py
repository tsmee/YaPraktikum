class StopFactors:

    __pension_age = {"M": 65, "F": 60}      #В РФ возраст выхода на пенсию записит от пола

    def __init__(self, gender, age, loan_years, approved_loan_amount, annual_income, credit_score, stake,
                 approved_loan_annual_payment, income_source):

        self.gender = gender
        self.age = age
        self.loan_years = loan_years
        self.approved_loan_amount = approved_loan_amount
        self.annual_income = annual_income
        self.credit_score = credit_score
        self.stake = stake
        self.approved_loan_annual_payment = approved_loan_annual_payment
        self.rejection_reasons = []
        self.income_source = income_source
    """
    Если возраст превышает пенсионный возраст на момент возврата кредита --> кредит не выдаётся 
    """
    def is_too_old(self):
        retire_age = self.__pension_age[self.gender]
        loan_repayed_age = self.age + self.loan_years
        if loan_repayed_age > retire_age:
            self.rejection_reasons.append("TooOld")

    #Если результат деления запрошенной суммы на срок
    # погашения в годах более трети годового дохода -->
    def is_sum_too_big(self):
        if (self.approved_loan_amount/self.loan_years) > (self.annual_income/3):
            self.rejection_reasons.append("SumIsTooBig")

    #Если кредитный рейтинг -2
    def is_lowest_score(self):
        if self.credit_score == -2:
            self.rejection_reasons.append("LowCreditScore")


    #Если в источнике дохода указано "безработный"
    def is_unemployed(self):
        if self.income_source == 'UNEMPLOYED':
            self.rejection_reasons.append("IsUnemployed")


    #Если годовой платёж (включая проценты) больше половины дохода
    def is_payment_too_big(self):
        if self.approved_loan_annual_payment > self.annual_income/2:
            self.rejection_reasons.append("PaymentIsTooBig")

    #Запуск всех проверок, возвращается список найденных, либо пустой
    def check_stop_factors(self):
        self.is_too_old()
        self.is_sum_too_big()
        self.is_lowest_score()
        self.is_unemployed()
        self.is_payment_too_big()
        return self.rejection_reasons

