# 人员管理系统
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"姓名:{self.name} | 年龄:{self.age}"

class Manager:
    def __init__(self):
        self.people_list = []

    # 添加人员
    def add_people(self):
        name = input("请输入姓名:")
        age = input("请输入年龄:")
        student = Student(name, age)
        self.people_list.append(student)

    # 查询人员
    def query_people(self):
        name = input("请输入要查询的姓名:")
        for s in self.people_list:
            if s.name == name:
                print(s)
                return
        print("未找到该人员信息")

    # 修改信息
    def update_people(self):
        name = input("请输入要修改人员的姓名:")
        for s in self.people_list:
            if s.name == name:
                print(f"修改前的信息: {s}")
                new_name = input("请输入新的姓名:")
                new_age = input("请输入新的年龄:")
                s.name = new_name
                s.age = new_age
                print("修改成功")
                print(f"修改后的信息: {s}")
                return
        print("未找到该人员信息")

    # 删除人员
    def delete_people(self):
        name = input("请输入要删除的人姓名:")
        for s in self.people_list:
            print(f"删除前的信息: {self.people_list}")
            if s.name == name:
                self.people_list.remove(s)
                print("删除成功")
                print(f"删除后的信息: {self.people_list}")
                return
        print("未找到该人员信息")
    # 显示所有人员
    def query_all(self):
        if not self.people_list:
            print("没有人员信息")
            return
        print(f"所有人员信息:{self.people_list}")
    
    # 执行
    def run(self):
        while True:
            print("欢迎使用人员管理系统")
            print("1. 添加人员")
            print("2. 查询人员")
            print("3. 修改人员信息")
            print("4. 删除人员")
            print("5. 显示所有人员信息")
            print("6. 退出系统")
            choice = input("请输入操作编号:")
            if choice == "1":
                self.add_people()
            elif choice == "2":
                self.query_people()
            elif choice == "3":
                self.update_people()
            elif choice == "4":
                self.delete_people()
            elif choice == "5":
                self.query_all()
            elif choice == "6":
                print("退出系统")
                break
            else:
                print("输入有误，请重新输入")

if __name__ == "__main__":
    manager = Manager()
    manager.run()