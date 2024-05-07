from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from .forms import StudentInfoForm
from .models import Student_info

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse

# from paginate import Paginator, EmptyPage


# Create your views here.


# this function add data in database and show all student data
# START INSERT DATA code
def add_student(request):
    if request.method == "POST":
        fm = StudentInfoForm(request.POST, request.FILES)
        # print(fm)
        if fm.is_valid():
            username = fm.cleaned_data["username"]
            # print(username)
            email = fm.cleaned_data["email"]
            raw_password = fm.cleaned_data["password"]
            image = fm.cleaned_data["image"]
            reg = Student_info(username=username, email=email, image=image)
            reg.set_password(raw_password)
            reg.save()
            fm = StudentInfoForm()
    else:
        fm = StudentInfoForm()
    # stud = Student_info.objects.all()
    return render(request, "addStudentData.html", {"form": fm})


# END INSERT DATA code

# this function delete data in database and form both
# START delete code


def delete_data(request, id):
    if request.method == "POST":
        pi = Student_info.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/")


# this code gives in chat GPT
# def delete_data(request, id):
#     if request.method == "POST":
#         # Get the specific instance using get_object_or_404
#         pi = get_object_or_404(Student_info, pk=id)
#         # Call delete() on the fetched instance
#         pi.delete()
#         # Redirect to the desired URL after deletion
#         return HttpResponseRedirect("/")

# END delete code

# this function update/edit data in database and form both
# START UPDATE AND EDIT DATA code


def update_data(request, id):
    if request.method == "GET":
        pi = Student_info.objects.get(pk=id)
        fm = StudentInfoForm(instance=pi)
        return render(request, "updateData.html", {"form": fm})

    elif request.method == "POST":
        pi = Student_info.objects.get(pk=id)
        # fm = StudentInfoForm(initial=pi, request.FILES, request.POST)
        fm = StudentInfoForm(request.POST, request.FILES, instance=pi)
        if fm.is_valid():
            username = fm.cleaned_data["username"]
            email = fm.cleaned_data["email"]
            raw_password = fm.cleaned_data["password"]
            image = fm.cleaned_data["image"]

            pi.username = username
            pi.email = email
            pi.set_password(raw_password)
            pi.image = image
            pi.save()
            return HttpResponseRedirect(
                reverse("showStudentData")
            )  # Redirect to showStudentData URL
            # return HttpResponseRedirect("/")
            # return render(request, "showStudentData")


# END UPDATE AND EDIT DATA code


# START SHOW STUDET DATA code


# def showStudentData(request):
#     stud = Student_info.objects.all()
#     return render(request, "showStudentData.html", {"stu": stud})


# Function to paginate data
def paginate_data(request, queryset, page_number=1, per_page=5):
    paginator = Paginator(queryset, per_page)
    try:
        page = paginator.page(page_number)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page


# View to display student data with pagination
def showStudentData(request):
    # Retrieve all student data
    all_students = Student_info.objects.all()

    # Get the requested page number from the URL query parameter
    page_number = request.GET.get("page", 1)

    # Paginate the student data
    paginated_data = paginate_data(request, all_students, page_number)

    # Render the template with paginated data
    return render(request, "showStudentData.html", {"data": paginated_data})


# END SHOW STUDET DATA code
