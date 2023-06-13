print("Grading System")
scores = {
    "harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Neville" : 62,
}
for men in scores:
    if scores[men] > 90:
        print(f"{men} is Outstanding")
    elif scores[men] > 80:
        print(f"{men} exceeds expectation")
    elif scores[men] > 70:
        print(f"{men} is Acceptable")
    else:
        print(f"{men} is Failed")