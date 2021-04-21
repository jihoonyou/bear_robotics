class ATM:
    """
    A class to represent an ATM
    '''

    Attributes
    ----------
    card_list (dictionary): ATM기 전체의 카드 및 계좌정보(공용데이터)를 갖고 있습니다.
    self.flag (boolean): ATM 클래스 test시 종료 flag입니다.
    self.cn (string): 사용자가 입력한 카드의 번호를 갖고 있습니다.
    self.card_inserted (boolean): 카드가 제대로 입력되었는지 확인합니다.
    self.selected_account (dictionary): 사용자의 계좌정보를 가지고 있습니다.
    """
    card_list = {
        '0000-0000-0000-0000': {
            'PIN': '1234',
            'balance': 5000
        }
    }

    def __init__(self):
        self.reset()

    def reset(self):
        """테스트시 사용되는 초기화 함수
        
        ATM 클래스의 instance variable을 초기화합니다
        
        """
        self.flag = True
        self.cn = None
        self.card_inserted = None
        self.selected_account = None

    def insert_card(self, card_number):
        """사용자의 카드번호 입력을 확인하는 함수
        
        사용자의 카드번호 입력정보를 확인합니다

        Args:
            card_number (string): 사용자가 입력한 카드정보

        Returns:
            tuple(string,boolean): 카드가 정보가 card_list에 있다면 (card_number, True) 아니면 ('', False)를 반환합니다
        """
        if card_number not in ATM.card_list.keys():
            self.add_decoration(['카드번호가 틀렸습니다'])
            return '', False
        return card_number, True

    def check_PIN_number(self, card_number, PIN):
        """사용자의 계좌비밀번호를 확인하는 함수

        사용자의 계좌비밀번호를 확인합니다

        Args:
            card_number (string): 사용자가 입력한 카드정보
            PIN (string): 계좌 비밀번호

        Returns:
            boolean: 계좌 비밀번호가 맞으면 True 아니면 False를 반환합니다.
        """
        if ATM.card_list[card_number]["PIN"] != PIN:
            self.add_decoration(['비밀번호가 틀렸습니다'])
            return False
        return True

    def select_account(self, card_number):
        """사용자의 계좌정보를 반환하는 함수

        사용자의 계좌정보를 반환합니다

        Args:
            card_number (string): 사용자가 입력한 카드정보

        Returns:
            dictionary: 사용자의 계좌정보를 ditionary형태로 반환합니다
        """
        return ATM.card_list[card_number]

    def get_balance(self):
        """사용자의 잔액정보를 반환하는 함수

        사용자의 계좌 잔액정보를 반환합니다

        Returns:
            string: 사용자의 계좌 잔고를 반환합니다
        """
        return self.selected_account['balance']

    def is_valid_digit(self, n):
        """숫자값을 판별하는 함수

        입력으로 들어오는 값이 valid한 숫자인지 판별합니다

        Args:
            n (string): 입급/출금 할 금액

        Returns:
            boolean: 숫자가 맞으면 True 아니면 False 
        """
        if not n.isdecimal():
            self.add_decoration(['숫자로 입력 입력해주세요 (소수, 음수 -> 불가)'])
            return False
        return True

    def deposit(self, money):
        """계좌에 돈을 입금하는 함수

        selected_account['balance']에 입력값을 더합니다

        Args:
            money (string): 입급할 금액
        """
        self.selected_account['balance'] += money
        self.add_decoration([self.get_balance()])

    def withdraw(self, money):
        """계좌에서 돈을 출금하는 함수

        selected_account['balance']에서 입력값만큼 뺍니다

        Args:
            money (string): 출금할 금액
        """
        if self.selected_account['balance'] >= money:
            self.selected_account['balance'] -= money
            self.add_decoration([self.get_balance()])
        else:
            self.add_decoration(['잔액이 부족합니다'])

    def add_decoration(self, sentences, deco="--------------------------"):
        """print를 꾸며주는 함수

        함수를 호출하면 print문이 deco로 감싸줘서 출력됩니다

        Args:
            sentences (list(string)): 화면에 출력할 문장
            deco (string, optional): [description]. Defaults to "--------------------------".
        """
        print(deco)
        for sentence in sentences:
            print(sentence)
        print(deco)

    def test(self):
        """test용 함수

        ATM 클래스의 동작을 테스트하기 위한 함수

        """
        self.reset()
        self.add_decoration(['Type (exit) to quit'], "**************************")
        while self.flag:
            user_input = input('카드번호를 입력해주세요:')
            if user_input == 'exit':
                self.flag = False
            else:
                self.cn, card_inserted = self.insert_card(user_input)
            
            while self.flag and card_inserted:
                user_input = input('비밀번호를 입력해주세요:')
                if user_input == 'exit':
                    self.flag = False
                else:
                    is_PIN_correct = self.check_PIN_number(self.cn, user_input)
                
                if is_PIN_correct: 
                    self.selected_account = self.select_account(self.cn)

                while self.flag and is_PIN_correct:
                    self.add_decoration(['Type (cb) to check balance', 'Type (d) to deposit',
                    'Type (w) to withdraw','Type (exit) to quit'],"**************************")
                    
                    user_input = input('입력:')

                    if user_input == 'exit':
                        self.flag = False
                    elif user_input == 'cb':
                        self.add_decoration([self.get_balance()])
                    elif user_input == 'd':
                        print('금액을 입력해주세요. (숫자{positive int, 0}외의 값 - 취소)')
                        money = input('입력:')
                        if self.is_valid_digit(money):
                            money = int(money)
                            self.deposit(money)
                    elif user_input == 'w':
                        print('금액을 입력해주세요. (숫자{positive int, 0}외의 값 - 취소)')
                        money = input('입력:')
                        if self.is_valid_digit(money):
                            money = int(money)
                            self.withdraw(money)
                    else:
                        self.add_decoration(['잘못 입력하셨습니다'])


if __name__ == "__main__":
    ATM1 = ATM()
    ATM1.test()
