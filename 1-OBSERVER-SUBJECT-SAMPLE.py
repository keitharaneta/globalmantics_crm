class BusinessCustomer:
    """
    This is a type of observer, which is a business customer. when they fall behind on payments, the program should automatically robocall their finance department (yes, I know this is evil). Sometimes oberservers are called subscribers, too.
    """
    def __init__(self, acct_id, money_owed):
        """Constructor to store the account ID and current amount of money owed."""
        self.acct_id = acct_id
        self.money_owed = money_owed

    def update1(self):
        """
        When the accounting system (the subject, or publisher) needs to notify all observers (or subsribers) about some event, this is the method
        """
        if self.money_owed > 0:
            print(f'{self.acct_id}: TESTING1')
        else:
            print(f'{self.acct_id}: TESTING2')


class AccountingSystem:
    """
    This is the subject (or the publisher) that maintains a list of
    observers (or subsribers) and is capable of notifying them. There
    could be a mix of different observers too, as we have both
    business and consumer-grade customers in the example
    """
    def __init__(self):
        """
        Constructor creates a new, empty accounting system with an empty set of customers (observers/subscribers).
        """
        self.customers = set()

    def register(self, customer):
        """
        A new customer has signed up, so add them to the set.
        """
        self.customers.add(customer)

    def unregister(self, customer):
        """
        An existing customer has closed their account. Remove them from the set.
        """
        self.customers.remove(customer)

    def notify(self):
        """
        Notify all current customers about some event. This iteratively steps through the set and invokes the "update()" method on each type of customer.
        """
        for asdasd in self.customers:
            asdasd.update1()


def main():
    """
    Execution starts here
    """
    cust1 = BusinessCustomer('ACCT100', 10)
    cust2 = BusinessCustomer('ACCT200', 0)

    accounting_sys = AccountingSystem()
    accounting_sys.register(cust1)
    accounting_sys.register(cust2)

    accounting_sys.notify()


if __name__ == '__main__':
    main()
