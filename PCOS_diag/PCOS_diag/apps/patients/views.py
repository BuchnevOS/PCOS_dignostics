from django.shortcuts import render, redirect
from .models import Patient, Doctor, Ethnicity, Visit, Appointment, Ultrasound, Laboratory_test
from .forms import PatientForm, VisitForm, UltrasoundForm, LaboratoryForm, FullForm, AppointmentForm
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse


def index(request):
	if request.user.is_authenticated:
		logout(request)
	return render(request, 'starts/index.html')

def selfdiagnostics(request):
	if request.user.is_authenticated:
		logout(request)
	return render(request,'starts/selfdiagnostics.html')

def contacts(request):
	if request.user.is_authenticated:
		logout(request)
	return render(request,'starts/contacts.html')




@login_required(login_url='/login_user')
def patients_list(request):
	try:
		patients_ = Patient.objects.order_by('id')
	except:
		raise Http404("Пациенты не найдены!")
	return render(request, 'patients/patients_list.html',{'patients_':patients_})

@login_required(login_url='/login_user')
def visits_list(request):
	try:
		visits_ = Visit.objects.order_by('date')
	except:
		raise Http404("Визиты!")
	return render(request, 'patients/visits_list.html',{'visits_':visits_})

@login_required(login_url='/login_user')
def ultrasounds_list(request):
	try:
		ultrasounds_ = Ultrasound.objects.order_by('date')
	except:
		raise Http404("Исследования УЗИ не найдены!")
	return render(request, 'patients/ultrasounds_list.html',{'ultrasounds_':ultrasounds_})

@login_required(login_url='/login_user')
def appointments_list(request):
	try:
		appointments_ = Appointment.objects.order_by('date')
	except:
		raise Http404("Приемы не найдены!")
	return render(request, 'patients/appointments_list.html',{'appointments_':appointments_})

@login_required(login_url='/login_user')
def laboratory_results_list(request):
	try:
		laboratory_results_list_ = Laboratory_test.objects.order_by('date')
	except:
		raise Http404("Результаты анализов не найдены!")
	return render(request, 'patients/laboratory_results_list.html',{'laboratory_results_list_':laboratory_results_list_})

@login_required(login_url='/login_user')
def add_patient(request):
	form=PatientForm()
	if request.method=='POST':
		form=PatientForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/patients_list')
	context = {'form':form, 'new':1}
	return render(request, 'forms/patient_form.html',context)


@login_required(login_url='/login_user')
def update_patient(request, pk):
	patient=Patient.objects.get(id=pk)
	form= PatientForm(instance=patient)
	if request.method=='POST':
		form=PatientForm(request.POST, instance=patient)
		if form.is_valid():
			form.save()
			return redirect('/patients_list')
	context = {'form':form, 'new':''}
	return render(request, 'forms/patient_form.html', context)


@login_required(login_url='/login_user')
def add_visit(request):
	form=VisitForm()
	if request.method=='POST':
		form=VisitForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/visits_list')
	context = {'form':form, 'new':1}
	return render(request, 'forms/visit_form.html',context)

@login_required(login_url='/login_user')
def update_visit(request, pk):
	visit=Visit.objects.get(id=pk)
	form= VisitForm(instance=visit)
	if request.method=='POST':
		form=VisitForm(request.POST, instance=visit)
		if form.is_valid():
			form.save()
			return redirect('/visits_list')
	context = {'form':form, 'new':''}
	return render(request, 'forms/visit_form.html', context)


@login_required(login_url='/login_user')
def add_appointment(request):
	form=AppointmentForm()
	if request.method=='POST':
		form=AppointmentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/appointments_list')
	context = {'form':form, 'new':1}
	return render(request, 'forms/appointment_form.html',context)

