from django import forms
from models import Project
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Div, HTML, ButtonHolder
from crispy_forms.bootstrap import FormActions, StrictButton, TabHolder, Tab, PrependedText, InlineCheckboxes, InlineField
import requests
from django.contrib.auth.models import User
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)

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
		#self.helper.form_class='form-horizontal'
		self.helper.layout = Layout(
			Field("projectName"),
			Div(
        		Div('firstname', css_class='col-md-6',),
        		Div('lastname', css_class='col-md-6',),
        		css_class='row',
    		),
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

		#current_user = get_current_user()
		#print "user: %s" % current_user

		#print User.objects.all()
		#user = User.objects.get(username=get_current_user())
		#print user.is_staff
		
		

		#self.helper[1:3].wrap_together(Div, css_class="name-wrapper")
		#self.helper['firstname'].wrap(Field, css_class="col-md-6", wrapper_class="firstname")
		#self.helper['lastname'].wrap(Field, css_class="col-md-6", wrapper_class="lastname")

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
		self.helper.layout = Layout(
			Div(HTML("<p>Think of it as a letter of introduction, your chance to grab a reader's interest. Tell them why they should care about your work. Preferably you keep it short (300 and 900 characters) You can change the text later.</p>")),
			Field("descriptionDE"),
			Field("descriptionEN"),
			Field("projectArea"),
			Div(HTML("<p>Please provide us a picture or logo of your project. We would like to promote your participation on our website.</p>"))
		)
		if self.instance and self.instance.logoOrg:
			self.helper.layout.extend([
				Field("logoOrg"),
				Div(HTML("<p>Current logo:</p><img src=\"{{object.logoOrg.url}}\" style=\"max-height:200px\"/>"), css_class = "control-group"),	
			])
		else:
			self.helper.layout.append(
				Div(Div(Field("logoOrg"),css_class = "col-md-2"), css_class = "row"),
			)	

		if self.instance and self.instance.logo:
			self.helper.layout.extend([
				Field("logo"),
				Div(HTML("<p>Current logo:</p><img src=\"{{object.logo.url}}\" style=\"max-height:200px\"/>"), css_class = "control-group"),	
			])
		else:
			self.helper.layout.append(
				Div(Div(Field("logo"),css_class = "col-md-2"), css_class = "row"),
			)	

		if self.instance and self.instance.logoTeam:
			self.helper.layout.extend([
				Field("logoTeam"),
				Div(HTML("<p>Current logo:</p><img src=\"{{object.logoTeam.url}}\" style=\"max-height:200px\"/>"), css_class = "control-group"),	
			])
		else:
			self.helper.layout.append(
				Div(Div(Field("logoTeam"),css_class = "col-md-2"), css_class = "row"),
			)	
		self.helper.add_input(Submit("Save", "Save changes"))
		

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
			Div(HTML("<p>Maker booths are the core of Make Munich. Now we need some information from you to get an idea in what you are planning.</p><p>Maker Booth: A standard booth consists of 2x2.2m of space, 1 table (0.5x2.2m), and 1 chair. Most stands will have fence back walls.</p>")),
			Div(HTML("<p>Describe what you will bring to Make Munich. Do provide any hands-on activities at your booth? (Note: There is a special form for workshops)</p>")),
			Field("boothDescription"),
			Div(
        		Div('boothTables', css_class='col-md-4',),
        		Div('boothChairs', css_class='col-md-4',),
				Div('boothBenches', css_class='col-md-4',),
        		css_class='row',
    		),
			Field("boothPower"),
			Field("boothExtras"),
			Field("boothExtrasComment"),
			Field("boothOwn"),
			Field("boothSafety"),
#			FormActions(Submit("Save", "Save changes"))
		)
		self.helper.add_input(Submit("Save","Save changes"))


class ProjectServiceForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = (
			"serviceTickets", 
			"serviceParking",
			)

	def __init__(self, *args, **kwargs):
		super(ProjectServiceForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Div(HTML("<p>Team members: Admission tickets for 2 makers are included with your booth. More tickets can be ordered</p><p>Exhibitor parking tickets: On-site parking at the venue is possible and there are 3-day parking permits available (valid from Friday to Sunday) for 10 € per vehicle.</p>")),
			Div(HTML("<p>Please select your total(!) team size</p>")),
			Field("serviceTickets"),
			Div(HTML("<p>Please select the number of desired 3-day parking tickets</p>")),
			Field("serviceParking"),
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
