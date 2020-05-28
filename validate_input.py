__KEYS = ['gender', 'age', 'loan_years', 'income_source', 'loan_amount', 'annual_income', 'loan_purpose',
          'credit_score']
"""
Модуль для проверки входных данных
"""

def validating_data(payload):
    if not isinstance(payload, dict):
        print("Wrong data type")
        return False
    assert set(payload.keys()) == set(__KEYS)
    assert payload['gender'] in ["F", "M"]
    assert type(payload['annual_income']) == 'int'

    return True
