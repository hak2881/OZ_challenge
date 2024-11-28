from .transaction import Transaction
from utils.exceptions import InsufficientFundsError, NegativeAmountError
from utils.decorators import validate_transaction

class Account:
    
    bank_name =''
    
    #생성자
    def __init__(self) -> None:
        self.transactions = []
        self.__balance=0
    #입금
    def deposit(self,amount:int) :
        if amount <0 : 
            raise NegativeAmountError()
        self.__balance += amount
        self.transactions.append(Transaction('입금',amount,self.__balance))
        
    #출금
    def withdraw(self,amount:int) -> None :
        if amount <= 0:
            raise NegativeAmountError()
        if amount > self.__balance:
            raise InsufficientFundsError(self.__balance)    
        self.__balance -= amount 
        self.transactions.append(Transaction('출금',amount,self.__balance))
        
    def get_balance(self) ->int :
        return self.__balance
            
    def get_transactions(self) :
        return self.transactions
    
    @classmethod # 클래스 변수를 사용하려면 반듯이 적어줘야함 
    def get_bank_name(cls) -> str:
        return cls.bank_name
    
    @classmethod
    def set_bank_name(cls, name: str) -> None:
        cls.bank_name = name