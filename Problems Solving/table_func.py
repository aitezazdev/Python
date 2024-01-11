def table():
    initial_balance = float(input("Enter initial balance : "))
    num_years = float(input("Enter no. of years : "))

    lis = [-6, -3, 0, 3, 6]

    print("initial balance is %0.2f" % initial_balance)

    for rate in lis:
        final_balance = initial_balance * (1 + rate / 100) ** num_years
        print("rate {}%, final balance {:.2f}".format(rate, final_balance))

table()