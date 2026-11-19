class Employee:
    def __init__(self,name, base_pay, bonus, overtime):
        self.name = name
        self.base_pay = base_pay
        self.bonus = bonus
        self.overtime = overtime

    def get_total(self):
        total = self.base_pay + self.bonus +self.overtime
        return total
    
    def get_tax(self):
        tax = self.get_total() * 0.1
        return tax

    
    def get_net(self):
        net = self.get_total() - self.get_tax()
        return net


    def to_string(self):
        return "{}\t{}\t{}\t{}".format(self.name, self.get_total(), self.get_tax(), self.get_net())

    
employees = [Employee("김민수",300,50,20),Employee("이지은",320,40,30),Employee("박준호",280,60,10),Employee("최서현",350,30,25),Employee("한도윤",300,70,15)]


#출력
print("이름","총액","세금","실수령액",sep="\t")
for employee in employees:
    print(employee.to_string())

