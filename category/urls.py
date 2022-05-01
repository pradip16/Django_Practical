from django.urls import path
from category import views 

urlpatterns = [
    path("",views.ListCategoryAPIView.as_view(),name="Category_list"),
    path("create/", views.CreateCategoryAPIView.as_view(),name="Category_create"),
    path("update/<int:pk>/",views.UpdateCategoryAPIView.as_view(),name="update_Category"),
    path("delete/<int:pk>/",views.DeleteCategoryAPIView.as_view(),name="delete_Category")
]

