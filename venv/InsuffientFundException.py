import BalancecheckException
class InsuffientFundException(Exception):

    def __init__(self, args):
        self.Exceptioninfo = args


withdraw_bal = int(input("enter the amount"))
acct_bal = 100000
if withdraw_bal > acct_bal:

    #raise bal("withdraw_bal>acct_bal")
    #raise InsuffientFundException("withdraw_bal>acct_bal")
    raise BalancecheckException("withdraw_bal>acct_bal")
else:

    print(acct_bal - withdraw_bal)