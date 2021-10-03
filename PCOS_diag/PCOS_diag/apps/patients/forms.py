from django.forms import ModelForm,  CharField, PasswordInput, TextInput, DateInput, Textarea, ModelChoiceField,  RadioSelect, IntegerField, FloatField, ValidationError
from .models import Patient, Ethnicity,Visit, Appointment, Doctor, Ultrasound, Laboratory_test
from django.contrib.auth.models import User

class PatientForm(ModelForm):
	class Meta:
		model = Patient
		fields=['name_patient','day_of_birth','ethnicity_key']
		ethnicity_key=ModelChoiceField(
				queryset=Ethnicity.objects.all(), 
				empty_label=None)
		
		included=RadioSelect()
		widgets={
			"name_patient":TextInput(attrs={
				'class':'form-control',
				'placeholder':'ФИО пациента'
				}),
			"day_of_birth":DateInput(format=('%Y-%m-%d'), attrs={
				'class':'form-control',
				'placeholder':'Дата рождения',
				'input_type' : 'text',
				'type': 'date'
				}),               
		};
class VisitForm(ModelForm):
	class Meta:
		model=Visit
		fields=['name_visit','patient_key', 'doctor_key','date','age_visit', 'inform_consent', 'comply_all_study', 'female_age',
		'current_preg_lact', 'history_hysterectomy', 'risk_no_compliance', 'unwillingness', 'medicince_listed_now_10',
		'medicince_listed_3month_10','PCOS','Exclusion','Grey', 'Phenotype', 'PCOS_text', 'Exclusion_text']

		patient_key=ModelChoiceField(
				queryset=Patient.objects.all(), 
				empty_label=None)
		doctor_key=ModelChoiceField(
				queryset=Doctor.objects.all(), 
				empty_label=None)
		age_visit						: IntegerField()
		inform_consent					= RadioSelect()
		comply_all_study				= RadioSelect()
		female_age						= RadioSelect()
		current_preg_lact				= RadioSelect()
		history_hysterectomy			= RadioSelect()
		risk_no_compliance				= RadioSelect()
		unwillingness					= RadioSelect()
		medicince_listed_now_10			= RadioSelect()
		medicince_listed_3month_10		= RadioSelect()
		PCOS 		=	IntegerField()
		Exclusion 	= 	IntegerField()
		Grey		=	IntegerField()


		widgets={
			"name_visit":TextInput(attrs={
				'class':'form-control',
				'placeholder':'Наименование визита'
				}),
			"date":DateInput(format=('%Y-%m-%d'), attrs={
				'class':'form-control',
				'placeholder':'Дата визита',
				'input_type' : 'text',
				'type': 'date'
				}),
			"inform_consent":RadioSelect(attrs={
				'class':'form-control'
				}),
			"comply_all_study":RadioSelect(attrs={
				'class':'form-control'
				}),
			"female_age":RadioSelect(attrs={
				'class':'form-control'
				}),
			"current_preg_lact":RadioSelect(attrs={
				'class':'form-control'
				}),
			"history_hysterectomy":RadioSelect(attrs={
				'class':'form-control'
				}),
			"risk_no_compliance":RadioSelect(attrs={
				'class':'form-control'
				}),
			"unwillingness":RadioSelect(attrs={
				'class':'form-control'
				}),
			"medicince_listed_now_10":RadioSelect(attrs={
				'class':'form-control'
				}),
			"medicince_listed_3month_10":RadioSelect(attrs={
				'class':'form-control'
				}),  
			"Phenotype":TextInput(attrs={
				'class':'form-control',
				'placeholder':'Фенотип'
				}),
			"PCOS_text":Textarea(attrs={
				'class':'form-control',
				'placeholder':'Текст заключения'
				}), 
			"Exclusion_text":Textarea(attrs={
				'class':'form-control',
				'placeholder':'Текст исключения'
				}),         
		};

