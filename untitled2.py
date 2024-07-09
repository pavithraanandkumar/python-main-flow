students = [
    {"name": "ram", "scores": [85, 90, 88]},
    {"name": "sam", "scores": [78, 81, 79]},
    {"name": "priya", "scores": [92, 95, 93]}
]
for std in students:
    name=std["name"]
    mark=std["scores"]
    ave=sum(mark)/len(mark)
    print(f"The average score for {name} is {ave:.1f}")
