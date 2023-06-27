class Database:
    def __init__(self):
        self.accts = {'ACCT100': {'paid': 100, 'due': 200}, 'ACCT200': {'paid': 300, 'due': 350}}

    def neededdata(self, acct_input):
        acct_output = self.accts.get(acct_input)
        if acct_output:
            return int(acct_output['paid']) - int(acct_output['due'])
        return None