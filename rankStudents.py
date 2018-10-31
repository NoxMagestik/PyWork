import operator
import random

student_number = int(input("Enter the number of students: "))


def student_details():
    student_log = {}
    for x in range(0, student_number):
        name = input("Enter the student's name: ")
        marks = int(input("Enter the marks of the student: "))
        student_log[name] = marks
    return student_log


def student_rank(student_log):
    try:
        sorted_log = sorted(student_log.items(), key=operator.itemgetter(1), reverse=True)
        print()
        print(sorted_log)
        print("{} has secured first rank, scoring {} marks".format(sorted_log[0][0], sorted_log[0][1]))
        print("{} has secured second rank, scoring {} marks".format(sorted_log[1][0], sorted_log[1][1]))
        print("{} has secured third rank, scoring {} marks".format(sorted_log[2][0], sorted_log[2][1]))
        print()
        return sorted_log
    except IndexError:
        print("Enter a minimum of 3 students")
        quit()


def student_reward(sorted_log, reward):
    print()
    print("{} has received a cash reward of £{}".format(sorted_log[0][0], reward[0]))
    print("{} has received a cash reward of £{}".format(sorted_log[1][0], reward[1]))
    print("{} has received a cash reward of £{}".format(sorted_log[2][0], reward[2]))
    print()


def student_appreciate(sorted_log):
    for z in sorted_log:
        if z[1] >= 950:
            print("Congratulations on scoring {} marks, {}".format(z[1], z[0]))
        else:
            break


def student_lottery(sorted_log, student_number1):
    rnd = random.randint(0, (student_number1 - 1))
    print
    print("{} won the lottery and is receiving a prize of £1000".format(sorted_log[rnd][0]))
    print()


student_log1 = student_details()
sorted_log1 = student_rank(student_log1)
reward1 = (500, 300, 100)
student_reward(sorted_log1, reward1)
student_appreciate(sorted_log1)
student_lottery(sorted_log1, student_number)
