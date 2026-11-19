class Student: 
    def __init__(self, name,korean,math,english,science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
      

student = Student()

Students= [Student("김철수",85,90,95,80), Student("이영희",90,85,88,90), Student("박민수",75,80,85,90),Student("최지우",95,92,90,88), Student("정민지",80,85,78,95)]

# class 클래스이름:
# def __init__(self, 추가적인 매개변수): ㅔㅁㄴㄴ ㅈ딜.ㅜ믇
Students[0].name
Students[0].korean
Students[0].english