import base64
from datetime import datetime
from _thread import start_new_thread
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .encode_faces import enf
from .recognize_face import rec_face_image
# Create your views here.
from SE.models import *
from SE.test import checkans
from django.core.files.base import ContentFile
status=True
facelist=[]
uid=0
studentid=0
examid=0
facestatus=0
YDATA=[]
PERCENTAGE_CHEAT=0
def first(request):
    return render(request, 'mindex.html')



def aboutus(request):
    return render(request, 'about_us.html')
def lg(request):
    return render(request, 'loginindex.html')


def logincode(request):
    uname=request.POST['textfield']
    pswd=request.POST['textfield2']
    try:
        ob=login_table.objects.get(username=uname,password=pswd)
        if ob.type == "admin":
            return HttpResponse('''<script>alert('Welcome');window.location='/adminpg'</script>''')
        elif ob.type == "staff":
            request.session["lid"]=ob.id
            return HttpResponse('''<script>alert('Welcome');window.location='/shme'</script>''')
        elif ob.type == "student":
            request.session["lid"] = ob.id
            ob2=students_table.objects.get(LOGIN=ob.id)
            request.session["student_course"]=ob2.COURSE.id
            request.session["student_sem"]=ob2.Sem
            return HttpResponse('''<script>alert('Welcome');window.location='/stdhme'</script>''')
        else:
            return HttpResponse('''<script>alert('Invalid Username or password');window.location='/'</script>''')
    except Exception as e:
        print(e,"==")
        print(e,"==")
        print(e,"==")
        return HttpResponse('''<script>alert('Invalid Username or password');window.location='/'</script>''')


def add_crs(request):
    return render(request, 'admin/add course.html')

def add_not(request):
    return render(request, 'admin/ADD NOTI.html')


def add_q(request):
    ob=exam_table.objects.filter(subject__STAFF__LOGIN__id=request.session['lid'])
    return render(request, 'staff/Add q.html',{'val':ob})


def editqs(request,id):
    request.session['oo']=id
    ob=assign_sub_table.objects.filter(STAFF__LOGIN__id=request.session['lid'])
    obb=question_table.objects.get(id=id)
    return render(request,"staff/edit question.html",{"val":ob,'v':obb})


def edit_question(request):
    question = request.POST['textfield']
    answer = request.POST['textfield2']
    asub = request.POST['select']
    ob = question_table.objects.get(id=request.session['oo'])
    ob.assign_sub=assign_sub_table.objects.get(id=asub)
    ob.question = question
    ob.answer = answer
    ob.save()
    return HttpResponse('''<script>alert('Edited succesfully');window.location='/mng_qus'</script>''')


def add_question(request):
    question = request.POST['textfield']
    answer = request.POST['textfield2']
    m = request.POST['m']
    asub = request.POST['select']
    ob = question_table()
    ob.EXAMID=exam_table.objects.get(id=asub)
    ob.question = question
    ob.answer = answer
    ob.mark = m
    ob.save()
    return HttpResponse('''<script>alert('added succesfully');window.location='/mng_qus'</script>''')

def add_staf(request):
    return render(request, 'admin/add staff.html')

def add_std(request):
    ob=courses_table.objects.all()
    obb=students_table.objects.all()
    return render(request, 'staff/add student.html',{'val':ob,'val1':obb})

def search_std(request):
    ob = courses_table.objects.all()
    cid=request.POST['select']
    sem=request.POST['select2']
    obb = students_table.objects.filter(COURSE__id=cid,Sem=sem)
    return render(request, 'staff/add student.html', {'val': ob, 'val1': obb})

