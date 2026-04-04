import json
import os

# [1] 퀴즈 한 문제의 틀
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # JSON 저장을 위해 딕셔너리로 변환하는 함수
    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

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
        self.file_path = "state.json"

    def add_quiz(self, quiz):
        self.quizzes.append(quiz)

    # --- [신규] 파일 저장 기능 ---
    def save_data(self):
        try:
            data = {
                "best_score": self.best_score,
                "quizzes": [q.to_dict() for q in self.quizzes]
            }
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            # print("\n💾 데이터가 안전하게 저장되었습니다.")
        except Exception as e:
            print(f"\n⚠️ 저장 중 오류 발생: {e}")

    # --- [신규] 파일 불러오기 기능 ---
    def load_data(self):
        if not os.path.exists(self.file_path):
            print("\n📂 저장된 파일이 없어 기본 퀴즈를 로드합니다.")
            self.set_default_quizzes()
            return

        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.best_score = data.get("best_score", 0)
                self.quizzes = []
                for q_data in data.get("quizzes", []):
                    self.quizzes.append(Quiz(q_data["question"], q_data["choices"], q_data["answer"]))
            print(f"\n✅ 데이터를 불러왔습니다. (퀴즈 {len(self.quizzes)}개, 최고점수 {self.best_score}점)")
        except (json.JSONDecodeError, KeyError):
            print("\n⚠️ 파일이 손상되어 초기화합니다.")
            self.set_default_quizzes()
        except Exception as e:
            print(f"\n⚠️ 불러오기 중 오류 발생: {e}")

    # 기본 퀴즈 설정 (파일이 없을 때 실행)
    def set_default_quizzes(self):
        self.quizzes = [
            Quiz("파이썬의 창시자는 누구일까요?", ["귀도 반 로섬", "제임스 고슬링", "빌 게이츠", "스티브 잡스"], 1),
            Quiz("리스트에 요소를 추가하는 메서드는?", ["add()", "append()", "push()", "insert_end()"], 2),
            Quiz("다음 중 기본 자료형이 아닌 것은?", ["int", "str", "boolean", "dictionary"], 4),
            Quiz("반복문을 중단할 때 사용하는 키워드는?", ["stop", "exit", "break", "continue"], 3),
            Quiz("출력을 위해 사용하는 함수는?", ["input()", "print()", "show()", "write()"], 2)
        ]
        self.save_data() # 기본 데이터도 파일로 만들어둠

    # 메뉴 기능들 (이전과 동일하지만 끝날 때 save_data() 호출 추가)
    def play(self):
        if not self.quizzes: return
        score = 0
        for i, quiz in enumerate(self.quizzes, 1):
            quiz.display(i)
            while True:
                user_input = input("정답 입력 (1-4): ").strip()
                if user_input in ['1', '2', '3', '4']: break
                print("⚠️ 1~4 사이 숫자만 입력하세요.")
            if int(user_input) == quiz.answer:
                print("✅ 정답입니다!"); score += 1
            else:
                print(f"❌ 오답입니다. (정답: {quiz.answer}번)")
        
        print(f"\n🏆 결과: {len(self.quizzes)}개 중 {score}개 정답!")
        if score > self.best_score:
            self.best_score = score
            print("🎉 새로운 최고 점수입니다!")
            self.save_data() # 최고 점수 갱신 시 저장

    def add_new_quiz_menu(self):
        print("\n📌 새로운 퀴즈 추가")
        q = input("문제: ").strip()
        c = [input(f"선택지 {i}: ").strip() for i in range(1, 5)]
        while True:
            ans = input("정답 (1-4): ").strip()
            if ans in ['1', '2', '3', '4']: break
        self.add_quiz(Quiz(q, c, int(ans)))
        self.save_data() # 퀴즈 추가 시 저장
        print("✅ 추가 완료!")

    def list_quizzes(self):
        print(f"\n📋 퀴즈 목록 ({len(self.quizzes)}개)")
        for i, quiz in enumerate(self.quizzes, 1):
            print(f"[{i}] {quiz.question}")

# [3] 메인 실행부
def main():
    game = QuizGame()
    game.load_data() # 시작할 때 데이터 불러오기

    try:
        while True:
            print("\n" + "="*40)
            print("        🎯 나만의 퀴즈 게임 🎯")
            print("="*40)
            print("1. 퀴즈 풀기\n2. 퀴즈 추가\n3. 퀴즈 목록\n4. 점수 확인\n5. 종료")
            print("="*40)
            choice = input("선택: ").strip()

            if choice == '1': game.play()
            elif choice == '2': game.add_new_quiz_menu()
            elif choice == '3': game.list_quizzes()
            elif choice == '4': print(f"\n🏆 최고 점수: {game.best_score}점")
            elif choice == '5': print("👋 종료합니다."); break
            else: print(f"⚠️ '{choice}'은(는) 잘못된 입력입니다.")

    except KeyboardInterrupt:
        game.save_data() # 갑자기 꺼져도 일단 저장 시도
        print("\n\n🛑 안전하게 종료되었습니다.")

if __name__ == "__main__":
    main()