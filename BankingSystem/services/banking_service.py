from utils.exceptions import UserNotFoundError,InsufficientFundsError,NegativeAmountError
from models.user import User


class BankingService :
    
    #생성자 구현
    def __init__(self)->None :
        self.users = []
        
    #
    def add_user(self,username:str):
        self.users.append(User(username))
    
    # 사용자 찾기 메서드 구현
    def find_user(self,username:str) :
        for user in self.users :
            if username == user.username:# self.users 는 User 로 받아진 객체임 그래서 User 안에 username이랑 비교하는 것임
                return user
        raise UserNotFoundError(username)
    
    # 사용자 메뉴 제공
    def user_menu(self,username:str):
        #입금 출금 잔고확인 거래내역 
        user=self.find_user(username)
        while True :
            try :
                mode = input("원하는 작업을 입력하세요. (1: 입금,2: 출금,3: 잔고확인,4: 거래내역, 5: 종료) ")
                if mode=='5' :
                    print('업무를 종료합니다.')
                    break
                elif mode == '1' :
                    amount= input('입금할 금액을 입력하세요.')
                    user.account.deposit(int(amount))
                elif mode == '2' :
                    amount= input('출금할 금액을 입력하세요.')
                    user.account.withdraw(int(amount))
                elif mode == '3' :
                    print(f'현재 잔고는 {user.account.get_balance()}원 입니다.')
                elif mode == '4' :
                    for transaction in user.account.get_transactions() :
                        print(transaction)
                else :
                    print("잘못된 입력입니다. 다시 시도하세요.")
            except ValueError as e:
                print(f"잘못된 입력입니다: {e}")
            except InsufficientFundsError as e:
                print(f"오류: {e}")
            except NegativeAmountError as e:
                print(f"오류: {e}")
            except UserNotFoundError as e:
                print(f"오류: {e}")