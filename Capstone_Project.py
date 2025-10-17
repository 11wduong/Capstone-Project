welcome_message = """ === FUTURE VALUE CALCULATOR === 

Welcome to the future value calculator. You will need:
-   Present Value of your investment.
-   Rate of Return
-   Number of Years you will hold it for
    
Please type \"Exit\" at any point to quit.

"""

print(welcome_message)


def get_numerical_input(prompt):

    while True:
        user_input = input(prompt).strip()

        if user_input.lower() == "exit":
            print("Exiting Program")
            raise SystemExit

        try:
            value = float(user_input)
            return value
        except ValueError:
            error_message = ("""
Invalid input! Please enter a numerical value.
            """)
            print(error_message)


pv = get_numerical_input("State the Present Value (£): ")
r_percent = get_numerical_input("State the Rate of Return (Percentage): ")
n = get_numerical_input("State the Number of Periods (Years): ")

r = r_percent / 100


def fv_calc(pv, r, n):
    fv = pv * (1 + r)**n
    return fv


fv = fv_calc(pv, r, n)
print(f"The Future Value Of Your Investment Is: £{fv:2f}")
