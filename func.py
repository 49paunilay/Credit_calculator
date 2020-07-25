import math
import argparse

parser=argparse.ArgumentParser()
# setting as optional arguments
parser.add_argument("--type")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
parser.add_argument("--payment")
args=parser.parse_args()
"""
print('''
What do you want to calculate? 
type "n" - for count of months, 
type "a" - for annuity monthly payment,
type "p" - for credit principal:
''')
"""
if len(vars(args))>=4:
    if not args.type:
        print('Incorrect parameters')
    elif args.type=='annuity':
        if args.principal and args.payment and args.interest:
            #print('Enter credit principal:')
            credit_principle=float(args.principal)
            #print('Enter monthly payment:')
            monthly_payment=int(args.payment)
            #print('Enter credit interest')
            credit_interest=float(args.interest)
            nominal_interest=credit_interest/(12*100)
            mysum=monthly_payment/(monthly_payment-(nominal_interest*credit_principle))
            periods=math.ceil(math.log(mysum,1+nominal_interest))
            periods_year=periods//12
            periods_month=periods%12
            overpayment=(monthly_payment*periods)-credit_principle
            if periods_year==0:
                print(f'You need {periods_month} months to repay this credit!')
            elif periods_month==0:
                print(f'You need {periods_year} years to repay this credit!')
            else:
                print(f'You need {periods_year} years and {periods_month} months to repay this credit!')
            print('Overpayment = ' + str(math.ceil(overpayment)))
        elif args.principal and args.periods and args.interest and not args.payment:
            #print('Enter credit principal:')
            credit_principle=float(args.principal)
            #print('Enter count of periods:')
            periods=int(args.periods)
            #print('Enter credit interest:')
            credit_interest=float(args.interest)
            nominal_interest=credit_interest/(12*100)
            upper=nominal_interest*math.pow((1+nominal_interest),periods)
            lower=math.pow((1+nominal_interest),periods)-1
            annuity_payment=math.ceil((credit_principle*upper)/lower)
            overpayment=(periods*annuity_payment)-credit_principle
            print(f'Your annuity payment = {annuity_payment}!')
            print('Overpayment = '+str(overpayment))
        elif args.payment and args.periods and args.interest:
            #print('Enter monthly payment:')
            monthly_payment=float(args.payment)
            #print('Enter count of periods:')
            periods=float(args.periods)
            #print('Enter credit interest:')
            credit_interest=float(args.interest)
            nominal_interest=credit_interest/(12*100)
            #print(nominal_interest)
            upper=nominal_interest* (math.pow((1+nominal_interest),periods))
            #print(upper)
            lower= (math.pow((1+nominal_interest),periods))-1
            #print(lower)
            resultant=upper/lower
            principle=math.ceil(monthly_payment/resultant) -1 
            overpayment=(periods*monthly_payment)-principle 
            print(f'Your credit principal = {principle}!')
            print('Overpayment = ' + str(math.ceil(overpayment)))

    if args.type=='diff' and int(args.periods)>0:
        principle=float(args.principal)
        periods=int(args.periods)
        interest=float(args.interest)
        i=interest/(100*12)
        total=0
        for m in range(1,periods+1):
            dis_payment=(principle/periods)+i*(principle-(principle*(m-1))/periods)
            total=total+dis_payment
            print(math.ceil(dis_payment))
        print(math.ceil(total-principle))
    else:
        print('Incorrect parameters')
else:
    print('Incorrect parameters')


