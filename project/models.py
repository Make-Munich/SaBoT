from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from multiselectfield import MultiSelectField

PREFERENCES = (
        (1, "Main Floor"),
        (2, "Stage"),
        (0, "No preference"),
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

        boothComment = models.TextField(blank=True, verbose_name=_("Here you have the chance to leave us further comments regarding your booth:"))

        talkComment = models.TextField(blank=True, verbose_name=_("Here you have the chance to leave us further comments regarding your booth:"))

        workshopComment = models.TextField(blank=True, verbose_name=_("Here you have the chance to leave us further comments regarding your booth:"))

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
