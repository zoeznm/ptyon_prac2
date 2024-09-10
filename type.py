def type_checker():
    user_input = input("값을 입력하세요: ")
    
    if type(user_input) == str and user_input.isdigit():
      
        print(f"{user_input}는 int 입니다.")
    else:
        print(f"{user_input}는 문자열입니다.")

type_checker()