def acpt_std(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='student'
    ob.save()
    return HttpResponse('''<script>alert('Accepted');window.location='/add_std'</script>''')


def rjt_std(request,id):
    ob = login_table.objects.get(id=id)
    ob.type = 'reject'
    ob.save()
    return HttpResponse('''<script>alert('Rejected');window.location='/add_std'</script>''')


def add_std_delete(request,id):
    ob = login_table.objects.get(id=id)

    ob.delete()
    return HttpResponse('''<script>alert('Rejected');window.location='/add_std'</script>''')

def addstaffcode(request):
    fname=request.POST['textfield']
    lname=request.POST['textfield2']
    gender=request.POST['radio']
    qualification=request.POST['textfield3']
    experience = request.POST['textfield4']
    phone = request.POST['textfield5']
    email = request.POST['textfield6']
    place = request.POST['textfield7']
    username = request.POST['textfield8']
    password = request.POST['textfield9']
    f = request.FILES['f']
    fs=FileSystemStorage()
    fn=fs.save(f.name,f)

    ob=login_table()
    ob.username=username
    ob.password=password
    ob.type="staff"
    ob.save()


    obb=staff_table()
    obb.LOGIN=ob
    obb.firstname=fname
    obb.lastname=lname
    obb.qualification=qualification
    obb.experience=experience
    obb.place=place
    obb.gender=gender
    obb.phone=phone
    obb.email=email
    obb.image=fn
    obb.save()
    return HttpResponse('''<script>alert('added succesfully');window.location='/mng_staf'</script>''')


def addcoursecode(request):
    course = request.POST['textfield']
    description = request.POST['textfield2']
    ob=courses_table()
    ob.course=course
    ob.description=description
    ob.save()
    return HttpResponse('''<script>alert('added succesfully');window.location='/mng_crs'</script>''')


def addsubcode(request):
    cid=request.POST['select']
    sub=request.POST['textfield']
    sem=request.POST['select2']
    ob=subject_table()
    ob.COURSE=courses_table.objects.get(id=cid)
    ob.subject=sub
    ob.Sem=sem
    ob.save()
    return HttpResponse('''<script>alert('added succesfully');window.location='/mng_sub'</script>''')



def add_sub(request):
    ob=courses_table.objects.all()
    return render(request, 'admin/add sub.html',{'val':ob})
def adminpg(request):
    return redirect('/adminhm')

def adminhm(request):
    return render(request,'admin/adminindex.html')

def assignsub(request):
    return render(request, 'admin/ASSIGN SUB.html')

def admexm(request):
    exam_id = []
    ob = exam_table.objects.filter(subject__SUBJECT__COURSE__id=request.session["student_course"],subject__SUBJECT__Sem=request.session["student_sem"])
    for i in ob:
        ob1 = attend_exam.objects.filter(STUDENT__LOGIN_id=request.session['lid'],QUESTION__EXAMID__id=i.id)
        print(ob1,"kkkkkkkkkkkkkkkkkkkkkkk")
        print(ob1,"kkkkkkkkkkkkkkkkkkkkkkk")
        print(ob1,"kkkkkkkkkkkkkkkkkkkkkkk")
        if len(ob1)>0:
            i.stts="no"
        else:
            i.stts="yes"
    return render(request, 'student/view exm.html',{'val':ob})

    # exam_id = []
    # not_attend=[]
    # union_set = []
    # attend = []
    # ob1 = attend_exam.objects.filter(STUDENT__LOGIN_id=request.session['lid'])
    # for i in ob1:
    #     exam_id.append(i.QUESTION.EXAMID.id)
    # not_attend_ob = exam_table.objects.filter(subject__SUBJECT__COURSE__id=request.session["student_course"],subject__SUBJECT__Sem=request.session["student_sem"]).exclude( id__in=exam_id)
    #
    # for i in not_attend_ob:
    #     not_attend = {"name":i.name, "exam": i.subject.SUBJECT.subject,"date": str(i.date), "time": str(i.time), "status": "attended"}
    #
    # attend_ob = exam_table.objects.filter(subject__SUBJECT__COURSE__id=request.session["student_course"],
    #                                           subject__SUBJECT__Sem=request.session["student_sem"], id__in=exam_id)
    #
    # for i in attend_ob:
    #     attend = {"name": i.name, "exam": i.subject.SUBJECT.subject, "date": str(i.date), "time": str(i.time),
    #                   "status": "not attended"}
    # union_set = not_attend | attend
    # return render(request, 'student/view exm.html',{'val':ob})


def cws(request):
    return render(request, 'staff/chat with student.html')
def mng_crs(request):
    ob = courses_table.objects.all()
    return render(request, 'admin/manage course.html',{'val':ob})
def mng_crs_delete(request,id):
    ob=courses_table.objects.filter(id=id).delete()
    return HttpResponse('''<script>alert('deleted succesfully');window.location='/mng_crs'</script>''')
def mng_crs_edit(request,id):
    request.session['cid'] = id
    ob=courses_table.objects.get(id=id)
    return render(request,'admin/edit_course.html',{"data":ob})

def course_edit(request):
    course = request.POST['textfield']
    description = request.POST['textfield2']
    ob=courses_table.objects.get(id=request.session['cid'])
    ob.course=course
    ob.description=description
    ob.save()
    return HttpResponse('''<script>alert('updated succesfully');window.location='/mng_crs'</script>''')
def mng_ntf(request):
    return render(request, 'admin/manage notifica.html')
def mng_qus(request):
    ob = question_table.objects.filter(EXAMID__subject__STAFF__LOGIN=request.session["lid"])
    obb = exam_table.objects.filter(subject__STAFF__LOGIN_id=request.session['lid'])
    return render(request,'staff/manage questions.html',{'exam':obb,"sub":ob})
def search_qus(request):

    search = request.POST['select']
    ob = question_table.objects.filter(EXAMID__subject__STAFF__LOGIN=request.session["lid"],EXAMID__id=search)
    obb = exam_table.objects.filter(subject__STAFF__LOGIN_id=request.session['lid'])
    return render(request, 'staff/manage questions.html', {'exam': obb, "sub": ob})

def mng_qus_delete(request,id):
    ob=question_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert('deleted succesfully');window.location='/mng_qus'</script>''')

def mng_staf(request):
    ob=staff_table.objects.all()
    return render(request, 'admin/manage stff.html',{'val':ob})

def mng_staf_delete(request,id):
    ob=staff_table.objects.filter(id=id).delete()
    return HttpResponse('''<script>alert('deleted succesfully');window.location='/mng_staf#about'</script>''')

def mng_staf_edit(request,id):
    request.session['sid']=id
    ob=staff_table.objects.get(id=id)
    return render(request,'admin/edit_staff.html',{"data":ob})

def edit_staf(request):
    fname=request.POST['textfield']
    lname=request.POST['textfield2']
    gender=request.POST['radio']
    qualification=request.POST['textfield3']
    experience = request.POST['textfield4']
    phone = request.POST['textfield5']
    email = request.POST['textfield6']
    place = request.POST['textfield7']

    obb=staff_table.objects.get(id=request.session['sid'])
    obb.firstname=fname
    obb.lastname=lname
    obb.qualification=qualification
    obb.experience=experience
    obb.place=place
    obb.gender=gender
    obb.phone=phone
    obb.email=email
    obb.save()
    return HttpResponse('''<script>alert('updated succesfully');window.location='/mng_staf#about'</script>''')

def mng_stafsearch(request):
    name=request.POST['textfield']
    ob=staff_table.objects.filter(firstname__icontains=name)
    return render(request, 'admin/manage stff.html',{'val':ob})


def mng_sub(request):
    obc=courses_table.objects.all()
    ob=subject_table.objects.all()
    return render(request, 'admin/manage sub.html',{"val":ob,"obc":obc})

def mng_sub_delete(request,id):
    ob=subject_table.objects.filter(id=id).delete()
    return HttpResponse('''<script>alert('deleted succesfully');window.location='/mng_sub'</script>''')


def assignsub(request):
    obs=staff_table.objects.all()
    oba=assign_sub_table.objects.all()
    sub=[]
    for i in oba:
        sub.append(i.SUBJECT.id)
    ob = subject_table.objects.all()
    return render(request, 'admin/ASSIGN SUB.html',{"val":ob,"val1":obs})

def view_assng_staff(request):
    ob=assign_sub_table.objects.all()
    return render(request, 'admin/view assigned staff.html',{'val':ob})

def assign_sub_delete(request,id):
    ob=assign_sub_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert('deleted succesfully');window.location='/view_assng_staff#about'</script>''')


def search_sub(request):
    sem=request.POST['select2']
    crs=request.POST['select']
    obc = courses_table.objects.all()
    ob = subject_table.objects.filter(COURSE__id=crs,Sem=sem)
    return render(request, 'admin/manage sub.html', {"val": ob, "obc": obc})


def assign_sub_staff(request):
    staff = request.POST['select']
    subject = request.POST['select2']
    ob=assign_sub_table()
    ob.SUBJECT = subject_table.objects.get(id=subject)
    ob.STAFF =staff_table.objects.get(id=staff)
    ob.save()
    return HttpResponse('''<script>alert('assign succesfully');window.location='/view_assng_staff#about'</script>''')


def vc(request):
    ob = complaint_table.objects.all()
    return render(request, 'admin/view complaint.html', {'val': ob})

def vc_reply(request,id):
    request.session['cid']=id
    return render(request,'admin/reply_complaint.html')