@login_required(login_url='/login_user')
def update_appointment(request, pk):
	appointment=Appointment.objects.get(id=pk)
	form= AppointmentForm(instance=appointment)
	if request.method=='POST':
		form=AppointmentForm(request.POST, instance=appointment)
		if form.is_valid():
			form.save()
			return redirect('/appointments_list')
	context = {'form':form, 'new':''}
	return render(request, 'forms/appointment_form.html', context)

@login_required(login_url='/login_user')
def add_ultrasound(request):
	form=UltrasoundForm()
	if request.method=='POST':
		form=UltrasoundForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/ultrasounds_list')
	context = {'form':form, 'new':1}
	return render(request, 'forms/ultrasound_form.html',context)

@login_required(login_url='/login_user')
def update_ultrasound(request, pk):
	ultrasound=Ultrasound.objects.get(id=pk)
	form= UltrasoundForm(instance=ultrasound)
	if request.method=='POST':
		form=UltrasoundForm(request.POST, instance=ultrasound)
		if form.is_valid():
			form.save()
			return redirect('/ultrasounds_list')
	context = {'form':form, 'new':''}
	return render(request, 'forms/ultrasound_form.html', context)

@login_required(login_url='/login_user')
def add_laboratory(request):
	form=LaboratoryForm()
	if request.method=='POST':
		form=LaboratoryForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/laboratory_results_list')
	context = {'form':form, 'new':1}
	return render(request, 'forms/laboratory_form.html',context)

@login_required(login_url='/login_user')
def update_laboratory(request, pk):
	laboratory=Laboratory_test.objects.get(id=pk)
	form= LaboratoryForm(instance=laboratory)
	if request.method=='POST':
		form=LaboratoryForm(request.POST, instance=laboratory)
		if form.is_valid():
			form.save()
			return redirect('/laboratory_results_list')
	context = {'form':form, 'new':''}
	return render(request, 'forms/laboratory_form.html', context)

@login_required(login_url='/login_user')
def view_full(request, pk):
	patient=Patient.objects.get(id=pk)
	visits_ = Visit.objects.filter(patient_key=pk)
	appointments_ = Appointment.objects.filter(patient_key=pk)
	ultrasounds_ = Ultrasound.objects.filter(patient_key=pk)
	laboratory_results_list_=Laboratory_test.objects.filter(patient_key=pk)
	form= PatientForm(instance=patient)
	if request.method=='POST':
		form=PatientForm(request.POST, instance=patient)
		if form.is_valid():
			form.save()
			return redirect('/patients_list')
	context = {'form':form,'visits_': visits_, 'appointments_':appointments_,
		'ultrasounds_':ultrasounds_,'laboratory_results_list_':laboratory_results_list_}
	return render(request, 'forms/patient_form_full.html', context)


@login_required(login_url='/login_user')
def add_visit_full(request, participant_key):
	form=VisitForm()
	form.fields['patient_key'].initial = participant_key
	if request.method=='POST':
		form=VisitForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/view_full/'+participant_key)
	context = {'form':form, 'new':1, 'patient_key':participant_key}
	return render(request, 'forms/visit_form_full.html',context)

@login_required(login_url='/login_user')
def update_visit_full(request, pk, participant_key):
	visit=Visit.objects.get(id=pk)
	form= VisitForm(instance=visit)
	if request.method=='POST':
		form=VisitForm(request.POST, instance=visit)
		if form.is_valid():
			form.save()
			return redirect('/view_full/'+participant_key)
	context = {'form':form, 'new':'', 'patient_key':participant_key}
	return render(request, 'forms/visit_form_full.html',context)

@login_required(login_url='/login_user')
def add_appointment_full(request, participant_key):
	form=AppointmentForm()
	form.fields['patient_key'].initial = participant_key
	form.fields['visit_key'].queryset = Visit.objects.filter(patient_key=participant_key)
	if request.method=='POST':
		form=AppointmentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/view_full/'+participant_key)
	context = {'form':form, 'new':1, 'patient_key':participant_key}
	return render(request, 'forms/appointment_form_full.html',context)

