# FutureValue.py
# A program to compute the value of an investment
# carried 10 years into the future.


def main():
    # Print an introduction
    print('This program will calculate the value in 10 years',
          'given the principal and interest rate (APR)')

    # Input principal
    principal = eval(input("Enter the value of the principal: "))

    # Input APR
    apr = eval(input("Enter the interest rate (APR): "))

    # Calculate increase over 10 years
    for i in range(10):
        principal = principal * (1 + apr)

    # Output final value
    print('The value in 10 years i:', principal)

main()
