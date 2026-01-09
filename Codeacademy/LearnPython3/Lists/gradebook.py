# Gradebook
last_semester_gradebook = [["politics", 80], [
    "latin", 96], ["dance", 97], ["architecture", 65]]

Subjects = ["Physics", "Calculus", "Poetry", "History"]

Grades = [98, 97, 85, 88]

Gradebook = [["Physics", 98], ["Calculus", 97],
             ["Poetry", 85], ["History", 88]]

Gradebook.append(["Computer Science", 100])

Gradebook.append(["Visual arts", 93])

Gradebook[-1][1] = 98

Gradebook[2].remove(85)

Gradebook[2].append("Pass")

full_gradebook = Gradebook + last_semester_gradebook
print(full_gradebook)
