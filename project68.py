from dataclasses import dataclass, field

@dataclass
class TransactionHistory:
    transactions: list

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_transaction_history(self):
        return self.transactions


@dataclass
class BankAccount:
    account_id: str
    __balance: float
    transaction_history: TransactionHistory = field(init=False)

    def __post_init__(self):
        self.transaction_history = TransactionHistory([])

    def check_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        self.transaction_history.add_transaction(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        self.transaction_history.add_transaction(f"Withdrew {amount}")
        
    def _update_balance(self, new_balance):
        self.__balance = new_balance



@dataclass
class SavingsAccount(BankAccount):
    interest_rate: float = 0

    def apply_interest(self):
        interest = self.check_balance() * self.interest_rate
        self._update_balance(self.check_balance() + interest)
        self.transaction_history.add_transaction(f"Interest applied: {interest}")


@dataclass
class CurrentAccount(BankAccount):
    overdraft_limit: float = 500

    def withdraw(self, amount):
        if self.check_balance() - amount < -self.overdraft_limit:
            raise ValueError("This withdrawal exceeds your overdraft limit")
        self._update_balance(self.check_balance() - amount)
        self.transaction_history.add_transaction(f"Withdrew {amount}")
        if self.check_balance() < 0:
            self.apply_overdraft_fee()

    def apply_overdraft_fee(self):
        fee = -self.check_balance() * 0.05
        self._update_balance(self.check_balance() - fee)
        self.transaction_history.add_transaction(f"Overdraft fee: {fee}")



@dataclass
class Customer:
    customer_id: str
    name: str
    address: str
    contact_num: str
    bank_accounts: list = field(default_factory=list)
    events: list = field(default_factory=list)
    
    def add_bank_account(self, account):
        self.bank_accounts.append(account)
        
    def subscribe(self, event):
        self.events.append(event)


@dataclass
class BankEvent:
    title: str
    date: str
    
    def party(self):
        return f"Welcome to {self.title} event on {self.date}"


if __name__ == "__main__":
    # إنشاء العميل
    customer = Customer(
        customer_id="CUST1001",
        name="Ali Al-Awjan",
        address="Al-Ahsa, Saudi Arabia",
        contact_num="0501234567" # غير حقيقي
    )

    # إنشاء حساب توفير
    savings = SavingsAccount(
        account_id="SA001",
        _BankAccount__balance=1000.0,  # استخدام name mangling
        interest_rate=0.05
    )

    # إنشاء حساب جاري
    current = CurrentAccount(
        account_id="CA001",
        _BankAccount__balance=500.0,
        overdraft_limit=300.0
    )

    # ربط الحسابات بالعميل
    customer.add_bank_account(savings)
    customer.add_bank_account(current)

    # إجراء عمليات على حساب التوفير
    savings.deposit(200)                     # الرصيد = 1200
    savings.withdraw(150)                   # الرصيد = 1050
    savings.apply_interest()                # 5% = +52.5 => الرصيد = 1102.5

    # إجراء عمليات على الحساب الجاري
    current.withdraw(600)                   # الرصيد = -100
    current.deposit(50)                     # الرصيد = -50

    # الاشتراك في فعالية
    event = BankEvent(title="Customer Appreciation Day", date="2025-08-01")
    customer.subscribe(event)

    # طباعة النتائج
    print("="*40)
    print(f"Customer: {customer.name}")
    print(f"Number of Accounts: {len(customer.bank_accounts)}")
    print(f"Subscribed Events: {[e.title for e in customer.events]}")
    print("="*40)

    # طباعة تفاصيل حساب التوفير
    print("Savings Account Balance:", savings.check_balance())
    print("Savings Transactions:")
    for t in savings.transaction_history.get_transaction_history():
        print("-", t)

    print("="*40)

    # طباعة تفاصيل الحساب الجاري
    print("Current Account Balance:", current.check_balance())
    print("Current Transactions:")
    for t in current.transaction_history.get_transaction_history():
        print("-", t)

    print("="*40)
    # طباعة رسالة الفعالية
    print(event.party())
