from math import ceil, log, floor
import argparse
import sys


class CreditCalculator:
    STATES = ['count_months', 'monthly_payment', 'credit_principal', 'waiting']
    TYPES = ['annuity', 'diff']

    def __init__(self):
        self.credit = 0
        self.state = None

    def get_differentiated_payment(self, interest, payments_number, current_period):

        nominal_interest = self.get_nominal_interest(interest)
        term_1 = self.credit / payments_number
        term_2 = self.credit - (self.credit * ((current_period - 1) / payments_number))

        return ceil(term_1 + nominal_interest * term_2)

    def get_annuity_payment(self, interest, payments_number):
        nominal_interest = self.get_nominal_interest(interest)
        numerator = (nominal_interest * (1 + nominal_interest) ** payments_number)
        denominator = ((1 + nominal_interest) ** payments_number - 1)

        return ceil(self.credit * numerator / denominator)

    def get_credit_principal(self, annuity_payment, interest, payments_number):
        nominal_interest = self.get_nominal_interest(interest)
        numerator = (nominal_interest * (1 + nominal_interest) ** payments_number)
        denominator = ((1 + nominal_interest) ** payments_number - 1)

        return annuity_payment / (numerator / denominator)

    def get_payments_number(self, credit_principal, annuity_payment, interest):
        value = annuity_payment / (annuity_payment - interest * credit_principal)
        return log(value, 1 + interest)

    def year_month_calculation(self, payment, interest):
        nominal_interest = self.get_nominal_interest(interest)
        payments_number = self.get_payments_number(self.credit, payment, nominal_interest)
        years, months = divmod(ceil(payments_number), 12)
        plural_months = ''
        plural_years = ''

        if months > 1:
            plural_months = 's'
        if years > 1:
            plural_years = 's'

        if months > 0 and years == 0:
            print('You need {} month{} to repay this credit!'.format(months, plural_months))
        elif months == 0 and years > 0:
            print('you need {} year{} to repay this credit!'.format(years, plural_years))
        else:
            print("You need {} year{} month{} to repay this credit!".format(years, plural_years, months, plural_months))
        return ceil(payments_number)

    def enter_credit(self, credit):
        self.credit = credit

    def get_nominal_interest(self, interest):
        return interest / (12 * 100)

    def negative_arguments(self, arg):
        return args.principal and args.principal < 0 \
               or args.periods and arg.periods < 0 \
               or args.interest and args.interest < 0 \
               or args.payment and args.payment < 0

    def start(self, args):
        self.credit = args.principal
        args_values = vars(args).values()
        n_values = sum([1 for v in args_values if v])
        if n_values != 4 or args.type not in CreditCalculator.TYPES \
                or args.type == CreditCalculator.TYPES[1] and args.payment \
                or not args.interest or self.negative_arguments(args):
            print("Incorrect parameters")
        elif args.type == CreditCalculator.TYPES[0]:
            if args.principal:
                if args.periods:
                    annuity_payment = self.get_annuity_payment(args.interest, args.periods)
                    overpayment = annuity_payment * args.periods - self.credit
                    print('Your annuity payment = {}!'.format(annuity_payment))
                    print('Overpayment = {}'.format(overpayment))
                elif args.payment:
                    months = self.year_month_calculation(args.payment, args.interest)
                    print('Overpayment = {}'.format(args.payment * months - self.credit))

            elif args.periods:
                credit_principal = self.get_credit_principal(args.payment, args.interest, args.periods)
                original_credit = args.payment * args.periods
                print('Your credit principal = {}!'.format(floor(credit_principal)))
                print('Overpayment = {}'.format(ceil(original_credit - credit_principal)))

            else:
                print('Error Annuity')
        elif args.type == CreditCalculator.TYPES[1]:
            month_payments = [self.get_differentiated_payment(args.interest, args.periods, i) for i in
                              range(1, args.periods + 1)]

            for i, payments in enumerate(month_payments):
                print('Month {}: paid out {}'.format(i+1, payments))
            print('Overpayment = {}'.format(sum(month_payments) - self.credit))
        else:
            print('Start error')


if __name__ == '__main__':
    my_bank = CreditCalculator()

    parser = argparse.ArgumentParser()
    parser.add_argument('--principal', type=float)
    parser.add_argument("--type", type=str)
    parser.add_argument('--periods', type=int)
    parser.add_argument('--interest', type=float)
    parser.add_argument('--payment', type=float)

    args = parser.parse_args()
    my_bank.start(args)
