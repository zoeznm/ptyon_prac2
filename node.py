import subprocess

def run_cli():
    while True:
        user_input = input("입력하세요: ")
        
        if '노드' in user_input:
  
            subprocess.run("node", shell=True)
            
        elif '타입' in user_input:
          type_input = input("넣어보시오 : ")
        if '타입' in user_input:
    
          if type(type_input) == str and type_input.isdigit():
      
              print(f"{type_input}는 int 입니다.")
          else:
              print(f"{type_input}는 문자열입니다.")

if __name__ == "__main__":
    run_cli()
