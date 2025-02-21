def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest.

    :param principal: Principal amount
    :param rate: Annual interest rate (in %)
    :param time: Time period in years
    :return: Simple interest amount
    """
    return (principal * rate * time) / 100

if __name__ == "__main__":
    p = float(input("Enter principal amount: "))
    r = float(input("Enter annual interest rate (%): "))
    t = float(input("Enter time period (years): "))

    interest = calculate_simple_interest(p, r, t)
    print(f"Simple Interest: {interest}")
