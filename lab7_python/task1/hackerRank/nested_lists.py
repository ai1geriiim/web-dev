def second_lowest_grade():
    records = []
    scores = []
    n = int(input().strip())
    for _ in range(n):
        name = input().strip()
        score = float(input().strip())
        records.append([name, score])
        scores.append(score)
    unique_scores = sorted(set(scores))
    second_lowest = unique_scores[1]
    second_lowest_students = sorted([name for name, score in records if score == second_lowest])
    for student in second_lowest_students:
        print(student)
second_lowest_grade()


