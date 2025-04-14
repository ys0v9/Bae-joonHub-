A = int(input())  # 물리 점수
B = int(input())  # 화학 점수
C = int(input())  # 생물 점수
D = int(input())  # 지구과학 점수
E = int(input())  # 역사 점수
F = int(input())  # 지리 점수

science_scores = [A, B, C, D]
science_scores.sort()

max_science_sum = sum(science_scores[1:])  

max_history_geography = max(E, F)

total_score = max_science_sum + max_history_geography

print(total_score)