def reply_post(request):
    fname=request.POST['textarea']
    ob=complaint_table.objects.get(id=request.session['cid'])
    ob.reply=fname
    ob.save()
    return HttpResponse('''<script>alert('updated succesfully');window.location='/mng_staf#about'</script>''')


def view_crs_search(request):
    name = request.POST['textfield']
    ob = courses_table.objects.filter(course__icontains=name)

    return render(request, 'admin/manage course.html', {'val': ob})

def vfb(request):
    ob=feedback_table.objects.all()
    return render(request, 'admin/view feedback.html',{'val':ob})

def scvr(request):
    res=complaint_table.objects.filter(STUDENT__LOGIN=request.session["lid"])
    return render(request, 'student/send complt viw rply.html',{'data':res})
def scvr_post(request):
    complaint = request.POST['textfield']
    ob = complaint_table()
    ob.complaint = complaint
    ob.date = datetime.today()
    ob.reply='pending'
    ob.STUDENT = students_table.objects.get(LOGIN__id=request.session["lid"])
    ob.save()
    return HttpResponse('''<script>alert('Complaint send succesfully');window.location='/scvr#about'</script>''')
def sdfd(request):
    ob=staff_table.objects.all()
    return render(request, 'student/send feedback.html',{'val': ob})




def send_feedback(request):
    feedback = request.POST['textfield']
    staff=request.POST['select']
    ob=feedback_table()
    ob.feedback=feedback
    ob.date=datetime.today()
    ob.STAFF=staff_table.objects.get(id=staff)
    ob.STUDENT=students_table.objects.get(LOGIN__id=request.session["lid"])
    ob.save()
    return HttpResponse('''<script>alert('feedback send succesfully');window.location='/sdfd#about'</script>''')

def sdrp(request):
    return render(request, 'staff/send reply.html')
def sup(request):
    obc = courses_table.objects.all()
    return render(request, 'student/sign_up_index.html',{"c":obc})

def addsup(request):
    Fname=request.POST['textfield']
    Lname=request.POST['textfield2']
    Gender=request.POST['checkbox']
    Course=request.POST['select2']
    Sem=request.POST['sem']
    Place=request.POST['textfield7']
    Phone= request.POST['textfield6']
    Email=request.POST['textfield5']
    Username= request.POST['textfield4']
    Password = request.POST['textfield3']

    ob=login_table()
    ob.username = Username
    ob.password = Password
    ob.type='pending'
    ob.save()
    f = request.FILES['f']
    fs = FileSystemStorage()
    fn = fs.save(f.name, f)

    obj=students_table()
    obj.LOGIN=ob
    obj.firstname=Fname
    obj.Lname=Lname
    obj.gender=Gender
    obj.COURSE=courses_table.objects.get(id=Course)
    obj.Sem=Sem
    obj.place=Place
    obj.phone=Phone
    obj.email=Email
    obj.image = fn
    obj.save()
    return HttpResponse('''<script>alert('added succesfully');window.location='/'</script>''')





def editexam(request,id):
    request.session['pp']=id
    ob = assign_sub_table.objects.filter(STAFF=staff_table.objects.get(LOGIN=request.session["lid"]))
    obb=exam_table.objects.get(id=id)
    return render(request, "staff/edit exam.html", {'ob':ob, 'val':obb, 'date':str(obb.date), 'time':str(obb.time)})

def update_exam_post(request):
    subject = request.POST['select']
    date = request.POST['d1']
    time = request.POST['t1']
    ob=exam_table.objects.get(id=request.session['pp'])
    ob.subject = assign_sub_table.objects.get(id=subject)
    ob.date=date
    ob.time=time
    ob.save()
    return HttpResponse('''<script>alert('updaded');window.location='/manage_exam'</script>''')




def shme(request):
    return render(request, 'staff/newstaffindex.html')
def stdhme(request):
    return render(request, 'student/index_student.html')




#----------------------------------staff

def add_exm(request):
    ob = assign_sub_table.objects.filter(STAFF__LOGIN=request.session["lid"])
    return render(request, 'staff/Add exam.html', {'ob':ob})

def add_exam_post(request):
    name=request.POST['exam_name']
    subject = request.POST['select']
    date = request.POST['d1']
    time = request.POST['t1']
    ob=exam_table()
    ob.name=name
    ob.subject_id =subject
    ob.date=date
    ob.time=time
    ob.save()
    return HttpResponse('''<script>alert('added');window.location='/manage_exam'</script>''')

def delete_exam_post(request,id):
    ob = exam_table.objects.filter(id=id)
    ob.delete()
    return HttpResponse('''<script>alert('deleted succesfully');window.location='/manage_exam'</script>''')


def manage_exam(request):
    ob=exam_table.objects.filter(subject__STAFF__LOGIN=request.session["lid"])
    return render(request, 'staff/manage exam.html', {'val':ob})



def viewexam1(request):
    ob=exam_table.objects.all()
    return render(request, 'student/examview.html', {'val':ob})



def resultviewpost(request,id):
    request.session['eid']=id
    ob=attend_exam.objects.filter(QUESTION__EXAMID__id=id,STUDENT__LOGIN__id=request.session['lid'])
    sid=[]
    for i in ob:
        sid.append(i.STUDENT.id)
    obs=students_table.objects.filter(id__in=sid)
    for i in obs:
        ob = attend_exam.objects.filter(QUESTION__EXAMID__id=id,STUDENT__id=i.id,STUDENT__LOGIN__id=request.session['lid'])
        tm=0
        fm = 0
        for j in ob:
            tm += float(j.mark)
            fm += float(j.QUESTION.mark)
        i.tm = str(tm) + "/" + str(fm)



    return render(request, 'student/resultview.html', {'val':obs})



def result_exam_post(request,id):
    request.session['eid']=id
    ob=attend_exam.objects.filter(QUESTION__EXAMID__id=id)
    sid=[]
    for i in ob:
        sid.append(i.STUDENT.id)
    obs=students_table.objects.filter(id__in=sid)
    for i in obs:
        ob = attend_exam.objects.filter(QUESTION__EXAMID__id=id,STUDENT__id=i.id)
        tm=0
        fm=0
        for j in ob:
            tm+=float(j.mark)
            fm+=float(j.QUESTION.mark)
        i.tm=str(tm)+"/"+str(fm)
    return render(request, 'staff/view reslt.html', {'val':obs})








