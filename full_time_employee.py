#full time employee

def full_time_employee():
    hours = int(input("Please enter the nuber of hours you have worked: "))
    rate_of_pay = float(input("Please enter your hourly rate of pay: "))
    overtime = int(input("Please enter the number of over time hours worked: "))
    overtime_pay_rate = float(input("Please enter your overtime pay rate: "))
    return hours, rate_of_pay, overtime, overtime_pay_rate

def total_pay(hours, rate_of_pay, overtime, overtime_pay_rate):
    standard_pay = hours * rate_of_pay
    overtime_pay = overtime * overtime_pay_rate
    total_pay = overtime_pay + standard_pay
    return total_pay

def full_time_main():
    hours, rate_of_pay, overtime, overtime_pay_rate = full_time_employee()
    totalPay = total_pay(hours, rate_of_pay, overtime, overtime_pay_rate)
    print("Total pay = £{0}".format(totalPay))

if __name__ == "__main__":
    full_time_main()
