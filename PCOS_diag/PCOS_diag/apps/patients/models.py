import datetime
from django.db import models

from django.utils import timezone

BOOL_CHOICES = ((True,'Yes'), (False,'No'))	

class Ethnicity(models.Model):
	name_ethnicity = models.CharField('Наименование ethnicity', max_length=50)
	def __str__(self):
		return self.name_ethnicity

class Doctor(models.Model):
	name_doctor = models.CharField('Имя доктора', max_length=200)
	def __str__(self):
		return self.name_doctor


class Patient(models.Model):
	name_patient = models.CharField('ФИО', max_length=200)
	day_of_birth     = models.DateField('Дата рождения')
	ethnicity_key    = models.ForeignKey(Ethnicity, on_delete=models.CASCADE)
	def __str__(self):
		return self.name_patient

class Visit(models.Model):
	name_visit			= models.CharField('Номер визита', max_length=20)
	patient_key			= models.ForeignKey(Patient,  on_delete=models.CASCADE)
	doctor_key			= models.ForeignKey(Doctor, on_delete=models.CASCADE)
	date 				= models.DateField()
	age_visit			= models.IntegerField()
	inform_consent		= models.BooleanField(choices=BOOL_CHOICES,  default='No')
	comply_all_study	= models.BooleanField(choices=BOOL_CHOICES,  default='No')
	female_age			= models.BooleanField(choices=BOOL_CHOICES,  default='No')
	current_preg_lact	= models.BooleanField(choices=BOOL_CHOICES,  default='No')
	history_hysterectomy	= models.BooleanField(choices=BOOL_CHOICES,  default='No')
	risk_no_compliance		= models.BooleanField(choices=BOOL_CHOICES,  default='No')
	unwillingness				= models.BooleanField(choices=BOOL_CHOICES,  default='No')
	medicince_listed_now_10	= models.BooleanField(choices=BOOL_CHOICES,  default='No')
	medicince_listed_3month_10= models.BooleanField(choices=BOOL_CHOICES,  default='No')
	PCOS 						= models.IntegerField(blank=True, null=True)
	Exclusion 					= models.IntegerField(blank=True, null=True)
	Grey 						= models.IntegerField(blank=True, null=True)
	Phenotype 					= models.CharField('Фенотип', max_length=1,blank=True)
	PCOS_text 					= models.TextField('Заключение', max_length=500,blank=True)
	Exclusion_text				= models.TextField('ПричиныИсключения', max_length=500,blank=True)
	def __str__(self):
		return self.name_visit+"-"+str(self.patient_key)+"-"+str(self.date)


class Ultrasound(models.Model):
	patient_key			= models.ForeignKey(Patient,  on_delete=models.CASCADE)
	visit_key			= models.ForeignKey(Visit,  on_delete=models.CASCADE)
	doctor_key			= models.ForeignKey(Doctor, on_delete=models.CASCADE)
	left_ovary_key 			= models.IntegerField()
	right_ovary_key 		= models.IntegerField()
	date 				= models.DateField()
	right_ovary_volume  = models.FloatField()
	right_ovary_follicle= models.FloatField()
	diameter_cyst_right = models.FloatField()
	left_ovary_volume	= models.FloatField()
	left_ovary_follicle	= models.FloatField()
	diameter_cyst_left	= models.FloatField()
	left_ovary_front	= models.FloatField()
	right_ovary_front	= models.FloatField()
	left_ovary_posterior	= models.FloatField()	
	right_ovary_posterior	= models.FloatField()
	left_ovary_side		= models.FloatField()
	right_ovary_side	= models.FloatField()

	def __str__(self):
		return str(self.date)



class Appointment(models.Model):
	patient_key			= models.ForeignKey(Patient,  on_delete=models.CASCADE)
	visit_key			= models.ForeignKey(Visit,  on_delete=models.CASCADE)
	doctor_key			= models.ForeignKey(Doctor,  on_delete=models.CASCADE)
	date 				= models.DateField()
	periods				= models.IntegerField()
	type_menstual_disorders_1	=	models.IntegerField()
	type_menstual_disorders_2	=	models.IntegerField()
	type_menstual_disorders_3	=	models.IntegerField()
	type_menstual_disorders_4	=	models.IntegerField()
	min_menstrual		= models.IntegerField()
	max_menstrual		= models.IntegerField()
	sum_physician		= models.IntegerField()

	def __str__(self):
		return str(self.date)





class Laboratory_test(models.Model):
	patient_key			= models.ForeignKey(Patient,  on_delete=models.CASCADE)
	date 				= models.DateField()
	visit_key 			= models.ForeignKey(Visit, on_delete=models.CASCADE)
	value_testosteron	= models.FloatField()
	value_shbg			= models.FloatField()
	value_dheas			= models.FloatField()
	value_tsh			= models.FloatField()
	day_mens_prl		= models.IntegerField()
	value_17hp			= models.FloatField()
	value_prl			= models.FloatField()
	value_testosteron_unit_key	= models.IntegerField()
	value_shbg_unit_key			= models.IntegerField()
	value_dheas_unit_key		= models.IntegerField()
	value_tsh_unit_key			= models.IntegerField() 
	value_17hp_unit_key			= models.IntegerField()
	value_prl_unit_key			= models.IntegerField()
 
	def __str__(self):
		return str(self.date)



