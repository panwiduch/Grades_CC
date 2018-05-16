grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


def print_grades(grades):
    for grade in grades:
        print(grade)

def grades_sum(grades):
    total = 0
    for grade in grades:
        total += grade
    return total

def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(grades):
    variance = 0
    average = grades_average(grades)
    for grade in grades:
        variance += (average - grade) ** 2
    variance = variance / len(grades)
    return variance

def grades_std_deviation(variance):
    return variance ** 0.5

variance = grades_variance(grades)

print('Grades:', grades)
print('Sum: ', grades_sum(grades))
print('Average: ', grades_average(grades))
print('Variance: ', grades_variance(grades))
print('Standard deviation: ', grades_std_deviation(variance))