def vexamd(request,id):
    eid=request.session['eid']
    ob=report_exam.objects.filter(STUDENT__id=id,EXAMID__id=eid,type='X_AXIS_CHEAT')
    r=[]
    r.append(len(ob))
    ob = report_exam.objects.filter(STUDENT__id=id, EXAMID__id=eid, type='Y_AXIS_CHEAT')
    r.append(len(ob))

    ob = report_exam.objects.filter(STUDENT__id=id, EXAMID__id=eid, type='multiple persons')
    r.append(len(ob))

    ob = report_exam.objects.filter(STUDENT__id=id, EXAMID__id=eid, type='phone')
    r.append(len(ob))

    ob = report_exam.objects.filter(STUDENT__id=id, EXAMID__id=eid, type='audio')
    r.append(len(ob))
    r.append(0)
    ob=report_examimage.objects.filter(STUDENT__id=id, EXAMID__id=eid)


    return render(request, 'staff/view reslt1.html', {'val':r,"imgs":ob})





def viewanswers(request,id):
    eid=request.session['eid']
    ob=attend_exam.objects.filter(STUDENT__id=id,QUESTION__EXAMID__id=eid)

    return render(request, 'staff/viewanswers.html', {'val':ob})









def vasubstf(request):
    ob=assign_sub_table.objects.filter(STAFF=staff_table.objects.get(LOGIN=request.session["lid"]))
    return render(request, 'staff/view assgn sub to stff.html',{"data":ob})

def vasub(request):
    ob = assign_sub_table.objects.filter(STAFF=staff_table.objects.get(LOGIN=request.session["lid"]))
    print("===",ob)
    print("===",request.session["lid"])
    return render(request, 'staff/view assigned subject.html',{"data":ob})


def manage_notes(request):
    ob=notes_table.objects.all()
    return render(request, 'staff/managenote.html',{'val':ob})

def mng_note_delete(request,id):
    ob=notes_table.objects.filter(id=id)
    ob.delete()
    return HttpResponse('''<script>alert('deleted succesfully');window.location='/manage_notes'</script>''')

def edit_note(request,id):
    request.session['oo']=id
    ob=notes_table.objects.get(id=id)
    sub = assign_sub_table.objects.filter(STAFF__LOGIN=request.session["lid"])
    return render(request,"staff/edit note.html",{"val":ob,'subj':sub})



def edit_notes(request):
    try:
        import datetime
        subid = request.POST["select"]
        note = request.FILES["file"]
        fs = FileSystemStorage()
        fsa = fs.save(note.name, note)
        ob = notes_table.objects.get(id=request.session['oo'])
        ob.SUBJECT_id = subid
        ob.NOTES = fsa
        ob.DATE = datetime.datetime.now()
        ob.save()
        return HttpResponse('''<script>alert('Edited');window.location='/manage_notes'</script>''')
    except:
        import datetime
        subid = request.POST["select"]

        ob = notes_table.objects.get(id=request.session['oo'])
        ob.SUBJECT_id = subid
        ob.DATE = datetime.datetime.now()
        ob.save()
        return HttpResponse('''<script>alert('Edited');window.location='/manage_notes'</script>''')


def staff_add_note(request):
    sub = assign_sub_table.objects.filter(STAFF__LOGIN=request.session["lid"])
    return render(request, 'staff/Add note.html', {"subj": sub})

def mang_notes_post(request):
    import datetime
    subid=request.POST["select"]
    note=request.FILES["file"]
    fs=FileSystemStorage()
    fsa=fs.save(note.name,note)

    ob=notes_table()
    ob.SUBJECT_id=subid
    ob.NOTES=fsa
    ob.DATE=datetime.datetime.now()
    ob.save()
    return HttpResponse('''<script>alert('added');window.location='/manage_notes'</script>''')

def ve(request):
    return render(request, 'student/view exm.html')

def vfbk(request):
    ob = feedback_table.objects.all()
    return render(request, 'staff/view feedbk.html',{"val":ob})

def vnoti(request):
    return render(request, 'staff/view noti.html')
def wrst(request):
    return render(request, 'staff/view reslt.html')

def manage_pq(request):
    ob = previous_question.objects.filter(assign_sub__STAFF__LOGIN=request.session["lid"])
    return render(request, 'staff/prev question.html',{"sub":ob})


def pq_delete(request,id):
    ob=previous_question.objects.filter(id=id).delete()
    return HttpResponse('''<script>alert('deleted succesfully');window.location='/manage_pq'</script>''')

def edit_prv_qs(request,id):
    request.session['oo']=id
    ob=assign_sub_table.objects.filter(STAFF__LOGIN__id=request.session['lid'])
    obb=previous_question.objects.get(id=id)
    return render(request,"staff/edit prv question.html",{"val":ob,'v':obb})


def editprecode(request):
    try:
        question = request.FILES['textfield']
        fp = FileSystemStorage()
        fs = fp.save(question.name, question)
        answer = request.POST['textfield2']
        asub = request.POST['select']
        ob = previous_question.objects.get(id=request.session['oo'])
        ob.assign_sub = assign_sub_table.objects.get(id=asub)
        ob.question = fs
        ob.year = answer
        ob.save()
        return HttpResponse('''<script>alert('Edited succesfully');window.location='/manage_pq'</script>''')
    except:

        answer = request.POST['textfield2']
        asub = request.POST['select']
        ob = previous_question.objects.get(id=request.session['oo'])
        ob.assign_sub = assign_sub_table.objects.get(id=asub)
        ob.year = answer
        ob.save()
        return HttpResponse('''<script>alert('Edited succesfully');window.location='/manage_pq'</script>''')


def add_prev_qstn(request):
    ob=assign_sub_table.objects.filter(STAFF__LOGIN__id=request.session['lid'])
    return render(request, 'staff/add previous question.html',{"val":ob})


def add_prv_qus(request):
    question = request.FILES['textfield']
    fp=FileSystemStorage()
    fn=fp.save(question.name,question)
    answer = request.POST['textfield2']
    asub = request.POST['select']
    ob = previous_question()
    ob.assign_sub=assign_sub_table.objects.get(id=asub)
    ob.question = fn
    ob.year = answer
    ob.save()
    return HttpResponse('''<script>alert('added succesfully');window.location='/manage_pq'</script>''')

def srch_prv_qs(request):
    date = request.POST['textfield']
    ob = previous_question.objects.filter()
    return render(request, 'staff/prev question.html',{'val':ob})

def view_notes(request):
    obb=students_table.objects.get(LOGIN__id=request.session['lid'])
    cid=obb.COURSE.id
    ob = subject_table.objects.filter(COURSE__id=cid)
    obb1=notes_table.objects.filter(SUBJECT__COURSE__id=cid)
    return render(request,'student/viewnotes.html',{"val":ob,"val1":obb1})

