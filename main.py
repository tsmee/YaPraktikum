from LoanRequest import LoanRequest
from DataValidation import DataValidation

"""
Простая функция, которая принимает заявку на кредит,
скрывая детали реализации.
Формат заявки - словарь. Пример формата внизу.
"""

def scoring(request_dict):
    validation_errors = DataValidation(request_dict).validate()
    if validation_errors:
        print("what")
        return validation_errors
    else:
        new_scoring = LoanRequest(**request_dict)
        new_scoring.start_scoring()
        print(new_scoring.scoring_result)



x = {
    "gender": "F",                                      # пол "F"/"M"
    "age": 30,                                          # Возраст [not negative int], лет
    "loan_years": 5,                                    # Источник дохода [пассивный доход, наёмный работник, собственный бизнес, безработный]
    "income_source": "PASSIVE_INCOME",                  # "BUSINESS_OWNER", "EMPLOYEE", "PASSIVE_INCOME", "UNEMPLOYED"]
    "loan_amount": 5.5,                                 # Запрошенная сумма [0.1 .. 10], млн
    "annual_income": 1,                                 # Доход за последний год [int], млн
    "loan_purpse": "CONSUMER",                         # Цель займа ["MORTGAGE", "BUSINESS", "CONSUMER"]
    "credit_score": 2                                   # Кредитный рейтинг [-2, -1, 0, 1, 2]
}
scoring(x)