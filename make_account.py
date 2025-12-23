def make_account(initial_balance):
    """
    that creates and returns two functions representing operations on a bank account:

    a function for depositing money,

    a function for withdrawing money.

    The account balance must be initialized using initial_balance and must persist betwen function calls.

    The following rules apply;

    Deposits and withdrawals must use positive numeric values.

    The account balance must never become negative.

    Invalid operations must raise appropriate Python exceptions.

    The account balance must not be directly accessible from outside the returned functions.
    
    """
    
    if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
        raise ValueError("Initial balance must be a non-negative number")
    
    balance = initial_balance  
    
    def deposit(amount):
        nonlocal balance
        
        if not isinstance(amount, (int, float)):
            raise TypeError('Deposit amount must be a number')
            
        if amount <= 0:
            raise ValueError('Deposit amount must be positive')
        
        balance += amount
        return balance
    
    def withdraw(amount):
        nonlocal balance
        
        if not isinstance(amount, (int, float)):
            raise TypeError('Withdrawal amount must be a number')
            
        if amount <= 0:
            raise ValueError('Withdrawal amount must be positive')
            
        if amount > balance:
            raise ValueError('Insufficient funds')
        
        balance -= amount
        return balance
    
    return deposit, withdraw


deposit, withdraw = make_account(100)


print(deposit(50))   
print(deposit(25))   


print(withdraw(30))  
print(withdraw(45))  
