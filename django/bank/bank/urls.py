"""bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from customer.views import first_django_customer_page
from employee.views import delete_emp,edit_emp,show,persist_or_update_emp
urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/',first_django_customer_page),

    path('emp/',show),
    path('create/',persist_or_update_emp),
    path('edit/<int:id>',edit_emp),
    path('delete/<int:id>',delete_emp),

]
