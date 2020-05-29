# loan_purpose_params = [["CONSUMER", 0.0], ["BUSINESS", -1.0], ["MORTGAGE", -3.5]]
# credit_score_params = [[-1, 0.0], [0, -1.5], [-2, -1.5], [1, -1.75], [2, -2.25]]
# loan_request_params = [[0.1, 0.0], [0.4, -1.0], [3.27, -2.0], [10.0, -2.0]]
# loan_income_params = [["PASSIVE_INCOME", 0.0], ["BUSINESS_OWNER", -0.25], ["UNEMPLOYED", -0.5], ["EMPLOYEE", -0.75]]
#
#
#
# default_params = ("MORTGAGE", 2, 10, "EMPLOYEE")
# default_stake = 14.5
#
# def loan_stake_generator(purpose="CONSUMER", score="-1", amount="0.1", income="PASSIVE_INCOME"):
#     tests = []
#     template = '("{}", {}, {}, "{}")'.format(purpose, score, amount, income)
#     for n in loan_purpose_params:
#         stake = 14.5 + n[1]
#         zzz = ((n[0], -1, 0.1, "PASSIVE_INCOME"), stake)
#         tests.append(zzz)
#
#     for n in credit_score_params:
#         stake = 14.5 + n[1]
#         zzz = (("CONSUMER", n[0], 0.1, "PASSIVE_INCOME"), stake)
#         if zzz not in tests:
#             tests.append(zzz)
#
#     for n in loan_request_params:
#         stake = 14.5 + n[1]
#         zzz = (("CONSUMER", -1, n[0], "PASSIVE_INCOME"), stake)
#         if zzz not in tests:
#             tests.append(zzz)
#
#     for n in loan_income_params:
#         stake = 14.5 + n[1]
#         zzz = (("CONSUMER", -1, 0.1, n[0]), stake)
#         if zzz not in tests:
#             tests.append(zzz)
#     print(tests)
#
#
# def req_generator(income="BUSINESS_OWNER", score=2, sum=10):
#     req = (income, score, sum)
#     print(req)
#
# inc = ["BUSINESS_OWNER", "EMPLOYEE", "PASSIVE_INCOME", "UNEMPLOYED"]
# sc = [2,1,0,-1,-2]
# sm = [0.1, 1.2, 4, 8, 9,9, 10]
#
# for i in inc:
#     req_generator(income=i)
# for s in sc:
#     req_generator(score=s)
#
# for m in sm:
#     req_generator(sum=m)
#
#
