# 급여 계산만 담당
class Salary:
    def __init__(self, base_pay, bonus, overtime):
        self.base_pay = base_pay
        self.bonus = bonus
        self.overtime= overtime

    def get_total(self):
        pay = self.base_pay + self.bonus + self.overtime
        return pay

    def get_tax(self):
        tax = self.get_total() * 0.1
        return tax

    def get_net(self):
        net = self.get_total() - self.get_tax()
        return net


# 사원정보 + Salary 객체를 속성으로 가진다.
class Employee:
    def __init__(self, name, dept, salary):
        self.name = name
        self.dept = dept
        self.salary = salary

    def to_string(self):
        return "{}\t{}\t{}\t{}\t{}".format( self.name,
                                            self.dept,
                                            self.salary.get_total(),
                                            self.salary.get_tax(),
                                            self.salary.get_net())


employees = [Employee("김민수","개발팀",Salary(300,50,20)),
             Employee("이지은","인사팀",Salary(320,40,30)),
             Employee("박준호","영업팀",Salary(280,60,10)),
             Employee("최서현","개발팀",Salary(350,30,25)),
             Employee("한도윤","마케팀",Salary(300,70,15))]

print("이름","부서","총액","세금","실수령액",sep="\t")
for employee in employees:
    print(employee.to_string())
