class Salary:
    def __init__(self, base_pay, bonus, overtime):
        self.base_pay = base_pay
        self.bonus = bonus
        self.overtime = overtime
    # 총 급여
    def get_total(self):
        total = self.base_pay + self.bonus + self.overtime
        return total
     # 세금 (예시: 총 급여의 10%)
    def get_tax(self):
        tax = self.get_total() * 0.1
        return tax
    # 실수령액
    def get_net(self):
        net = self.get_total() - self.get_tax()
        return net

class WorkHistory:
    def __init__(self, company, position, start_year, end_year):
        self.company = company
        self.position = position
        self.start_year = start_year
        self.end_year = end_year

    # 근무 기간 계산
    def get_years(self):
        return self.end_year - self.start_year

    def to_string(self):
        return "{}\t{}\t{}\t{}\t{}".format(
            self.company, self.position, self.start_year,
            self.end_year, self.get_years()
        )
    
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.dept = None
        self.salary = salary
        self.histories = []

    def add_history(self,history):
        self.histories.append(history)

    def get_career(self):
        career = 0

        for history in self.histories:
            career += history.get_years()

        return career
    def to_string(self):
        return "{}\t{}\t{}\t{}".format(self.name,self.dept,self.salary.get_total(),self.get_career())

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        employee.dept = self.name

    def get_payroll(self):
        total = 0

        for emp in self.employees:
            total += emp.salary.get_total()

        return total

    def get_avg_career(self):
        if len(self.employees) == 0:
            return 0

        total = 0

        for emp in self.employees:
            total += emp.get_career()

        return total / len(self.employees)

    # 부서 요약 + 사원별 급여명세
    def print_members(self):
        print(f"\n[{self.name}] "
              f"인원: {len(self.employees)}명 / "
              f"급여 총액: {self.get_payroll():,}만원 / "
              f"평균 경력: {self.get_avg_career():.1f}년")

        print("-" * 75)

        for emp in self.employees:
            print(f"이름: {emp.name}")
            print(f"부서: {emp.dept}")
            print(f"기본급: {emp.salary.base_pay:,}만원")
            print(f"보너스: {emp.salary.bonus:,}만원")
            print(f"초과근무수당: {emp.salary.overtime:,}만원")
            print(f"총 급여: {emp.salary.get_total():,}만원")
            print(f"세금: {emp.salary.get_tax():,.1f}만원")
            print(f"실수령액: {emp.salary.get_net():,.1f}만원")
            print(f"총 경력: {emp.get_career()}년")
            print("-" * 75)    


class Company:
    def __init__(self,name):
        self.name = name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)


    def get_employee_count(self):
        count = 0

        for dept in self.departments:
            count += len(dept.employees)
        return count

    def get_payroll(self):
        payroll = 0

        for dept in self.departments:
            payroll += dept.get_payroll()
        return payroll
 # 전체 현황 출력
    def print_report(self):
        print(f"\n========== {self.name} 전체 현황 ==========")
        print(f"{'부서':<12}{'인원':<10}{'급여 총액':<15}{'평균 경력'}")
        print("-" * 55)

        for dept in self.departments:
            print(
                f"{dept.name:<12}"
                f"{len(dept.employees):<10}"
                f"{dept.get_payroll():<15,}"
                f"{dept.get_avg_career():.1f}년"
            )

        print("-" * 55)
        print(
                f"{self.name + ' 전체':<12}"
                f"{self.get_employee_count():<10}"
                f"{self.get_payroll():,}"
)

# ==================================
# 6. 객체 생성 및 실행
# ==================================

# ==================================
# 사원 생성 (급여 단위: 만원)
# ==================================

e1 = Employee("김민수", Salary(300, 50, 20))
e2 = Employee("최서연", Salary(350, 30, 25))
e3 = Employee("이지은", Salary(320, 40, 30))
e4 = Employee("박준호", Salary(280, 60, 10))
e5 = Employee("한도윤", Salary(300, 70, 15))


# ==================================
# 근무이력 추가
# ==================================

# 김민수: 3년 + 4년 = 7년
e1.add_history(WorkHistory("네오소프트", "사원", 2015, 2018))
e1.add_history(WorkHistory("한빛시스템", "대리", 2018, 2022))

# 최서연: 4년 + 4년 + 3년 = 11년
e2.add_history(WorkHistory("데이터랩", "연구원", 2012, 2016))
e2.add_history(WorkHistory("클라우드원", "선임", 2016, 2020))
e2.add_history(WorkHistory("넥스트AI", "책임", 2020, 2023))

# 이지은: 4년
e3.add_history(WorkHistory("그린HR", "사원", 2017, 2021))

# 박준호: 신입 (근무이력 없음)

# 한도윤: 3년
e5.add_history(WorkHistory("브랜드웍스", "사원", 2019, 2022))


# ==================================
# 부서 생성
# ==================================

dev = Department("개발팀")
hr = Department("인사팀")
sales = Department("영업팀")
marketing = Department("마케팅팀")


# ==================================
# 부서에 사원 배치
# ==================================

dev.add_employee(e1)
dev.add_employee(e2)

hr.add_employee(e3)

sales.add_employee(e4)

marketing.add_employee(e5)


# ==================================
# 회사 생성
# ==================================

company = Company("블루웨이브")

# 회사에 부서 등록
company.add_department(dev)
company.add_department(hr)
company.add_department(sales)
company.add_department(marketing)


# ==================================
# 전체 보고서 출력
# ==================================

company.print_report()