def srch_note_std(request):
    obb = students_table.objects.get(LOGIN__id=request.session['lid'])
    cid = obb.COURSE.id
    ob = subject_table.objects.filter(COURSE__id=cid)
    sid=request.POST['select']
    obb = notes_table.objects.filter(SUBJECT__id=sid)
    return render(request, 'student/viewnotes.html', {'val': ob, 'val1': obb,'sid':int(sid)})

def view_prev_qsnt(request):
    obb = students_table.objects.get(LOGIN__id=request.session['lid'])
    cid = obb.COURSE.id
    ob = subject_table.objects.filter(COURSE__id=cid)
    obb1 = previous_question.objects.filter(assign_sub__SUBJECT__COURSE__id=cid)
    return render(request, 'student/viewprev qstn.html',{'val': ob,'val1':obb1})

def srch_prv_note_std(request):
    obb = students_table.objects.get(LOGIN__id=request.session['lid'])
    cid = obb.COURSE.id
    ob = subject_table.objects.filter(COURSE__id=cid)
    sid=request.POST['select']
    obb = previous_question.objects.filter(assign_sub__SUBJECT__id=sid)
    return render(request, 'student/viewprev qstn.html', {'val': ob, 'val1': obb,'sid':int(sid)})


def add_notes(request):
    return render(request, 'staff/Add note.html')




def viewrslt(request):
    obb = students_table.objects.get(LOGIN__id=request.session['lid'])
    cid = obb.COURSE.id
    ob1=exam_table.objects.filter(subject__SUBJECT__COURSE__id=cid)
    ob = subject_table.objects.filter(COURSE__id=cid)
    return render(request, 'student/view result.html',{'val':ob,'val1':ob1})



def viewrslt_search(request):
    subid=request.POST['select']
    exid=request.POST['select1']

    obbn = students_table.objects.get(LOGIN__id=request.session['lid'])
    cid = obbn.COURSE.id
    ob1=exam_table.objects.filter(subject__SUBJECT__COURSE__id=cid)
    ob = subject_table.objects.filter(COURSE__id=cid)
    obb = attend_exam.objects.filter(STUDENT__LOGIN__id=request.session['lid'], QUESTION__EXAMID__subject__SUBJECT__id=subid,QUESTION__EXAMID__id=exid)
    test = []
    for item in obb:
        if item.QUESTION.EXAMID not in test:
            test.append(item.QUESTION.EXAMID)
            ob2 = attend_exam.objects.filter(QUESTION__EXAMID=item.QUESTION.EXAMID)
            print(ob2,"llllllllllllllllllllllllllll")
            total_marks = 0
            for i in ob2:
                total_marks = int(total_marks) + int(i.mark)
            test.append(total_marks)
            # row={"testname":i.QUESTION__EXAMID.subject.SUBJECT.subje,"score":total_marks}
            print(test,"dddddddddddddddddddddddddd")
            return render(request, 'student/view result.html', {"t": total_marks, "val": ob, 'val1': ob1})

        else:
            return HttpResponse('''<script>alert('where is no data);window.location='/viewrslt'</script>''')

    return render(request, 'student/view result.html',{"val":ob,'val1':ob1})



#_____________STAFF CHAT______________________



def chatwithuser(request):
    ob = students_table.objects.all()
    return render(request,"staff/fur_chat.html",{'val':ob})




def chatview(request):
    ob = students_table.objects.all()
    d=[]
    for i in ob:
        r={"name":i.firstname+" "+i.Lname,'photo':i.image.url,'email':i.email,'loginid':i.LOGIN.id}
        d.append(r)
    return JsonResponse(d, safe=False)




def coun_insert_chat(request,msg,id):
    try:
        print("===",msg,id)
        ob=chat_table()
        ob.FROM=login_table.objects.get(id=request.session['lid'])
        ob.TO=login_table.objects.get(id=id)
        ob.message=msg
        ob.date=datetime.now().strftime("%Y-%m-%d")
        ob.time="10:30:25"
        ob.save()

        return JsonResponse({"task":"ok"})
    except Exception as e:
        print(e,"---------------------")
        return JsonResponse({"task": "invalid"})
    # refresh messages chatlist



def coun_msg(request,id):

    ob1=chat_table.objects.filter(FROM__id=id,TO__id=request.session['lid'])
    ob2=chat_table.objects.filter(FROM__id=request.session['lid'],TO__id=id)
    combined_chat = ob1.union(ob2)
    combined_chat=combined_chat.order_by('id')
    res=[]
    for i in combined_chat:
        res.append({"from_id":i.FROM.id,"msg":i.message,"date":str(i.date),"chat_id":i.id})

    obu=students_table.objects.get(LOGIN__id=id)


    return JsonResponse({"data":res,"name":obu.firstname+" "+obu.Lname,"photo":obu.image.url,"user_lid":obu.LOGIN.id})





#_________________STUDENT CHAT____________________




def chatwithuser1(request):
    ob = staff_table.objects.all()
    return render(request,"student/fur_chat.html",{'val':ob})




def chatview1(request):
    ob = staff_table.objects.all()
    d=[]
    for i in ob:
        r={"name":i.firstname+" "+i.lastname,'photo':i.image.url,'email':i.email,'loginid':i.LOGIN.id}
        d.append(r)
    return JsonResponse(d, safe=False)




def coun_insert_chat1(request,msg,id):
    print("===",msg,id)
    ob=chat_table()
    ob.FROM=login_table.objects.get(id=request.session['lid'])
    ob.TO=login_table.objects.get(id=id)
    ob.message=msg
    ob.date=datetime.now().strftime("%Y-%m-%d")
    ob.time=datetime.now().strftime("%Y-%m-%d")
    ob.save()

    return JsonResponse({"task":"ok"})
    # refresh messages chatlist



def coun_msg1(request,id):

    ob1=chat_table.objects.filter(FROM__id=id,TO__id=request.session['lid'])
    ob2=chat_table.objects.filter(FROM__id=request.session['lid'],TO__id=id)
    combined_chat = ob1.union(ob2)
    combined_chat=combined_chat.order_by('id')
    res=[]
    for i in combined_chat:
        res.append({"from_id":i.FROM.id,"msg":i.message,"date":str(i.date),"chat_id":i.id})
    obu=staff_table.objects.get(LOGIN__id=id)
    return JsonResponse({"data":res,"name":obu.firstname+" "+obu.lastname,"photo":obu.image.url,"user_lid":obu.LOGIN.id})
