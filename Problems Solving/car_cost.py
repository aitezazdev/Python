# Calculate the cost of owning a car for 10 years. Assume a  purchase price of £10,000, a price of £4 per gallon of petrol, a  usage of 15,000 miles per year and a fuel efficiency of 20 miles  per gallon.

annual_fuel_consumed = 15000 / 20
annual_fuel_cost = 4 * annual_fuel_consumed
operating_cost = 10 * annual_fuel_cost
total_cost = 10000 + operating_cost

print("total Cost : ", total_cost)