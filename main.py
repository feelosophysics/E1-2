# [1] 설계도(클래스)를 먼저 정의합니다.
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

        # [추가] 퀴즈 한 문제를 화면에 보여주는 메서드
    def display(self, index):
        print(f"\n----------------------------------------")
        print(f"[문제 {index}] {self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"{i}. {choice}")

class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0

    def add_quiz(self, quiz):
        self.quizzes.append(quiz)

        # [추가] 전체 퀴즈를 진행하는 메서드
    def play(self):
        if not self.quizzes:
            print("\n⚠️ 등록된 퀴즈가 없습니다. 퀴즈를 먼저 추가해 주세요!")
            return

        print(f"\n📝 퀴즈를 시작합니다! (총 {len(self.quizzes)}문제)")
        score = 0

        for i, quiz in enumerate(self.quizzes, 1):
            quiz.display(i) # 퀴즈 보여주기
            
            # 정답 입력 받기 및 예외 처리
            while True:
                user_input = input("정답 번호 입력 (1-4): ").strip()
                if user_input in ['1', '2', '3', '4']:
                    break
                print("⚠️ 1에서 4 사이의 숫자만 입력해 주세요.")
            
            # 정답 확인
            if int(user_input) == quiz.answer:
                print("✅ 정답입니다!")
                score += 1
            else:
                print(f"❌ 오답입니다. (정답: {quiz.answer}번)")

        # 결과 출력
        print("\n" + "="*40)
        print(f"🏆 결과: {len(self.quizzes)}문제 중 {score}문제 정답!")
        
        # 최고 점수 갱신 (나중에 파일 저장할 때 사용)
        if score > self.best_score:
            self.best_score = score
            print("🎉 새로운 최고 점수입니다!")
        print("="*40)

# [2] 실제 동작할 로직(함수)을 정의합니다.
def main():
    # 이제 파이썬이 위에서 클래스들을 읽었기 때문에 에러가 나지 않습니다.
    game = QuizGame()

    # 기본 퀴즈 추가
    game.add_quiz(Quiz("파이썬의 창시자는 누구일까요?", ["귀도 반 로섬", "제임스 고슬링", "빌 게이츠", "스티브 잡스"], 1))
    game.add_quiz(Quiz("리스트에 요소를 추가하는 메서드는?", ["add()", "append()", "push()", "insert_end()"], 2))
    game.add_quiz(Quiz("다음 중 기본 자료형이 아닌 것은?", ["int", "str", "boolean", "dictionary"], 4))
    game.add_quiz(Quiz("반복문을 중단할 때 사용하는 키워드는?", ["stop", "exit", "break", "continue"], 3))
    game.add_quiz(Quiz("출력을 위해 사용하는 함수는?", ["input()", "print()", "show()", "write()"], 2))

    try:
        while True:
            print("\n" + "="*40)
            print(f"        🎯 나만의 퀴즈 게임 🎯 (현재 퀴즈: {len(game.quizzes)}개)")
            print("="*40)
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록")
            print("4. 점수 확인")
            print("5. 종료")
            print("="*40)
            
            try:
                choice = input("선택: ").strip()
            except EOFError:
                print("\n\n⚠️ 입력 종료. 안전하게 종료합니다.")
                break

            if choice not in ['1', '2', '3', '4', '5']:
                print(f"⚠️ '{choice}'은 잘못된 입력입니다.")
                continue

            if choice == '1':
                game.play()  # 퀴즈 풀기 시작!
            elif choice == '5':
                print("👋 게임을 종료합니다!")
                break
            elif choice == '2':
                print("✨ [퀴즈 추가] 기능을 구현할 차례입니다!")
            elif choice == '3':
                print("✨ [퀴즈 목록] 기능을 구현할 차례입니다!")
            elif choice == '4':
                print("✨ [점수 확인] 기능을 구현할 차례입니다!")

    except KeyboardInterrupt:
        print("\n\n🛑 강제 종료되었습니다.")

# [3] 가장 마지막에 프로그램을 시작시킵니다.
if __name__ == "__main__":
    main()