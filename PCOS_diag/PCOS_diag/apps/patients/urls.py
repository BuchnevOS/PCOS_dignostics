from django.urls import path

from . import views

app_name = 'patients'

urlpatterns = [
	path('', views.index, name='index'),
	path('selfdiagnostics', views.selfdiagnostics, name='selfdiagnostics'),
	path('contacts', views.contacts, name='contacts'),
	
	path('patients_list', views.patients_list, name='patients_list'),
	path('visits_list', views.visits_list, name='visits_list'),
	path('ultrasounds_list', views.ultrasounds_list, name='ultrasounds_list'),
	path('appointments_list', views.appointments_list, name='appointments_list'),
	path('laboratory_results_list', views.laboratory_results_list, name='laboratory_results_list'),
	
	path('add_patient', views.add_patient, name='add_patient'),
	path('update_patient/<str:pk>', views.update_patient, name='update_patient'),

	path('add_visit', views.add_visit, name='add_visit'),
	path('update_visit/<str:pk>', views.update_visit, name='update_visit'),

	path('add_appointment', views.add_appointment, name='add_appointment'),
	path('update_appointment/<str:pk>', views.update_appointment, name='update_appointment'),

	path('add_ultrasound', views.add_ultrasound, name='add_ultrasound'),
	path('update_ultrasound/<str:pk>', views.update_ultrasound, name='update_ultrasound'),

	path('add_laboratory', views.add_laboratory, name='add_laboratory'),
	path('update_laboratory/<str:pk>', views.update_laboratory, name='update_laboratory'),
	
	path('add_visit_full/<str:participant_key>', views.add_visit_full, name='add_visit_full'),
	path('update_visit_full/<str:pk>/<str:participant_key>', views.update_visit_full, name='update_visit_full'),

	path('add_appointment_full/<str:participant_key>', views.add_appointment_full, name='add_appointment_full'),
	path('update_appointment_full/<str:pk>/<str:participant_key>', views.update_appointment_full, name='update_appointment_full'),

	path('add_ultrasound_full/<str:participant_key>', views.add_ultrasound_full, name='add_ultrasound_full'),
	path('update_ultrasound_full/<str:pk>/<str:participant_key>', views.update_ultrasound_full, name='update_ultrasound_full'),

	path('add_laboratory_full/<str:participant_key>', views.add_laboratory_full, name='add_laboratory_full'),
	path('update_laboratory_full/<str:pk>/<str:participant_key>', views.update_laboratory_full, name='update_laboratory_full'),

	path('view_full/<str:pk>', views.view_full, name='view_full'),

	path('login_user', views.login_user, name='login_user'),

	path('logout_user', views.logout_user, name='logout_user'),

	path('execute_query', views.execute_query, name='execute_query'),

	
	

]