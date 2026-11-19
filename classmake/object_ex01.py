#학생 리스트 (students)를 선언해 주세요. 5명의 학생정보를 아래 속성으로 저장하세요.
#학생은 이름(name),(4과목 점수 데이터를 갖는다.)
class Students:
    def __init__(self, name):
        self.name = name
        self.subject = []

    def subject(self, category):
        self.subject.append(category)

students = [
    {"name": "김철수", "korean": 85, "english": 90, "math": 95, "science": 80},
    {"name": "이영희", "korean": 90, "english": 85, "math": 88, "science": 92},
    {"name": "박민수", "korean": 75, "english": 80, "math": 85, "science": 90},
    {"name": "최지우", "korean": 95, "english": 92, "math": 90, "science": 88},
    {"name": "정민지", "korean": 80, "english": 85, "math": 78, "science": 95}
]
# 학생명단을(성적표) 출력하세요
print("이름","총점","평균",sep="\t")

for student in students :
    #점수의 총함과 평균을 구하세요.
    score_sum = student["korean"]+student["english"]+student["math"]+student["science"]
    score_avg = score_sum/ 4
    # 출력
    print(student["name"],score_sum,score_avg,sep="\t") 
