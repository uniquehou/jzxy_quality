from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from school_student.models import *
from quality.models import *
import json

class Search(View):
    def get(self, request):
        grades = Grade.objects.all()
        res = {'grades': grades}
        return render(request, 'quality/search.html', res)

    def post(self, request):
        if request.POST.get('student_id'):
            students  = Student.objects.filter(student_id = request.POST['student_id'])
        elif request.POST.get('grade'):
            grade = Grade.objects.get(name=request.POST['grade'])
            students = Student.objects.filter(student_grade = grade)
        res = {}
        if students:
            matin_list = []
            exer_list = []
            for student in students:
                res['status'] = 1
                late_matin = Late_matin.objects.filter(student=student)
                late_exer = Late_morn_exer.objects.filter(student=student)
                for matin in late_matin:
                    matin_list.append({
                        'name': matin.student.student_name,
                        'date': matin.date.strftime("%Y-%m-%d"),
                        'note': matin.note
                    })
                for exer in late_exer:
                    exer_list.append({
                        'name': exer.student.student_name,
                        'date': exer.date.strftime("%Y-%m-%d"),
                        'note': exer.note
                    })
            res['matin_list'] = matin_list
            res['exer_list'] = exer_list
        else:
            res['status'] = 0
        return HttpResponse(json.dumps(res))