class AppointmentForm(ModelForm):
	class Meta:
		model = Appointment
		fields=['patient_key','doctor_key','visit_key','date','periods','type_menstual_disorders_1','type_menstual_disorders_2','type_menstual_disorders_3','type_menstual_disorders_4','min_menstrual','max_menstrual','sum_physician']
		patient_key=ModelChoiceField(
				queryset=Patient.objects.all(), 
				empty_label=None)
		doctor_key=ModelChoiceField(
				queryset=Doctor.objects.all(), 
				empty_label=None)
		visit_key=ModelChoiceField(
				queryset=Visit.objects.all(), 
				empty_label=None)
		periods:IntegerField()
		type_menstual_disorders_1:IntegerField()
		type_menstual_disorders_2:IntegerField()
		type_menstual_disorders_3:IntegerField()
		type_menstual_disorders_4:IntegerField()
		min_menstrual:IntegerField()
		max_menstrual:IntegerField()
		sum_physician:IntegerField()
		widgets={
			"date":DateInput(format=('%Y-%m-%d'), attrs={
				'class':'form-control',
				'placeholder':'Дата приема',
				'input_type' : 'text',
				'type': 'date'
				}),        
		}

class UltrasoundForm(ModelForm):
	class Meta:
		model = Ultrasound
		fields=['patient_key','visit_key', 'doctor_key','date','left_ovary_key','right_ovary_key',
		'right_ovary_volume','right_ovary_follicle','diameter_cyst_right','left_ovary_volume',
		'left_ovary_follicle','diameter_cyst_left','left_ovary_front', 'right_ovary_front','left_ovary_posterior',
		'right_ovary_posterior','left_ovary_side','right_ovary_side']
		patient_key=ModelChoiceField(
				queryset=Patient.objects.all(), 
				empty_label=None)
		doctor_key=ModelChoiceField(
				queryset=Doctor.objects.all(), 
				empty_label=None)
		visit_key=ModelChoiceField(
				queryset=Visit.objects.all(), 
				empty_label=None)
		left_ovary_key		:IntegerField()
		right_ovary_key		:IntegerField()
		right_ovary_volume	:FloatField()
		right_ovary_follicle:FloatField()
		diameter_cyst_right	:FloatField()
		left_ovary_volume	:FloatField()
		left_ovary_follicle	:FloatField()
		diameter_cyst_left	:FloatField()
		left_ovary_front	:FloatField()
		right_ovary_front	:FloatField()
		left_ovary_posterior	:FloatField()	
		right_ovary_posterior	:FloatField()
		left_ovary_side		:FloatField()
		right_ovary_side	:FloatField()
		widgets={
			"date":DateInput(format=('%Y-%m-%d'), attrs={
				'class':'form-control',
				'placeholder':'Дата приема',
				'input_type' : 'text',
				'type': 'date'
				}),
			      
		}

class LaboratoryForm(ModelForm):
	class Meta:
		model = Laboratory_test
		fields=['patient_key','visit_key','date', 'value_testosteron', 'value_testosteron_unit_key',
		'value_shbg', 'value_shbg_unit_key','value_tsh','value_tsh_unit_key','value_17hp_unit_key', 'day_mens_prl', 
		'value_17hp', 'value_prl_unit_key','value_prl', 'value_dheas', 'value_dheas_unit_key']
		patient_key=ModelChoiceField(
				queryset=Patient.objects.all(), 
				empty_label=None)
		visit_key=ModelChoiceField(
				queryset=Visit.objects.all(), 
				empty_label=None)
		value_testosteron_unit_key	:IntegerField()
		value_shbg_unit_key			:IntegerField()
		value_tsh_unit_key			:IntegerField()
		value_17hp_unit_key			:IntegerField()
		value_prl_unit_key			:IntegerField()
		value_dheas_unit_key		:IntegerField()
		value_testosteron:FloatField()
		value_shbg 		 :FloatField()
		value_tsh 		 :FloatField()
		day_mens_prl 	 :IntegerField()
		value_17hp 		 :FloatField()
		value_prl 		 :FloatField()
		value_dheas		 :FloatField()
		widgets={
			"date":DateInput(format=('%Y-%m-%d'), attrs={
				'class':'form-control',
				'placeholder':'Дата приема',
				'input_type' : 'text',
				'type': 'date'
				}),       
		}

class FullForm(ModelForm):
	class Meta:
		model = Patient
		fields=['name_patient','day_of_birth','ethnicity_key']
		ethnicity_key=ModelChoiceField(
				queryset=Ethnicity.objects.all(), 
				empty_label=None)
		widgets={
			"name_patient":TextInput(attrs={
				'class':'form-control',
				'placeholder':'ФИО пациента'
				}),
			"day_of_birth":DateInput(format=('%Y-%m-%d'), attrs={
				'class':'form-control',
				'placeholder':'Дата рождения',
				'input_type' : 'text',
				'type': 'date'
				}),           
		};

