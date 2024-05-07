from . import views
from django.urls import path

urlpatterns = [
    path("", views.add_student, name="add_student"),
    path("showStudentData/", views.showStudentData, name="showStudentData"),
    path("delete/<int:id>", views.delete_data, name="deletedata"),
    path("update/<int:id>", views.update_data, name="update_data"),
]
