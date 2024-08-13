#!/usr/bin/env python3
"""Students sorted by average score"""


def top_students(mongo_collection):
    """Returns all students sorted by average score"""
    student_lst = []

    for student in mongo_collection.find():
        total = 0
        new_dict = {}
        new_dict["name"] = student.get('name')
        new_dict['id'] = student.get('_id')
        num = len(student.get('topics'))
        for topic in student.get('topics'):
            total += topic.get('score')
        avg = total / num
        new_dict['averageScore'] = avg
        student_lst.append(new_dict)

    return student_lst.sort(key=myFunc, reverse=True)

def myFunc(e):
  return e['averageScore']
