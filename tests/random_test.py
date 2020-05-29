import random

def get_random_test():
    g = ["M", "F"]
    gender = random.choice(g)
    age = random.randint(0, 70)
    period = random.randint(1, 20)
    inc = ["PASSIVE_INCOME", "EMPLOYEE", "BUSINESS_OWNER", "UNEMPLOYED"]
    income_source = random.choice(inc)
    loan_size = round(random.uniform(0,10), 2)
    income = random.randint(1, 1000)
    pr = ["MORTGAGE", "BUSINESS", "CONSUMER"]
    purpose = random.choice(pr)
    score = random.randint(-2, 2)
    return (gender, age, period, income_source, loan_size, income, purpose, score)

def generate_tests(tests_num):
    reqs = []
    n = 0
    while n < tests_num:
        reqs.append(get_random_test())
        n += 1
    return reqs



