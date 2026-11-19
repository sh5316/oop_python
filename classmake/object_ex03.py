#딕셔너리를 리턴하는 함수를 선언
def create_student(name,korean,math,english,science):
    return {
        "name":name,
        "korean": korean,
        "math": math,
        "english": english,
        "science": science
    }

students = [
    create_student("김철수",85,90,95,80),
    create_student("이영희",90,85,88,90),
    create_student("박민수",75,80,85,90),
    create_student("최지우",95,92,90,88),
    create_student("정민지",80,85,78,95)
]

# 학생을 처리하는 함수
# 학생 총점을 리턴하는 함수: student_get_sum(student)
# 학생 평균을 리턴하는 함수: student_get_avg(student)
# 학생 한명의 점수를 출력하는 함수: student_to_string(student)

def student_get_sum(student):
    score_sum = student["korean"]+student["english"]+student["math"]+student["science"]
    return score_sum
    

def student_get_avg(student):
    score_avg = student_get_sum(student)/ 4
    return score_avg

def student_to_string(student):
    return "{}\t{}\t{}".format(student["name"], student_get_sum(student), student_get_avg(student))



print("이름","총점","평균",sep="\t")
for student in students:
        print(student_to_string(student))