def face_verification():
    import cv2

    # Create a VideoCapture object
    cap = cv2.VideoCapture(0)  # Use 0 for the default camera, change to another number if you have multiple cameras

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()

    # Loop to capture frames from the camera
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Check if the frame is read correctly
        if not ret:
            print("Error: Unable to read frame.")
            break

        # Display the captured frame
        cv2.imshow('Frame', frame)

        # Check for the 'q' key to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite(r"D:\sub_eval\sub_eval\media\sample.png",frame)
            break

    # Release the VideoCapture object and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()
    return ""


def view_sample_question(request,id):

        from datetime import date
        today = date.today()
        print(today,"ppppppppppp")
        # qq="SELECT * FROM `test_result` WHERE DATE=CURDATE() AND `candidate_id`=%s and status='completed'"
        res=attend_exam.objects.filter(QUESTION__EXAMID__id=id,STUDENT__LOGIN__id=request.session['lid'])
        # res=selectone(qq,session['lid'])
        if len(res)==0:
            global studentid
            studentid=request.session['lid']
            global  examid
            examid=id

            obstu=students_table.objects.get(LOGIN__id=request.session['lid'])

            enf([['face',str(obstu.image)]])
            res=face_verification()
            reslist = rec_face_image(r"D:\sub_eval\sub_eval\media\sample.png")
            if len(reslist)==0:
                return HttpResponse('''<script>alert("Face verification failed");window.location="/admexm"</script>''')
            start_new_thread(camclick, ())
            start_new_thread(sound_analysis, ())
            res=question_table.objects.filter(EXAMID__id=id)
            tid = id
            cid = 1
            cnt=0
            request.session['tid']=tid
            request.session['cnt']=cnt
            q=[]
            # res=selectall("SELECT * FROM `qa` WHERE `exam_id`='"+str(tid)+"'")

            if len(res) != 0:
                s=False
                if len(res)-1 == cnt:
                    s=True

                return render(request,'student/sample.html',{'data':res[0],"s":s,'cnt':int(cnt), 'ln':len(res)})
            else:
                return HttpResponse('''<script>alert("No Questions");window.location="/admexm"</script>''')

        else:
            return HttpResponse('''<script>alert("Attended");window.location="/admexm"</script>''')


import random



def get_data(request):
    # Generate sample x and y values (replace with your data retrieval logic)
    global YDATA
    global PERCENTAGE_CHEAT
    XDATA = list(range(200))
    x_values = XDATA
    y_values = YDATA

    # Return x and y values as JSON
    data = {'x': list(x_values), 'y': y_values,"z":PERCENTAGE_CHEAT}
    print(data)
    return JsonResponse(data)
def save_base64_image(base64_string, file_path):
    # Split the base64 string to get the header and data
    header, data = base64_string.split(',', 1)

    # Decode the base64 data
    image_data = base64.b64decode(data)

    # Write the image data to a file
    with open(file_path, 'wb') as f:
        f.write(image_data)
def save_image(request):
    if request.method == 'POST':
        print(request.POST)
        # Retrieve the image data from the POST request
        image_data = request.POST.get('image_data')
        print(image_data)

        # Decode base64 image data
        # decoded_image_data = base64.b64decode(image_data.split(',')[1])
        save_base64_image(image_data.split(',')[1],r"D:\sub_eval\sub_eval\media\sample.png")
        # Save the image to a file in the media directory

        # captured_image.image.save('captured_image.png', ContentFile(decoded_image_data))

        return JsonResponse({'message': 'Image saved successfully.'})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=400)



def finishexm(request):
    tid = request.session['tid']
    cnt = request.session['cnt']
    uans = request.POST['ans']
    ans = request.POST['rans']
    mark = request.POST['mark']
    res = question_table.objects.filter(EXAMID__id=tid)

    btnv=request.POST['btn']
    if btnv == "next":
        from datetime import date

        tid=request.session['tid']
        cnt=request.session['cnt']
        uans=request.POST['ans']
        ans=request.POST['rans']
        mark=request.POST['mark']
        res = question_table.objects.filter(EXAMID__id=tid)
        # ob=attend_exam()
        # ob.STUDENT = students_table.objects.get(LOGIN__id=request.session['lid'])
        # ob.QUESTION = res[cnt]
        # ob.answer=ans
        #
        # ob.save()


        mm = checkans(uans, ans)

        totalmark = (mm * int(mark))
        print(totalmark, "ttttotal")
        if totalmark<0:
            totalmark=0

        ob = attend_exam()
        ob.STUDENT=students_table.objects.get(LOGIN__id=request.session['lid'])
        ob.QUESTION=res[cnt]
        ob.mark=totalmark
        ob.answer=uans
        ob.status="pending"
        ob.save()
        request.session['cnt'] = cnt + 1
        # res_ans = attend_exam.objects.filter(QUESTION__id=res[cnt].id,STUDENT__LOGIN__id=request.session['lid'])
        # if len(res_ans) == 0:
        #     ob=result_table()
        #     ob.STUDENT=students_table.objects.get(LOGIN__id=request.session['lid'])
        #     ob.EXAM_id=request.session['tid']
        #     ob.result=totalmark
        #     ob.status="pending"
        #     ob.save()
        #     # qry = "INSERT INTO `result` VALUES(NULL,%s,%s,%s,%s)"
        #     # val = (session['lid'], q, user_ans, totalmark)
        #     # ans_id = iud(qry, val)
        # else:
        #     ob=result_table.objects.get(id=res_ans[0].id)
        #     ob.result=totalmark
        #     ob.answer=res_ans
        #     ob.save()
        #     # qry = "UPDATE `result` SET `answer`=%s,`result`=%s WHERE `res_id`=%s"
        #     # val = (user_ans, totalmark, res_ans['res_id'])
        #     # iud(qry, val)
        cnt=cnt+1
        if len(res)==cnt:
            return HttpResponse('''<script>alert("Exam Completed");window.location="/admexm"</script>''')

        else:
            s=False
            if len(res)-1 == cnt:
                s=True
            return render(request,'student/sample.html',{'data':res[cnt],"s":s})
    else:
        from datetime import date

        tid = request.session['tid']
        cnt = request.session['cnt']
        ans = request.POST['ans']
        res = question_table.objects.filter(EXAMID__id=tid)
        ob = attend_exam()
        ob.STUDENT = students_table.objects.get(LOGIN__id=request.session['lid'])
        ob.QUESTION = res[cnt]
        ob.answer = ans
        ob.mark = 10
        ob.save()


        request.session['cnt'] = cnt

        if cnt ==0:
            cnt=cnt
        else:
            cnt=cnt-1


        return render(request, 'student/sample.html', {'data': res[cnt]})

