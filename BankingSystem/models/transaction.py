class Transaction:
    
    # 생성자 구현
    def __init__(self, transaction_type: str, amount: int, balance: int) -> None :
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance = balance
    # 문열 반환 메소드 구현 str(class명) 하면 밑에 리턴된 내용이 나온다
    def __str__(self) -> str : # 클래스 객체를 읽을수 있는 객체로 선언해주는 것
        return f'거래 유형 : {self.transaction_type}, 거래금액 : {self.amount}, 잔고 : {self.balance}'
    # 튜플로 반환시키는 메소드 구현
    def to_tuple(self) -> tuple : # a = c.to_tuple 이런 입력을 하면 튜플로 반환시켜 저장해 놓을수 있음 
        return (self.transaction_type,self.amount,self.balance)


