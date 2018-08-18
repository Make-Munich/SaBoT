from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from multiselectfield import MultiSelectField

PREFERENCES = (
        (1, _("Main Floor")),
        (2, _("Stage")),
        (0, _("No preference")),
)

AREAS = (
        (1, _("3D Printing")),
        (2, _("Arduino")),
        (3, _("Art")),
        (4, _("Biohacking")),
        (5, _("Bionics")),
        (6, _("Crafts")),
        (7, _("Design")),
        (8, _("Digital Fabrication")),
        (9, _("Education")),
        (10, _("Electronics")),
        (11, _("Fashion")),
        (12, _("Food & Agriculture")),
        (13, _("Garden")),
        (14, _("Healthcare")),
        (15, _("Home Automation")),
        (16, _("Interaction")),
        (17, _("Internet of Things")),
        (18, _("Model Making")),
        (19, _("New Materials")),
        (20, _("Raspberry Pi")),
        (21, _("Robot & Drones")),
        (22, _("Science")),
        (23, _("Social design")),
        (24, _("Sustainability")),
        (25, _("Startup / Small Business")),
        (26, _("Tiny Houses")),
        (27, _("Transportation")),
        (28, _("Wearables")),
        (29, _("Wellness")),
        (30, _("Young Makers")),
        (31, _("Other")),
)


class Project(models.Model):
	owner = models.ForeignKey(User,editable=False,related_name="projects")
	createDate = models.DateField(auto_now_add=True,editable=False)
	modifyDate = models.DateField(auto_now=True, editable=False)
	projectName = models.CharField(max_length=128, verbose_name=_("Project name"))
	logo = models.ImageField(blank=True,upload_to="projects/logos", verbose_name=_("Project logo"))
	homepage = models.URLField(blank=True, verbose_name=_("Project homepage url"))

	descriptionDE = models.TextField(blank=False, verbose_name=_("Description text of your project (German)"))
	descriptionEN = models.TextField(blank=False, verbose_name=_("Description text of your project (English)"))

	boothPreferedLocation = models.PositiveIntegerField(choices=PREFERENCES, verbose_name=_("Do you have a preferred location for your booth?"), default=0)
	boothNumTables = models.PositiveIntegerField(blank=True,null=True, verbose_name=_("How many tables do you need (roughly 1.20m x 0.80m)?"))
	boothNumChairs = models.PositiveIntegerField(blank=True,null=True, verbose_name=_("How many chairs do you need?"))
        boothPower = models.PositiveIntegerField(blank=True,null=True, verbose_name=_("Do you need power? (How many kwH)"))
        boothArea = MultiSelectField(choices=AREAS, max_choices=31, verbose_name=_("Which area is your booth in?"))
        boothComment = models.TextField(blank=True, verbose_name=_("Here you have the chance to leave us further comments regarding your booth:"))

        talkComment = models.TextField(blank=True, verbose_name=_("Here you have the chance to leave us further comments regarding your talk:"))

        workshopComment = models.TextField(blank=True, verbose_name=_("Here you have the chance to leave us further comments regarding your workshop:"))

	participants = models.ManyToManyField(User,blank=True,editable=False,related_name="projectparticipation", through="ProjectParticipants")
	accepted = models.BooleanField(default=False, editable=False)

	year = models.PositiveIntegerField(editable=False, verbose_name=_("Conference year this project belongs to"))

	def has_read_permission(self, user):
		return ProjectParticipants.objects.filter(user=user).count() > 0 or user == self.owner

	def has_write_permission(self, user):
		return ProjectParticipants.objects.filter(user=user,isAdmin=True).count() > 0 or user == self.owner

class ProjectParticipants(models.Model):
	project = models.ForeignKey(Project)
	user = models.ForeignKey(User)
	isAdmin = models.BooleanField(default=False)
