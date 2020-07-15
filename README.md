# Credit calculator
Credit calculator that works with different types of payment and to work with command-line arguments.

# About
Finance is an important part of the life of any people. Sometimes you think about getting additional income and want to open a deposit account. And sometimes you need additional money right now and want to take a credit or mortgage. Anyway, you may want to calculate different financial indicators to make a decision. Let’s make such an instrument that can help us.

# Description

Finally, let's add to our calculator the capacity to compute the differentiated payment. In such a kind of payment where the part for reducing the credit principal is constant. Another part of the payment is for interest repayment and it reduces during the credit term. It means that the payment is different each month. Let’s look at the formula:

Dm=Pn+i∗(P−P∗(m−1)n)D_m = \dfrac{P}{n} + i * \left( P - \dfrac{P*(m-1)}{n} \right) 

Dm = P / n + i ∗ (P − P∗(m−1)/n)

Where:

Dm = mth differentiated payment;

P = the credit principal;

i = nominal interest rate. Usually, it’s 1/12 of the annual interest rate. And usually, it’s a floating value, not a percentage. For example, if we our annual interest rate = 12%, then i = 0.01.

n = Number of payments. Usually, it’s the count of months.

m = current period.

As you can see, the user has to input a lot of parameters. So it might be convenient to use command-line arguments.

Using command-line arguments you can run your program this way:

```

python credit_calc.py --type=diff --principal=1000000 --periods=10 --interest=10

```

# Objectives

At this stage, it is required to implement these features:

    the calculation of differentiated payment. To do this, the user may run the program specifying interest, count of periods and credit principal.

    a capacity to calculate the same values as in the previous stage for annuity payment (principal, count of periods and value of the payment). A user specifies all known parameters with command-line arguments, while a single parameter will be unknown. This is the value the user wants to calculate.

    handling of invalid parameters. It's a good idea to show an error message Incorrect parameters in case of invalid parameters (they are discussed in detail below).

The final version of your program is supposed to work from the command line and parse the following parameters:

    --type, which indicates the type of payments: "annuity" or "diff" (differentiated). If --type is specified neither as "annuity" nor as "diff", or it is not specified at all, show the error message.

    > python credit_calc.py --principal=1000000 --periods=60 --interest=10
    Incorrect parameters

    --payment, that is a monthly payment. For --type=diff the payment is different each month, so we can't calculate periods or principal, therefore, its combination with --payment is invalid, too:

    > python credit_calc.py --type=diff --principal=1000000 --interest=10 --payment=100000
    Incorrect parameters

    --principal is used for calculations of both types of payment. You can get its value knowing the interest, annuity payment and periods.
    --periods parameter denotes the number of months and/or years needed to repay the credit. It's calculated based on the interest, annuity payment and principal.
    --interest is specified without a percent sign. Note that it may accept a floating-point value. Our credit calculator can't calculate the interest, so these parameters are incorrect:

    > python credit_calc.py --type=annuity --principal=100000 --payment=10400 --periods=8
    Incorrect parameters

Let's make a comment. You might have noticed that for differentiated payments you will need 4 out of 5 parameters (excluding payment), and the same is true for annuity payments (missing either periods, payment or principal). Thus, when less than four parameters are given, you should display the error message too:

> python credit_calc.py --type=annuity --principal=1000000 --payment=104000
Incorrect parameters

Another case when you should output this message is negative values. We can't work with these!

> python credit_calc.py --type=diff --principal=30000 --periods=-14 --interest=10
Incorrect parameters

Finally, don't forget to compute the value of overpayment, and you'll have your real credit calculator!

### This project is a part of the following track Python Developer of JetBrains Academy
