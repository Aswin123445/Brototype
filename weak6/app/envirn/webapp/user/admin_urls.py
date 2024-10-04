from django.urls import path
from django.conf.urls import handler404
from user import views
handler404='user.views.custom_404'
urlpatterns=[
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_home/',views.admin_home,name="admin_home"),
    path('admin_user_details/<int:user_id>/',views.admin_user_details,name="admin_user_details"),
    path('admin_user_delete/<int:user_id>/',views.admin_user_delete,name="admin_user_delete"),
    path('update_user/<int:user_id>/',views.update_user,name="update_user"),
    path('update_email/<int:user_id>/',views.update_email,name="update_email"),
    path('create_user_from_admin',views.create_user_from_admin,name="create_user_from_admin"),
    path('adminlogout/',views.admin_logout,name='adminlogout')




]
