if __name__ == "__main__":
    students = []
    for _ in range(int(input().strip())):
        name = input().strip()
        score = float(input().strip())
        students.append([name, score])

    # Extract unique scores and sort them
    unique_scores = sorted({s[1] for s in students})
    second_lowest_score = unique_scores[1]

    # Filter names with the second-lowest score
    names = [s[0] for s in students if s[1] == second_lowest_score]
    names.sort()
    
    for name in names:
        print(name)
