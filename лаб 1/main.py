income = []
sum_ = 0
for i in range(12):
    month_income = float(input())
    income.append(month_income)
    sum_ += month_income
    if i == 0:
        max_ = month_income
        min_ = month_income
    max_ = max(income)
    min_ = min(income)

average = sum_ / 12
more_than_average = []

for i in income:
    if i > average:
        more_than_average.append(i)

print(income, sum_, max_, min_, average, more_than_average, sep='\n')