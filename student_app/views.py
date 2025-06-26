from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course
from .forms import StudentForm

def student_list(request):
    course_id = request.GET.get('course')
    courses = Course.objects.all()

    if course_id:
        students = Student.objects.filter(course__id=course_id)
    else:
        students = Student.objects.all()

    return render(request, 'student_app/student_list.html', {
        'students': students,
        'courses': courses,
        'selected_course': int(course_id) if course_id else None
    })

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_app/add_student.html', {'form': form})

def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_app/edit_student.html', {'form': form, 'student': student})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_app/delete_student.html', {'student': student})
