Eren = {
    'name': "Eren",
    'homework': [],
    'quizzes': [],
    'tests': [],
}
Mikasa = {
    'name': "Mikasa",
    'homework': [],
    'quizzes': [],
    'tests': [],
}
Armin = {
    'name': "Armin",
    'homework': [],
    'quizzes': [],
    'tests': [],
}
eren = {
 "name": "Eren",
 "homework": [90.0, 97.0, 75.0, 92.0],
 "quizzes": [88.0, 40.0, 94.0],
 "tests": [75.0, 90.0]
}
mikasa = {
    "name": "Mikasa",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
armin = {
   "name": "Armin",
   "homework": [0.0, 87.0, 75.0, 22.0],
   "quizzes": [0.0, 75.0, 78.0],
   "tests": [100.0, 100.0]
}
Students = [eren, mikasa, armin]
for data in Students:
    print(data['name'])
    print(data['homework'])
    print(data['quizzes'])
    print(data['tests'])


def average (numbers):
    total = float(sum(numbers))
    return total/len(numbers)
print(average([4, 6, 9, 5, 8, 7]))


def get_average(data):
    homework = average(data['homework'])
    quizzes = average(data['quizzes'])
    tests = average(data['tests'])
    return homework * 0.1 + quizzes * 0.3 + tests * 0.6
print ( get_average (armin))


def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
lloyd = {
    "name": "Lloyd",
    "homework": [70.0, 90.0, 30.0, 67.0],
    "quizzes": [40.0, 98.0, 100.0],
    "tests": [84.0, 88.0, 50.0]
}
print(get_letter_grade(get_average(lloyd)))

def get_class_average(Students):
    results = []
    for data in Students:
        results.append(get_average(data))
    return results
class_averages = get_class_average(Students)
print(class_averages)
print(get_letter_grade(average(class_averages)))