
from django.urls import path
from . import views as portals_views

urlpatterns = [
    path('', portals_views.dashboard, name='dashboard'),
    path('login/', portals_views.login, name='login'),
    path('<int:year>/<str:month>/', portals_views.dashboard, name='calender'),
    path('messaging/', portals_views.messaging, name='messaging'),
    path('receipt/', portals_views.receipt, name='receipt'),
    path('payment/', portals_views.payment, name='payment'),
    path('statement/', portals_views.statement, name='statement'),
    path('maps/', portals_views.maps, name='maps'),
    path('settings/', portals_views.settings, name='settings'),
    path('profile/', portals_views.profile, name='profile'),
    path('academics/', portals_views.academics, name='academics'),
    path('book_exam/', portals_views.book_exam, name='book-exam-url'),
    path('exams/', portals_views.exam, name='exams'),
    path('deleteexam/<id>', portals_views.delete_exam, name='delete-exam-url'),
    path('deletettest/<id>', portals_views.delete_test, name='delete-test-url'),
    path('book_test/', portals_views.book_test, name='book-test-url'),
    path('admissions/', portals_views.result, name='admissions'),
    path('faqs/', portals_views.faqs, name='faqs'),
    path('edit/', portals_views.edit_profile, name='profile-edit'),
    path('bookings/', portals_views.test, name='test-booking'),
]
