from django import forms
from models import Project
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Div, HTML, ButtonHolder
from crispy_forms.bootstrap import FormActions, StrictButton, TabHolder, Tab, PrependedText, InlineCheckboxes
import requests
from django.contrib.auth.models import User

class ProjectGeneralForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = (
			"projectName", 
			"firstname", 
			"lastname", 
			"email", 
			"phone", 
			"homepage", 
			"projecttype", 
			"language", 
			"hear", 
			"recommendation",
			"generalComment"
			)

	def __init__(self, *args, **kwargs):
		super(ProjectGeneralForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Field("projectName"),
			Field("firstname"),
			Field("lastname"),
			Field("email"),
			Field("phone"),
			Field("homepage"),
			Field("projecttype"),
			Field("language"),
			Field("hear"),
			Field("recommendation"),
			Field("generalComment"),
#			FormActions(Submit("Save", "Save changes"))
			)
		if self.instance is not None and self.instance.id is not None:
			self.helper.add_input(Submit("Save", "Save changes"))
		else:
			self.helper.add_input(Submit("Save", "Register"))

		

class ProjectDescriptionForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = (
			"descriptionDE", 
			"descriptionEN",
			"projectArea",
			"logoOrg",
			"logo", 
			"logoTeam",
			"video"
			)

		widgets = {
			"logoOrg" : forms.widgets.FileInput,
			"logo" : forms.widgets.FileInput,
			"logoTeam" : forms.widgets.FileInput,
		}

	def __init__(self, *args, **kwargs):
		super(ProjectDescriptionForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		if self.instance and self.instance.logo and self.instance.logoOrg and self.instance.logoTeam:
			self.helper.layout = Layout(
				Field("descriptionDE"),
				Field("descriptionEN"),
				Field("projectArea"),
				Field("logoOrg"),
					Div(
						HTML("<p>Current logo:</p><img src=\"{{object.logoOrg.url}}\" style=\"max-height:200px\"/>"),
						css_class = "control-group"),
				Field("logo"),
					Div(
						HTML("<p>Current logo:</p><img src=\"{{object.logo.url}}\" style=\"max-height:200px\"/>"),
						css_class = "control-group"),
				Field("logoTeam"),
					Div(
						HTML("<p>Current logo:</p><img src=\"{{object.logoTeam.url}}\" style=\"max-height:200px\"/>"),
						css_class = "control-group"),
				Field("video"),
#			FormActions(Submit("Save", "Save changes"))
			)
		else:
			self.helper.layout = Layout(
				Field("descriptionDE"),
				Field("descriptionEN"),
				Field("projectArea"),
				Div(
					Div(Field("logoOrg"),css_class = "col-md-2"),
					css_class = "row"
				),
				Div(
					Div(Field("logo"),css_class = "col-md-2"),
					css_class = "row"
				),
				Div(
					Div(Field("logoTeam"),css_class = "col-md-2"),
					css_class = "row"
				),
				Field("video"),self.helper.add_input(Submit("Save","Save changes"))
			)
		if self.instance is not None and self.instance.id is not None:
			self.helper.add_input(Submit("Save", "Save changes"))
		else:
			self.helper.add_input(Submit("Save", "Register"))


class ProjectBoothForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = (
			"boothDescription", 
			"boothTables",
			"boothChairs",
			"boothBenches",
			"boothPower",
			"boothExtras",
			"boothExtrasComment",
			"boothOwn",
			"boothSafety"
			)

	def __init__(self, *args, **kwargs):
		super(ProjectBoothForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Field("boothDescription"),
			Field("boothTables"),
			Field("boothChairs"),
            Field("boothBenches"),
			Field("boothPower"),
			Field("boothExtras"),
			Field("boothExtrasComment"),
			Field("boothOwn"),
			Field("boothSafety"),
#			FormActions(Submit("Save", "Save changes"))
		)
		self.helper.add_input(Submit("Save","Save changes"))

class ProjectTalkForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ("talkComment",)

	#print('ip: %s' % geodata['ip'])
	#print('country: %s' % geodata['country_name'])

	#talk_user = User.objects.get(email=username)

	def __init__(self, *args, **kwargs):
		#print kwargs['instance']
		self.user = kwargs.pop('user', None)
		#kwargs['instance'] = user
		print('user: %s' % self.user)
		#super().__init__(*args, **kwargs)
		#self.talk_user = User.get_username()
		#self.user = kwargs.pop('user')
		#self.endpoint = 'https://pretalx.mm.derchris.eu/api/events/mm2018/speakers/?q={user_email}'
		#self.talk_user = self.user
		#self.url = self.endpoint.format(user_email=self.talk_user)
		#self.headers = {'Authorization': 'Token b81068d5c94911ac8df1a0ff9d095decde1ced1a', 'Accept': 'application/json'}
		#self.response = requests.get(self.url, headers=self.headers)
		#if self.response.status_code == 200:  # SUCCESS
		#	self.talksdata = self.response.json()
		#	print self.talksdata
		super(ProjectTalkForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			ButtonHolder(
				HTML("<a class='btn btn-primary' href='https://pretalx.mm.derchris.eu/mm2018/me/submissions'>View or add submissions</a>"),
			),
			Field("talkComment"),
#			FormActions(Submit("Save", "Save changes"))
		)
		self.helper.add_input(Submit("Save","Save changes"))

class ProjectWorkshopForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ("workshopComment",)

	def __init__(self, *args, **kwargs):
		super(ProjectWorkshopForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			ButtonHolder(
				HTML("<a class='btn btn-primary'href='https://pretalx.mm.derchris.eu/mm19w/me/submissions'>View or add submissions</a>"),
			),
			Field("workshopComment"),
#			FormActions(Submit("Save", "Save changes"))
		)
		self.helper.add_input(Submit("Save","Save changes"))