@login_required(login_url='/login_user')
def update_appointment_full(request, pk, participant_key):
	appointment=Appointment.objects.get(id=pk)
	form= AppointmentForm(instance=appointment)
	form.fields['visit_key'].queryset = Visit.objects.filter(patient_key=participant_key)
	if request.method=='POST':
		form=AppointmentForm(request.POST, instance=appointment)
		if form.is_valid():
			form.save()
			return redirect('/view_full/'+participant_key)
	context = {'form':form, 'new':'', 'patient_key':participant_key}
	return render(request, 'forms/appointment_form_full.html',context)

@login_required(login_url='/login_user')
def add_ultrasound_full(request, participant_key):
	form=UltrasoundForm()
	form.fields['patient_key'].initial = participant_key
	form.fields['visit_key'].queryset = Visit.objects.filter(patient_key=participant_key)
	if request.method=='POST':
		form=UltrasoundForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/view_full/'+participant_key)
	context = {'form':form, 'new':1, 'patient_key':participant_key}
	return render(request, 'forms/ultrasound_form_full.html',context)

@login_required(login_url='/login_user')
def update_ultrasound_full(request, pk, participant_key):
	ultrasound=Ultrasound.objects.get(id=pk)
	form= UltrasoundForm(instance=ultrasound)
	form.fields['visit_key'].queryset = Visit.objects.filter(patient_key=participant_key)
	if request.method=='POST':
		form=UltrasoundForm(request.POST, instance=ultrasound)
		if form.is_valid():
			form.save()
			return redirect('/view_full/'+participant_key)
	context = {'form':form, 'new':'', 'patient_key':participant_key}
	return render(request, 'forms/ultrasound_form_full.html',context)

@login_required(login_url='/login_user')
def add_laboratory_full(request, participant_key):
	form=LaboratoryForm()
	form.fields['patient_key'].initial = participant_key
	form.fields['visit_key'].queryset = Visit.objects.filter(patient_key=participant_key)
	if request.method=='POST':
		form=LaboratoryForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/view_full/'+participant_key)
	context = {'form':form, 'new':1, 'patient_key':participant_key}
	return render(request, 'forms/laboratory_form_full.html',context)

@login_required(login_url='/login_user')
def update_laboratory_full(request, pk, participant_key):
	laboratory=Laboratory_test.objects.get(id=pk)
	form= LaboratoryForm(instance=laboratory)
	form.fields['visit_key'].queryset = Visit.objects.filter(patient_key=participant_key)
	if request.method=='POST':
		form=LaboratoryForm(request.POST, instance=laboratory)
		if form.is_valid():
			form.save()
			return redirect('/view_full/'+participant_key)
	context = {'form':form, 'new':'', 'patient_key':participant_key}
	return render(request, 'forms/laboratory_form_full.html',context)


def login_user(request):
	if request.user.is_authenticated:
		logout(request)
	username=request.POST.get('username')
	password=request.POST.get('password')
	user=authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		return redirect('/patients_list')
	return render(request, 'starts/datawork.html')


def logout_user(request):
	logout(request)
	return redirect('/login_user')

