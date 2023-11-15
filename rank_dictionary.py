students = [
    {"rollno": 101, "name": "joel", "mark": 85},
    {"rollno": 104, "name": "gokul", "mark": 95},
    {"rollno": 105, "name": "blesson", "mark": 88},
]

sorted_students = sorted(students, key=lambda x: x["mark"], reverse=True)

rank_list = {}
for rank, student in enumerate(sorted_students):
    rank_list[rank] = {"rollno": student["rollno"], "name": student["name"], "mark": student["mark"]}

print("Rank List as a Dictionary (Descending Order):")
for rank, student in rank_list.items():
    print(f"Rank {rank + 1}: Roll No: {student['rollno']}, Name: {student['name']}, Mark: {student['mark']}")