from audioop import avg
from glob import glob
from itertools import count
import cv2
import mediapipe as mp
import numpy as np
import threading as th
import sounddevice as sd
from . import audio
import os
# place holders and global variables
x = 0                                       # X axis head pose
y = 0                                       # Y axis head pose

X_AXIS_CHEAT = 0
Y_AXIS_CHEAT = 0
import time
# import matplotlib.pyplot as plt
def camclick():
    global examid
    global studentid

    PLOT_LENGTH = 200

    # place holders
    GLOBAL_CHEAT = 0
    global PERCENTAGE_CHEAT
    PERCENTAGE_CHEAT = 0
    CHEAT_THRESH = 0.5
    global YDATA
    XDATA = list(range(200))
    YDATA = [0] * 200

    def avg(current, previous):
        if previous > 1:
            return 0.65
        if current == 0:
            if previous < 0.01:
                return 0.01
            return previous / 1.01
        if previous == 0:
            return current
        return 1 * previous + 0.1 * current

    import cv2
    import numpy as np

    # Paths to YOLO files
    weights_path = r"D:\sub_eval\sub_eval\src\yolo-coco\yolov3.weights"
    config_path = r"D:\sub_eval\sub_eval\src\yolo-coco\yolov3.cfg"
    names_path = r"D:\sub_eval\sub_eval\src\yolo-coco\coco.names"
    weightsPath = os.path.sep.join([r"D:\sub_eval\sub_eval\src\yolo-coco", "yolov3.weights"])
    configPath = os.path.sep.join([r"D:\sub_eval\sub_eval\src\yolo-coco", "yolov3.cfg"])

    # load our YOLO object detector trained on COCO dataset (80 classes)
    # and determine only the *output* layer names that we need from YOLO
    print("[INFO] loading YOLO from disk...")
    net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)
    # Load YOLO
    # net = cv2.dnn.readNetFromDarknet(weights_path, config_path)

    # net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)
    ln = net.getLayerNames()
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    output_layers_names = ln
    # Load COCO class labels
    with open(names_path, "r") as f:
        classes = f.read().strip().split("\n")
    global VOLUME_NORM, x, y, X_AXIS_CHEAT, Y_AXIS_CHEAT
    #############################
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

    mp_drawing = mp.solutions.drawing_utils
    # mp_drawing_styles = mp.solutions
    # Capture video from camera
    cap = cv2.VideoCapture(0)

    # plt.show()
    # axes = plt.gca()
    # axes.set_xlim(0, 200)
    # axes.set_ylim(0, 1)
    # line, = axes.plot(XDATA, YDATA, 'r-')
    # plt.title("SUSpicious Behaviour Detection")
    # plt.xlabel("Time")
    # plt.ylabel("Cheat Probablity")
    px=0
    py=0
    ret, frame = cap.read()
    ret, frame = cap.read()
    ret, frame = cap.read()
    ret, frame = cap.read()


    PERCENTAGE_CHEAT=0
    while True:

        ret, frame = cap.read()
        image =frame
        if not ret:
            break
        #  Object Detection Started
        #  Object Detection Started
        #  Object Detection Started
        #  Object Detection Started

        height, width = frame.shape[:2]

        # Create blob from input image
        blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)

        # Set input blob for the network
        net.setInput(blob)

        # Forward pass through the network

        layer_outputs = net.forward(output_layers_names)

        # Lists to store detected bounding boxes, confidences, and class IDs
        boxes = []
        confidences = []
        class_ids = []
        phones="0"
        humans="0"
        hcount=0
        # Process each layer output
        for output in layer_outputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                # Filter out weak predictions and detect persons and mobile phones (indices 0 and 67 in COCO dataset)
                if confidence > 0.5 and (class_id == 0 or class_id == 67):
                    if class_id == 67:

                        ob=report_exam()
                        ob.STUDENT = students_table.objects.get(LOGIN__id=studentid)
                        ob.EXAMID = exam_table.objects.get(id=examid)
                        ob.type='phone'
                        ob.save()
                        fn = datetime.now().strftime("%Y%m%d%H%M%S") + ".png"
                        cv2.imwrite(r"D:\sub_eval\sub_eval\media/" + fn, frame)
                        ob = report_examimage()
                        ob.STUDENT = students_table.objects.get(LOGIN__id=studentid)
                        ob.EXAMID = exam_table.objects.get(id=examid)
                        ob.image = fn
                        ob.save()

                        phones="1"
                    if class_id == 0:
                        hcount+=1
                        humans="1"
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    # Calculate top-left corner of the bounding box
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    # Append to lists
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        # Non-max suppression to remove redundant overlapping boxes
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, score_threshold=0.5, nms_threshold=0.4)

        # Draw bounding boxes and labels
        font = cv2.FONT_HERSHEY_PLAIN
        colors = np.random.uniform(0, 255, size=(len(boxes), 3))
        if len(indexes) > 0:
            for i in indexes.flatten():
                x, y, w, h = boxes[i]
                label = classes[class_ids[i]]
                color = colors[i]
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                cv2.putText(frame, label, (x, y - 5), font, 1, color, 2)
                print ("phone and human detected")
                print ("phone and human detected")
                print ("phone and human detected")
                print ("phone and human detected")
                print(phones,"phones",humans,"humans")
                print ("=======================================")
                print ("=======================================")
        if hcount>1:
            ob = report_exam()
            ob.STUDENT = students_table.objects.get(LOGIN__id=studentid)
            ob.EXAMID = exam_table.objects.get(id=examid)
            ob.type = 'multiple persons'
            ob.save()


        # Head pose detection started
        # Head pose detection started
        # Head pose detection started
        # Head pose detection started


        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

        # To improve performance
        image.flags.writeable = False

        # Get the result
        results = face_mesh.process(image)

        # To improve performance
        image.flags.writeable = True

        # Convert the color space from RGB to BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        img_h, img_w, img_c = image.shape
        face_3d = []
        face_2d = []

        face_ids = [33, 263, 1, 61, 291, 199]


        try:
            if results.multi_face_landmarks:
                for face_landmarks in results.multi_face_landmarks:
                    mp_drawing.draw_landmarks(
                        image=image,
                        landmark_list=face_landmarks,
                        connections=mp_face_mesh.FACEMESH_CONTOURS,
                        landmark_drawing_spec=None)
                    for idx, lm in enumerate(face_landmarks.landmark):
                        # print(lm)
                        if idx in face_ids:
                            if idx == 1:
                                nose_2d = (lm.x * img_w, lm.y * img_h)
                                nose_3d = (lm.x * img_w, lm.y * img_h, lm.z * 8000)

                            x, y = int(lm.x * img_w), int(lm.y * img_h)

                            # Get the 2D Coordinates
                            face_2d.append([x, y])

                            # Get the 3D Coordinates
                            face_3d.append([x, y, lm.z])

                            # Convert it to the NumPy array
                    face_2d = np.array(face_2d, dtype=np.float64)

                    # Convert it to the NumPy array
                    face_3d = np.array(face_3d, dtype=np.float64)

                    # The camera matrix
                    focal_length = 1 * img_w

                    cam_matrix = np.array([[focal_length, 0, img_h / 2],
                                           [0, focal_length, img_w / 2],
                                           [0, 0, 1]])

                    # The Distance Matrix
                    dist_matrix = np.zeros((4, 1), dtype=np.float64)

                    # Solve PnP
                    success, rot_vec, trans_vec = cv2.solvePnP(face_3d, face_2d, cam_matrix, dist_matrix)

                    # Get rotational matrix
                    rmat, jac = cv2.Rodrigues(rot_vec)

                    # Get angles
                    angles, mtxR, mtxQ, Qx, Qy, Qz = cv2.RQDecomp3x3(rmat)

                    # Get the y rotation degree
                    x = angles[0] * 360
                    y = angles[1] * 360

                    # print(y)

                    # See where the user's head tilting
                    if y < -10:
                        text = "Looking Left"
                    elif y > 10:
                        text = "Looking Right"
                    elif x < -10:
                        text = "Looking Down"
                    else:
                        text = "Forward"
                    text = str(int(x)) + "::" + str(int(y)) + text
                    print(text)
                    print(text)
                    print(text)
                    print(text)
                    print ("========================================")
                    print ("========================================")
                    print ("========================================")
                    print ("========================================")
                    # print(str(int(x)) + "::" + str(int(y)))
                    # print("x: {x}   |   y: {y}  |   sound amplitude: {amp}".format(x=int(x), y=int(y), amp=audio.SOUND_AMPLITUDE))

                    # Y is left / right
                    # X is up / down
                    if y < -10 or y > 10:
                        X_AXIS_CHEAT = 1
                        ob = report_exam()
                        ob.STUDENT = students_table.objects.get(LOGIN__id=studentid)
                        ob.EXAMID = exam_table.objects.get(id=examid)
                        ob.type = 'X_AXIS_CHEAT'
                        ob.save()
                    else:
                        X_AXIS_CHEAT = 0

                    if x < -5:
                        Y_AXIS_CHEAT = 1
                        ob = report_exam()
                        ob.STUDENT = students_table.objects.get(LOGIN__id=studentid)
                        ob.EXAMID = exam_table.objects.get(id=examid)
                        ob.type = 'Y_AXIS_CHEAT'
                        ob.save()
                    else:
                        Y_AXIS_CHEAT = 0
            PERCENTAGE_CHEAT=(avg(X_AXIS_CHEAT,px)+avg(Y_AXIS_CHEAT,py))/2
            print (PERCENTAGE_CHEAT)
            px=X_AXIS_CHEAT
            py=Y_AXIS_CHEAT
            if PERCENTAGE_CHEAT>=0.5:
                fn=datetime.now().strftime("%Y%m%d%H%M%S")+".png"
                cv2.imwrite(r"D:\sub_eval\sub_eval\media/"+fn,frame)
                ob=report_examimage()
                ob.STUDENT = students_table.objects.get(LOGIN__id=studentid)
                ob.EXAMID = exam_table.objects.get(id=examid)
                ob.image = fn
                ob.save()

        except:
            PERCENTAGE_CHEAT=0.01
        YDATA.pop(0)
        YDATA.append(PERCENTAGE_CHEAT)
        # line.set_xdata(XDATA)
        # line.set_ydata(YDATA)
        # plt.draw()
        # plt.pause(1e-17)


                            # Break the loop when 'q' is pressed
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break
    #
    # # Release resources
    # cap.release()
    # cv2.destroyAllWindows()


