from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from multiselectfield import MultiSelectField

PREFERENCES = (
        (1, "Main Floor"),
        (2, "Stage"),
        (0, "No preference"),
)

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

class Exhibitor(models.Model):
	owner = models.ForeignKey(User,editable=False,related_name="exhibitors")
	createDate = models.DateField(auto_now_add=True,editable=False)
	modifyDate = models.DateField(auto_now=True, editable=False)
	projectName = models.CharField(max_length=128, verbose_name=_("Project name"))
	logo = models.ImageField(blank=True,upload_to="exhibitors/logos", verbose_name=_("Project logo"))
	homepage = models.URLField(blank=True, verbose_name=_("Project homepage url"))

	descriptionDE = models.TextField(blank=True, verbose_name=_("Description text of your project (German)"))
	descriptionEN = models.TextField(blank=True, verbose_name=_("Description text of your project (English)"))


	boothPreferedLocation = models.PositiveIntegerField(choices=PREFERENCES, verbose_name=_("Do you have a preferred location for your booth?"), default=0)
	boothNumTables = models.PositiveIntegerField(blank=True,null=True, verbose_name=_("How many tables do you need (roughly 1.20m x 0.80m)?"))
	boothNumChairs = models.PositiveIntegerField(blank=True,null=True, verbose_name=_("How many chairs do you need?"))
        boothPower = models.PositiveIntegerField(blank=True,null=True, verbose_name=_("Do you need power? (How many kwH)"))
        boothArea = MultiSelectField(choices=AREAS, max_length=3, max_choices=3, verbose_name=_("Which area is your booth in?"))
        boothComment = models.TextField(blank=True, verbose_name=_("Here you have the chance to leave us further comments regarding your booth:"))

	participants = models.ManyToManyField(User,blank=True,editable=False,related_name="exhibitorparticipation", through="ExhibitorParticipants")
	accepted = models.BooleanField(default=False, editable=False)

	year = models.PositiveIntegerField(editable=False, verbose_name=_("Conference year this exhibitor belongs to"))

	def has_read_permission(self, user):
		return ExhibitorParticipants.objects.filter(user=user).count() > 0 or user == self.owner

	def has_write_permission(self, user):
		return ExhibitorParticipants.objects.filter(user=user,isAdmin=True).count() > 0 or user == self.owner

class ExhibitorParticipants(models.Model):
	project = models.ForeignKey(Exhibitor)
	user = models.ForeignKey(User)
	isAdmin = models.BooleanField(default=False)
