from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from school_student.models import *
import json

class Search(View):
    def get(self, request):
        return render(request, 'quality/search.html')

    def post(self, request):
        student = Student.objects.filter(student_id=request.POST.get("student_id"))
        if student:
            res = {
                "status": 1,
                "student_id": student[0].student_id,
                "student_name": student[0].student_name,
                "sex": Student.sex_choice[int(student[0].sex)-1][1],
                "nation": Student.nation_choice[int(student[0].nation)-1][1],
                "political_satus": Student.political_satus_choice[int(student[0].political_satus)-1][1],
                "student_department": student[0].student_department.name,
                "student_grade": student[0].student_grade.name,
                "duty": student[0].duty,
                "account": student[0].account,
            }

            praise = Praise.objects.filter(student=student[0])
            res['praise'] = []
            for each in praise:
                res['praise'].append({
                    "type": Praise.praise_type_choice[int(each.praise_type)-1][1],
                    "text": each.text
                })

            publish = Publishment.objects.filter(student=student[0])
            res['publish'] = []
            for each in publish:
                res['publish'].append({
                    "type": Publishment.publish_type_choice[int(each.publish_type)-1][1],
                    "text": each.text
                })
            return HttpResponse(json.dumps(res), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"status": 2}), content_type="application/json")


class SeAccount(View):
    def get(self, request):
        return render(request, 'quality/se_account.html')

    def post(self, request):
        student = Student.objects.filter(account=request.POST.get("account"))
        if student:
            res = {
                "status": 1,
                "student_name": student[0].student_name,
                "student_department": student[0].student_department.name,
                "student_grade": student[0].student_grade.name,
            }
            return HttpResponse(json.dumps(res), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"status": 2}), content_type="application/json")


class AddInfo(View):
    def get(self, request):
        return_data = {
            'department': Department.objects.all(),
            'major': Major.objects.all(),
            'grade': Grade.objects.all(),
        }
        return render(request, 'quality/addinfo.html', return_data)

    def post(self, request):
        s = Student.objects.get(id=request.session.get('stu_id'))
        s.sex = request.POST.get('sex')
        s.nation = request.POST.get('nation')
        s.political_satus = request.POST.get('political_satus')
        s.duty = request.POST.get('duty')
        s.account = request.POST.get('account')
        s.save()
        return HttpResponse(json.dumps({"status": 1}), content_type="application/json")


@csrf_exempt
def verify(request):
    if request.method == "POST":
        student = Student.objects.select_related().filter(student_id=request.POST['student_id'])
        if student:
            data = {
                "exist": 1,
                "student_id": student[0].student_id,
                "student_name": student[0].student_name,
                "sex": student[0].sex,
                "nation": student[0].nation,
                "political_satus": student[0].political_satus,
                "student_department": student[0].student_department.name,
                "student_grade": student[0].student_grade.name,
                "duty": student[0].duty,
                "account": student[0].account,
            }
            request.session['stu_id'] = student[0].id   # 将学生id写入session中
            return HttpResponse(json.dumps(data), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"exist": 0}))