import sounddevice as sd
import numpy as np



# place holders and global variables
SOUND_AMPLITUDE = 0
AUDIO_CHEAT = 0

# sound variables
# SUS means next sound packet is worth analyzing
CALLBACKS_PER_SECOND = 38               # callbacks per sec(system dependent)
SUS_FINDING_FREQUENCY = 2               # calculates SUS *n* times every sec
SOUND_AMPLITUDE_THRESHOLD = 20          # amplitude considered for SUS calc

# packing *n* frames to calculate SUS
FRAMES_COUNT = int(CALLBACKS_PER_SECOND/SUS_FINDING_FREQUENCY)
AMPLITUDE_LIST = list([0]*FRAMES_COUNT)
SUS_COUNT = 0
count = 0

def print_sound(indata, outdata, frames, time, status):
    avg_amp = 0
    global SOUND_AMPLITUDE, SUS_COUNT, count, SOUND_AMPLITUDE_THRESHOLD, AUDIO_CHEAT
    vnorm = int(np.linalg.norm(indata)*10)
    AMPLITUDE_LIST.append(vnorm)
    count += 1
    AMPLITUDE_LIST.pop(0)
    if count == FRAMES_COUNT:
        avg_amp = sum(AMPLITUDE_LIST)/FRAMES_COUNT
        SOUND_AMPLITUDE = avg_amp
        if SUS_COUNT >= 2:
            #print("!!!!!!!!!!!! FBI OPEN UP !!!!!!!!!!!!")
            AUDIO_CHEAT = 1
            SUS_COUNT = 0
        if avg_amp > SOUND_AMPLITUDE_THRESHOLD:
            SUS_COUNT += 1
            #print("Sus...", SUS_COUNT)
        else:
            SUS_COUNT = 0
            AUDIO_CHEAT = 0
        count = 0

def sound():
    with sd.Stream(callback=print_sound):
        sd.sleep(-1)

def sound_analysis():
    global examid
    global studentid
    global AMPLITUDE_LIST, FRAMES_COUNT, SOUND_AMPLITUDE
    while True:
        AMPLITUDE_LIST.append(SOUND_AMPLITUDE)
        AMPLITUDE_LIST.pop(0)

        avg_amp = sum(AMPLITUDE_LIST)/FRAMES_COUNT

        if avg_amp > 10:

            ob = report_exam()
            ob.STUDENT = students_table.objects.get(LOGIN__id=studentid)
            ob.EXAMID = exam_table.objects.get(id=examid)
            ob.type = 'Audio'
            ob.save()
            print("Sus...")
