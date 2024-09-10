import subprocess

def run_cli():
    while True:
        user_input = input("입력하세요: ")
        
        if '노드' in user_input:
  
            subprocess.run("node", shell=True)
        elif '타입' in user_input:
    
            data = input("타입을 확인할 값을 입력하세요: ")
            print(f"입력된 값의 타입은: {type(data)}")
        else:
            print("명령을 인식하지 못했습니다.")

if __name__ == "__main__":
    run_cli()
