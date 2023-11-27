
from django.urls import path
from . import views as portals_views

urlpatterns = [
    path('login/', portals_views.dashboard, name='dashboard'),
    path('', portals_views.login_user, name='login_user-url'),
    path('logout/', portals_views.logout_user, name='logout_user-url'),
    path('signup/', portals_views.register_user, name='register_user-url'),
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
    # path('exams/', portals_views.exam, name='exams'),
    path('delete/exam/<int:exam_id>', portals_views.delete_test, name='delete-exam-url'),
    path('delete/test/<int:test_id>', portals_views.delete_test, name='delete-test-url'),
    path('book_test/', portals_views.book_test, name='book-test-url'),
    path('admissions/', portals_views.result, name='admissions'),
    path('faqs/', portals_views.faqs, name='faqs'),
    path('edit/', portals_views.edit_profile, name='profile-edit'),
    path('bookings/', portals_views.test, name='test-booking'),
]
