from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from quality.models import *
import json
from quality import base

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


class Login(View):
    def get(self, request):
        return render(request, 'quality/login.html')

    def post(self, request):
        student_id = request.POST.get('student_id')
        password = base.encodepass( request.POST.get('password') )
        student = Student.objects.filter(student_id=student_id)
        if len(student)>0:
            if password == student[0].password:
                request.session['id'] = student[0].id
                request.session['student_id'] = student[0].student_id
                request.session['student_name'] = student[0].student_name
                return HttpResponse(json.dumps({'status': 1}), content_type='json')  # 1，登录成功
            else:
                return HttpResponse(json.dumps({'status': 3}), content_type='json')  # 3，密码错误
        else:
            return HttpResponse(json.dumps({'status': 2}), content_type='json')    # 2，学号不存在


def quit(request):
    del request.session['id']
    del request.session['student_id']
    del request.session['student_name']
    return HttpResponse(json.dumps({'status': 1}), content_type='json')  # 1，退出成功


def IsLogin(func):
    def wrapper(obj, request):
        if request.session.get('id'):
            func(obj, request)
        else:
            return HttpResponseRedirect(reverse('quality:login'))
    return wrapper


class Index(View):
    # @IsLogin
    def get(self, request):
        res = {}
        res['student_id'] = request.session.get('student_id')
        res['student_name'] = request.session.get('student_name')
        return render(request, 'quality/index.html', res)


class Info(View):
    def get(self, request):
        student = Student.objects.get(id=int(request.session.get('id')))
        res = {
            "student_name": student.student_name,
            "sex": student.sex,
            "nation": student.nation,
            "student_department": student.student_department,
            "student_grade": student.student_grade,
            "political_satus": student.political_satus,
            "duty": student.duty,
            "address": student.address,
            "contact": student.contact,
            "parent_contact": student.parent_contact,
            "account": student.account,
        }
        return render(request, 'quality/info.html', res)

    def post(self, request):
        student = Student.objects.get(id=int(request.session.get('id')))
        # student.student_name = request.POST.get('student_name')
        student.sex = request.POST.get('sex')
        student.nation = request.POST.get('nation')
        # student.student_department = request.POST.get('student_department')
        # student.student_grade = request.POST.get('student_grade')
        student.political_satus = request.POST.get('political_satus')
        student.duty = request.POST.get('duty')
        student.address = request.POST.get('address')
        student.contact = request.POST.get('contact')
        student.parent_contact = request.POST.get('parent_contact')
        student.account = request.POST.get('account')
        student.save()
        return HttpResponse(json.dumps({'status': 1}), content_type='json')  # 1，修改成功


class ChangePass(View):
    def get(self, request):
        return render(request, 'quality/changepass.html')

    def post(self, request):
        old_pass = base.encodepass( request.POST.get('old_pass') )
        new_pass = base.encodepass( request.POST.get('new_pass') )
        student = Student.objects.get(id=int(request.session.get('id')))
        if student.password == old_pass:
            student.password = new_pass
            student.save()
            return HttpResponse(json.dumps({'status': 1}), content_type='json')  # 1，修改成功
        else:
            return HttpResponse(json.dumps({'status': 2}), content_type='json')  # 2，原密码错误


class Quality(View):
    def get(self, request):
        terms =  Term.objects.all().order_by('-id')
        for term in terms:
            term.praises = PraiseRecord.objects.filter(term=term)
            term.publishes = PublishmentRecord.objects.filter(term=term)
            term.remark = Remark.objects.filter(term=term)[0].text.split('\n')
        res = {'terms': terms}
        return render(request, 'quality/quality.html', res)

    def post(self, request):
        pass

def praise_info(request):
    praise = PraiseRecord.objects.get(id = int(request.POST.get('id')))
    res = {
        "type": praise.praise_type.name,
        "standard": PraiseRecord.standard_choice[int(praise.standard)-1][1],
        "text": praise.text,
        "description": praise.description,
        "image": praise.image.url if praise.image else '',
        "praise_time": praise.praise_time.strftime('%Y-%m-%d')
    }
    return HttpResponse(json.dumps(res), content_type='json')

def publish_info(request):
    publish = PublishmentRecord.objects.get(id = int(request.POST.get('id')))
    res = {
        "type": publish.publish_type.name,
        "text": publish.text,
        "description": publish.description,
        "image": publish.image.url if publish.image else '' ,
        "publish_time": publish.publish_time.strftime('%Y-%m-%d')
    }
    return HttpResponse(json.dumps(res), content_type='json')

