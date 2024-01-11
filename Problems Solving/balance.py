def Balance(bal, rate, years):
    finalBalance = bal * ( 1 + rate / 100) ** years
    return finalBalance

print(Balance(1000, 6, 2))