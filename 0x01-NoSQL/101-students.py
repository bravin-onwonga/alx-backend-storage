#!/usr/bin/env python3
"""Students sorted by average score"""


def top_students(mongo_collection):
    """Returns all students sorted by average score"""
    student_lst = []
    average_list = []
    sorted_student_lst = []

    for student in mongo_collection.find():
        total = 0
        new_dict = {}
        new_dict["name"] = student.get('name')
        new_dict['_id'] = student.get('_id')
        num = len(student.get('topics'))
        for topic in student.get('topics'):
            total += topic.get('score')
        avg = total / num
        average_list.append(avg)
        new_dict['averageScore'] = avg
        student_lst.append(new_dict)

    sorted_avgs = sorted(average_list, reverse=True)

    for i in sorted_avgs:
        for stud in student_lst:
            if stud.get('averageScore') == i:
                sorted_student_lst.append(stud)
                break

    return sorted_student_lst
