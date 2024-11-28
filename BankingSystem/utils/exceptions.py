class InsufficientFundsError(Exception) :
    def __init__(self,balance:int):
        super().__init__(f'잔액이 부족합니다. 잔고 :{balance}원 ')
class NegativeAmountError(Exception) :
    def __init__(self) :
        super().__init__('음수 금액은 허용 안됩니다.')
class UserNotFoundError(Exception):
    def __init__(self,username) :
        super().__init__(f'사용자를 찾을 수 없습니다. {username}')
    