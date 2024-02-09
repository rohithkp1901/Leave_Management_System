from django.shortcuts import render,redirect,get_object_or_404
from .models import Student,LeaveRequest,Teacher
from django.contrib.auth import logout
from django.contrib import messages
from .forms import AddForm,TeacherReg,TeacherLoginForm
# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def s_insert(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        department=request.POST.get('department')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        gender=request.POST.get('gender')
        image=request.POST.get('image')
        Student(name=name,department=department,username=username,email=email,password=password,gender=gender,image=image).save()
    return render(request,'s_register.html')

def s_login(request):
    return render(request,'s_login.html')

def s_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user =Student.objects.filter(username=username, password=password)

        if user:
            user_details=Student.objects.get(username=username)

            name=user_details.name
            username=user_details.username
            email=user_details.email
            department=user_details.department

            request.session['name']=name
            request.session['username']=username
            request.session['email']=email
            request.session['department']=department
            return redirect('view_student_details')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')

    return render(request, 's_login.html')

def s_logout_view(request):
    logout(request)
    return redirect('s_login_view')

def view_student_details(request):
    username=request.session.get('username')
    student = Student.objects.get(username=username)
    return render(request, 'view_student_details.html', {'student': student})

def s_edit_profile(request,username):
    s=Student.objects.get(username=username)
    f=AddForm(instance=s)
    if request.method == 'POST':
        f=AddForm(request.POST,request.FILES,instance=s)
        if f.is_valid(): 
            f.save()
            return redirect('view_student_details')
    return render(request,'s_edit_profile.html',{'f':f})


def add_leave_request(request):
    if request.method == 'POST':

        student = Student.objects.get(username=request.session['username'])
        reason = request.POST.get('reason', '')

        if not reason:
            messages.error(request, 'Please provide a reason for leave request.')
        else:
            LeaveRequest.objects.create(student=student, reason=reason)
            messages.success(request, 'Leave request added successfully.')
            return redirect('view_leave_requests')

    return render(request, 'add_leave_request.html')

def view_leave_requests(request):
    leave_requests = LeaveRequest.objects.filter(student__username=request.session['username'])
    return render(request, 'view_leave_requests.html', {'leave_requests': leave_requests})

def register_teacher(request):
    if request.method == 'POST':
        form = TeacherReg(request.POST)
        if form.is_valid():
            teacher = form.save(commit=False)

            teacher.is_approved = False
            teacher.save()

            return redirect('not_approved')
    else:
        form = TeacherReg()

    return render(request, 't_register.html', {'form': form})
def t_login(request):
    return render(request,'t_login.html')
def login_teacher(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        teacher = Teacher.objects.get(username=username, password=password)

        if teacher is not None:
            request.session['teacher_username'] = teacher.username

            if teacher.is_approved:
                return redirect('t_dashboard')  
            else:
                return render(request, 'not_approved.html')
        else:
            return render(request, 't_login.html', {'error': 'Invalid login credentials'})

    return render(request, 't_login.html')

def t_dashboard(request):
    username = request.session.get('teacher_username')

    if not username:
        messages.error(request, 'Teacher not found.')
        return redirect('t_login')
    teacher = Teacher.objects.get(username=username)
    return render(request, 't_dashboard.html', {'teacher': teacher})
    
def not_approved(request):
    return render(request, 'not_approved.html')

def view_students(request):
    teacher_username = request.session.get('teacher_username')

    if teacher_username:
        
        teacher = Teacher.objects.get(username=teacher_username)

        students = Student.objects.filter(department=teacher.department)
        leave_requests = LeaveRequest.objects.filter(student__department=teacher.department, status='Pending')

        return render(request, 'view_students.html', {'students': students, 'teacher': teacher, 'leave_requests': leave_requests})

    else:
        return redirect('t_login')
    
def logout_user(request):
    logout(request)
    return redirect('t_login')

def approve_leave(request, student_username):
    student = get_object_or_404(Student, username=student_username)
    leave_request = LeaveRequest.objects.filter(student=student, status='Pending').first()

    if leave_request:
        leave_request.status = 'Approved'
        leave_request.save()

    return redirect('view_students')

def pending_requests(request):
    username = request.session.get('teacher_username')

    if not username:
        messages.error(request, 'Teacher not found.')
        return redirect('t_login')

    teacher = Teacher.objects.get(username=username)

    pending_requests = LeaveRequest.objects.filter(student__department=teacher.department, status='Pending')

    return render(request, 'pending_requests.html', {'teacher': teacher, 'pending_requests': pending_requests})

def view_student_request(request, student_username):
    teacher_username = request.session.get('teacher_username')

    if teacher_username:
        teacher = Teacher.objects.get(username=teacher_username)
        student = get_object_or_404(Student, username=student_username)
        leave_requests = LeaveRequest.objects.filter(student=student)

        if request.method == 'POST':
            leave_request_id = request.POST.get('leave_request_id')
            leave_request = get_object_or_404(LeaveRequest, id=leave_request_id)
            leave_request.approved = True
            leave_request.save()

        return render(request, 'view_students2.html', {'teacher': teacher, 'student': student, 'leave_requests': leave_requests})
