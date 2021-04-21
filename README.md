# 베어로보틱스 과제
> Implement a simple ATM controller

## :arrow_forward:실행

---

```
cd bear_robotics
python ATM.py

카드번호를 입력해주세요:0000-0000-0000-0000
비밀번호를 입력해주세요:1234
```
- test용
    - 카드번호: 0000-0000-0000-0000
    - 비밀번호: 1234
## 📌 TODO

---

- [x] Insert Card
- [x] PIN number 
- [x] Select Account
    - [x] card_list[key] 형태에서 selected_account로 전환
- [x] See Balance
- [x] Deposit & Withdraw
    - [x] 숫자가 아닌 값 처리
    - [x] 소수점 처리(There are only 1 dollar bills in this world, no cents. Thus account balance can be represented in integer.)
    - [x] 음수처리
    - [x] 취소하기 (잘못된 입력 == 취소)
- [x] Test
- [x] 입출력 환경 깔끔하게(데코레이션)

## :ant:개발일지

---

### 1일차(04/18/21)
- Coding Challenges 완료

### 2일차(04/19/21)
- Custom Tasks 시작
- 전체적인 클래스 구조 구성 및 문제 이해

### 3일차(04/20/21)
- TODO 정의
- 기본기능 구현

### 4일차(04/21/21)
- docstring 정리
- README.md 정리
- 리팩토링
