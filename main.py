import sys

# [1] 퀴즈 한 문제의 틀
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self, index):
        print(f"\n----------------------------------------")
        print(f"[문제 {index}] {self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"{i}. {choice}")

# [2] 게임 전체 관리자
class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0

    def add_quiz(self, quiz):
        self.quizzes.append(quiz)

    # 1번 메뉴: 퀴즈 풀기
    def play(self):
        if not self.quizzes:
            print("\n⚠️ 등록된 퀴즈가 없습니다. 퀴즈를 먼저 추가해 주세요!")
            return

        print(f"\n📝 퀴즈를 시작합니다! (총 {len(self.quizzes)}문제)")
        score = 0
        for i, quiz in enumerate(self.quizzes, 1):
            quiz.display(i)
            while True:
                user_input = input("정답 입력 (1-4): ").strip()
                if user_input in ['1', '2', '3', '4']:
                    break
                print("⚠️ 1~4 사이의 숫자를 입력해 주세요.")
            
            if int(user_input) == quiz.answer:
                print("✅ 정답입니다!")
                score += 1
            else:
                print(f"❌ 오답입니다. (정답: {quiz.answer}번)")

        print(f"\n🏆 결과: {len(self.quizzes)}문제 중 {score}문제 정답!")
        if score > self.best_score:
            self.best_score = score
            print("🎉 새로운 최고 점수입니다!")

    # 2번 메뉴: 퀴즈 추가 (예외 처리 포함)
    def add_new_quiz_menu(self):
        print("\n📌 새로운 퀴즈를 추가합니다.")
        question = input("문제 내용을 입력하세요: ").strip()
        if not question:
            print("⚠️ 문제는 비워둘 수 없습니다.")
            return

        choices = []
        for i in range(1, 5):
            choice = input(f"선택지 {i}: ").strip()
            if not choice:
                choice = f"선택지 {i} (비어 있음)"
            choices.append(choice)

        while True:
            try:
                ans_input = input("정답 번호 (1-4): ").strip()
                answer = int(ans_input)
                if 1 <= answer <= 4:
                    break
                print("⚠️ 1에서 4 사이의 번호를 입력하세요.")
            except ValueError:
                print("⚠️ 숫자만 입력 가능합니다.")

        new_quiz = Quiz(question, choices, answer)
        self.add_quiz(new_quiz)
        print("✅ 퀴즈가 성공적으로 추가되었습니다!")

    # 3번 메뉴: 퀴즈 목록 보기
    def list_quizzes(self):
        if not self.quizzes:
            print("\n⚠️ 등록된 퀴즈가 없습니다.")
            return
        
        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        for i, quiz in enumerate(self.quizzes, 1):
            print(f"[{i}] {quiz.question}")

    # 4번 메뉴: 점수 확인
    def show_best_score(self):
        print(f"\n🏆 현재 최고 점수: {self.best_score}점")

# [3] 메인 실행부
def main():
    game = QuizGame()
    
    # 기본 데이터 (Phase 3 내용)
    game.add_quiz(Quiz("파이썬의 창시자는?", ["귀도 반 로섬", "제임스 고슬링", "빌 게이츠", "스티브 잡스"], 1))
    game.add_quiz(Quiz("리스트 추가 메서드는?", ["add()", "append()", "push()", "insert()"], 2))

    try:
        while True:
            print("\n" + "="*40)
            print("        🎯 나만의 퀴즈 게임 🎯")
            print("="*40)
            print("1. 퀴즈 풀기\n2. 퀴즈 추가\n3. 퀴즈 목록\n4. 점수 확인\n5. 종료")
            print("="*40)
            
            choice = input("선택: ").strip()

            if choice == '1':
                game.play()
            elif choice == '2':
                game.add_new_quiz_menu()
            elif choice == '3':
                game.list_quizzes()
            elif choice == '4':
                game.show_best_score()
            elif choice == '5':
                print("👋 게임을 종료합니다. 안녕!")
                break
            else:
                print(f"⚠️ '{choice}'은(는) 잘못된 메뉴입니다.")

    except KeyboardInterrupt:
        print("\n\n🛑 프로그램을 안전하게 종료합니다.")

if __name__ == "__main__":
    main()