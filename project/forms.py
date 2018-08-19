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
		fields = ("projectName", "logo", "homepage")

		widgets = {
			"logo" : forms.widgets.FileInput,
		}

	def __init__(self, *args, **kwargs):
		super(ProjectGeneralForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		if self.instance and self.instance.logo:
			self.helper.layout = Layout(
				Field("projectName"),
				Field("logo"),
				Div(
					HTML("<p>Current logo:</p><img src=\"{{object.logo.url}}\" style=\"max-height:200px\"/>"),
					css_class = "control-group"),
				Field("homepage"),
#				FormActions(Submit("Save", "Save changes"))
			)
		else:
			self.helper.layout = Layout(
				Field("projectName"),
				Div(
					Div(Field("logo"),css_class = "col-md-2"),
					css_class = "row"
				),
				Field("homepage"),
#				FormActions(Submit("Save", "{% if object %}Save changes{% else %}Register{% endif %}"))
			)

		if self.instance is not None and self.instance.id is not None:
			self.helper.add_input(Submit("Save", "Save changes"))
		else:
			self.helper.add_input(Submit("Save", "Register"))

class ProjectDescriptionForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ("descriptionDE", "descriptionEN")

	def __init__(self, *args, **kwargs):
		super(ProjectDescriptionForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Field("descriptionDE"),
			Field("descriptionEN"),
#			FormActions(Submit("Save", "Save changes"))
		)
		self.helper.add_input(Submit("Save","Save changes"))

class ProjectBoothForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ("boothPreferedLocation", "boothNumTables", "boothNumChairs", "boothPower", "boothArea", "boothComment")

	def __init__(self, *args, **kwargs):
		super(ProjectBoothForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Field("boothPreferedLocation"),
			Field("boothNumTables"),
			Field("boothNumChairs"),
            Field("boothPower"),
			Field("boothArea"),
			Div("boothComment", HTML("{% if user.is_staff %} <p>Admin only</p> {% endif %}")),
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

	def __init__(self, user, *args, **kwargs):
		self.user = user
		kwargs['instance'] = user
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
