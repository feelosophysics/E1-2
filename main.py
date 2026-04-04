def main():
    while True:
        print("\n=== 🎯 나만의 퀴즈 게임 ===")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        
        choice = input("선택: ").strip()
        
        if choice == '5':
            print("게임을 종료합니다. 안녕!")
            break
        else:
            print(f"아직 {choice}번 기능은 준비 중이에요!")

if __name__ == "__main__":
    main()