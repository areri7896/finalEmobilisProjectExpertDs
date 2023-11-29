
from django.urls import path
from . import views as portals_views

urlpatterns = [
    path('home/', portals_views.dashboard, name='dashboard'),
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
    path('delete_exam/<int:pk>', portals_views.delete_exam, name='delete_exam'),
    path('delete_test/<int:id>', portals_views.delete_test, name='delete-test-url'),
    path('book_test/', portals_views.book_test, name='book-test-url'),
    path('admissions/', portals_views.result, name='admissions'),
    path('faqs/', portals_views.faqs, name='faqs'),
    path('examupdate/<int:pk>', portals_views.exam_update, name='exam_update'),
    path('edittest/<int:pk>', portals_views.edit_test, name='test-update'),
    path('exam_booking_records/', portals_views.exam_record, name='exam-booking-url'),
    path('test_booking_records/', portals_views.test_record, name='test-booking-url'),
    # path('bookings/', portals_views.test, name='test-booking'),
    path('statement_pdf/', portals_views.statement_pdf, name='statement-pdf'),
]
