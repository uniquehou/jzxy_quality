import numpy as np
from school_student.models import *
import pandas as pd

DEPAR = {}
GRADE = {}
error = []


def get_grade(grade):
    if grade in GRADE:
        return GRADE[grade]
    else:
        g = Grade.objects.create(name=grade)
        GRADE[grade] = g
        return g


def get_depar(depar):
    if depar in DEPAR:
        return DEPAR[depar]
    else:
        d = Department.objects.create(name=depar)
        DEPAR[depar] = d
        return d


data_excel = pd.read_excel('data.xls', skiprows=[0, ])
data = np.array(data_excel).astype(np.str)

for i in range(data.shape[0]):
    try:
        s = Student(student_id=data[i][0],
                    student_name=data[i][1],
                    student_grade=get_grade(data[i][2]),
                    student_department=get_depar(data[i][3]),
                    )
        s.save()
        print("success: ", i, data[i][0])
    except:
        error.append(data[i][0])