def execute_query(request):
	if request.method == 'GET':
		patient_key 		= request.GET.get('patient_key')
		visit_key 	= request.GET.get('visit_key')
		patient =Patient.objects.get(id=patient_key)
		visit	=Visit.objects.get(id=visit_key)
		appointments 	= Appointment.objects.filter(patient_key=patient_key, visit_key=visit_key)
		if not appointments:
			periods=None
			type_menstrual_disorders_1=None
			type_menstrual_disorders_2=None
			type_menstrual_disorders_3=None
			type_menstrual_disorders_4=None
			min_menstrual				=None
			max_menstrual				=None
			sum_physician				=None
		else:
			last_appointment=appointments.latest('date')
			periods					=last_appointment.periods
			type_menstrual_disorders_1=last_appointment.type_menstual_disorders_1
			type_menstrual_disorders_2=last_appointment.type_menstual_disorders_2
			type_menstrual_disorders_3=last_appointment.type_menstual_disorders_3
			type_menstrual_disorders_4=last_appointment.type_menstual_disorders_4
			min_menstrual				=last_appointment.min_menstrual
			max_menstrual				=last_appointment.max_menstrual
			sum_physician				=last_appointment.sum_physician

		
		ultrasounds 	= Ultrasound.objects.filter(patient_key=patient_key, visit_key=visit_key)
		if not ultrasounds:
			right_ovary_volume	=None
			right_ovary_follicle=None
			diameter_cyst_right	=None
			left_ovary_volume	=None
			left_ovary_follicle	=None
			diameter_cyst_left	=None
		else:
			last_ultrasound	=ultrasounds.latest('date')
			right_ovary_volume	=last_ultrasound.right_ovary_volume
			right_ovary_follicle=last_ultrasound.right_ovary_follicle
			diameter_cyst_right	=last_ultrasound.diameter_cyst_right
			left_ovary_volume	=last_ultrasound.left_ovary_volume
			left_ovary_follicle	=last_ultrasound.left_ovary_follicle
			diameter_cyst_left	=last_ultrasound.diameter_cyst_left



		laboratory_tests= Laboratory_test.objects.filter(patient_key=patient_key, visit_key=visit_key)
		if not laboratory_tests:
			value_testosteron	=None
			value_shbg 			=None
			value_dheas			=None
			value_tsh			=None
			day_mens_prl		=None
			value_17ph			=None
			value_prl 			=None
		else:
			last_laboratory_test	=laboratory_tests.latest('date')
			value_testosteron	=last_laboratory_test.value_testosteron
			value_shbg 			=last_laboratory_test.value_shbg
			value_dheas			=last_laboratory_test.value_dheas
			value_tsh			=last_laboratory_test.value_tsh
			day_mens_prl		=last_laboratory_test.day_mens_prl
			value_17ph			=last_laboratory_test.value_17hp
			value_prl 			=last_laboratory_test.value_prl
		
		return JsonResponse({
			"ethnicity"					:patient.ethnicity_key.id,
			"periods"					:periods,
			"type_menstrual_disorders___1":type_menstrual_disorders_1,
			"type_menstrual_disorders___2":type_menstrual_disorders_2,
			"type_menstrual_disorders___3":type_menstrual_disorders_3,
			"type_menstrual_disorders___4":type_menstrual_disorders_4,
			"min_menstrual"				:min_menstrual,
			"max_menstrual"				:max_menstrual,
			"sum_physician"				:sum_physician,

		
			"right_ovary_volume"		:right_ovary_volume,
			"right_ovary_follicle"		:right_ovary_follicle,
			"diameter_cyst_right_ovary"	:diameter_cyst_right,
			"left_ovary_volume"			:left_ovary_volume,
			"left_ovary_follicle"		:left_ovary_follicle,
			"diameter_cyst_left"		:diameter_cyst_left,
			
			
			"value_testosteron"			:value_testosteron,
			"value_shbg"				:value_shbg,
			"value_dheas"				:value_dheas,
			"value_tsh"					:value_tsh,
			"day_mens_prl"				:day_mens_prl,
			"value_17hp"				:value_17ph,
			"value_prl"					:value_prl,

		
			"age_visit1"				:visit.age_visit,
			"inform_consent"			:visit.inform_consent,
			"comply_all_study"			:visit.comply_all_study,
			"female_age"				:visit.female_age,
			"current_preg_lact"			:visit.current_preg_lact, 
			"history_hysterectomy"		:visit.history_hysterectomy,
			"risk_no_compliance"		:visit.risk_no_compliance,
			"unwillingness"				:visit.unwillingness,
			"medicince_listed_now___10"	 	:visit.medicince_listed_now_10,
			"medicince_listed_3month___10"	:visit.medicince_listed_3month_10,

		})


