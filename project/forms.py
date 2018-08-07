from django import forms
from models import Project
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Div, HTML
from crispy_forms.bootstrap import FormActions, StrictButton, TabHolder, Tab

AREAS = (
        (1, "3D Printing"),
        (2, "Arduino"),
        (3, "Art"),
        (4, "Biohacking"),
        (5, "Bionics"),
        (6, "Crafts"),
        (7, "Design"),
        (8, "Digital Fabrication"),
        (9, "Education"),
        (10, "Electronics"),
        (11, "Fashion"),
        (12, "Food & Agriculture"),
        (13, "Garden"),
        (14, "Healthcare"),
        (15, "Home Automation"),
        (16, "Interaction"),
        (17, "Internet of Things"),
        (18, "Model Making"),
        (19, "New Materials"),
        (20, "Raspberry Pi"),
        (21, "Robot & Drones"),
        (22, "Science"),
        (23, "Social design"),
        (24, "Sustainability"),
        (25, "Startup / Small Business"),
        (26, "Tiny Houses"),
        (27, "Transportation"),
        (28, "Wearables"),
        (29, "Wellness"),
        (30, "Young Makers"),
        (31, "Other"),
)

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
		boothArea = forms.MultipleChoiceField(choices=AREAS,label="What area is your booth in?")
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Field("boothPreferedLocation"),
			Field("boothNumTables"),
			Field("boothNumChairs"),
            Field("boothPower"),
			'boothArea',
			Div("boothComment", HTML("{% if user.is_staff %} <p>Admin only</p> {% endif %}")),
#			FormActions(Submit("Save", "Save changes"))
		)
		self.helper.add_input(Submit("Save","Save changes"))

class ProjectTalkForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ("talkComment",)

	def __init__(self, *args, **kwargs):
		super(ProjectTalkForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
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
			Field("workshopComment"),
#			FormActions(Submit("Save", "Save changes"))
		)
		self.helper.add_input(Submit("Save","Save changes"))
