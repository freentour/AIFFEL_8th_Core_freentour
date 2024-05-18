# ToDo 클래스
class ToDo:
    def __init__(self, content='', completed=False):
        self.content = content      # 할일 내용
        self.completed = completed  # 할일 완료 여부
    
    def get(self):
        if self.completed:
            msg = f"{self.content} ☑"
        else:
            msg = f"{self.content} ☐"
        
        return msg

    def set(self, content):
        self.content = content
    
    def complete(self):
        self.completed = True
    
    def incomplete(self):
        self.completed = False

# ToDoList 클래스
class ToDoList:
    def __init__(self):
        self.todos = []
    
    def print(self):
        if len(self.todos) == 0:
            print(" ")
            print("현재 등록된 할일이 없습니다.")
        else:
            print(" ")
            print("-"*5, "등록된 할일 목록", "-"*5)
            for i in range(len(self.todos)):
                print(f"{i+1}. {self.todos[i].get()}")

    def append(self, todo):     # 할일 추가
        self.todos.append(todo)

    def complete(self, index):      # 할일 완료로 표시
        self.todos[index-1].complete()

    def incomplete(self, index):    # 할일 미완료로 표시
        self.todos[index-1].incomplete()

    def update(self, index, content):   # 할일 내용 수정
        self.todos[index-1].set(content)

    def remove(self, index):    # 할일 삭제
        del self.todos[index-1]
    
    def empty(self):    # 할일 목록 비우기
        self.todos = []

# ToDoApp 클래스
class ToDoApp:
    def __init__(self):
        self.todo_list = ToDoList()     # ToDoList 객체 생성
    
    def print_start_msg(self):
        print("할일 관리 프로그램을 시작합니다.")
    
    def print_exit_msg(self):
        print(" ")
        print("할일 관리 프로그램을 종료합니다.")

    def print_menu_msg(self):
        menu_msg = """
========== Menu ==========
1. 할일 등록
2. 할일 완료로 표시
3. 할일 미완료로 표시
4. 할일 내용 수정
5. 할일 삭제
6. 할일 목록 비우기
7. 전체 목록 출력하기
0. 프로그램 종료
=========================="""
        print(menu_msg)
    
    def run(self):
        self.print_start_msg()  # 프로그램 시작 메세지 출력

        while True:
            self.print_menu_msg()   # 메뉴 출력

            menu = input("메뉴를 선택해 주세요 : ")
            
            menu_list = ['1', '2', '3', '4', '5', '6', '7', '0']
            if menu not in menu_list:
                print("Menu에 없는 문자를 입력하셨네요. 다시 선택해 주세요.")
                continue

            if menu == '0':     # 프로그램 종료
                break
            else:
                if menu == '1':     # 할일 등록
                    content = input("새로 등록할 할일의 내용을 입력해 주세요 : ")
                    todo = ToDo(content)    # ToDo 객체 생성
                    self.todo_list.append(todo)
                elif menu == '2':   # 할일 완료로 표시
                    index = int(input("완료로 표시할 할일의 번호를 입력해 주세요 : "))
                    self.todo_list.complete(index)
                elif menu == '3':   # 할일 미완료로 표시
                    index = int(input("미완료로 표시할 할일의 번호를 입력해 주세요 : "))
                    self.todo_list.incomplete(index)
                elif menu == '4':   # 할일 내용 수정
                    index = int(input("수정할 할일의 번호를 입력해 주세요 : "))
                    content = input("수정할 내용을 입력해 주세요 : ")
                    self.todo_list.update(index, content)
                elif menu == '5':   # 할일 삭제
                    index = int(input("삭제할 할일의 번호를 입력해 주세요 : "))
                    self.todo_list.remove(index)
                elif menu == '6':   # 할일 목록 비우기
                    self.todo_list.empty()
                    print("할일 목록을 모두 비웠습니다.")
                elif menu == '7':   # 전체 목록 출력하기
                    self.todo_list.print()
                
                if menu != '7':
                    # 작업 후 항상 현재 할일 목록 전체 표시하기
                    self.todo_list.print()
        
        self.print_exit_msg()   # 프로그램 종료 메세지 출력

def main():
    app = ToDoApp()     # ToDoApp 객체 생성
    app.run()

if __name__ == '__main__':
    main()