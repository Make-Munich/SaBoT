from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from multiselectfield import MultiSelectField

PSTATE = (
        (1, _("Submitted")),
        (2, _("Accepted")),
        (3, _("Rejected")),
        (4, _("Cancelled")),
        (5, _("Waiting list")),
)

PTYPE = (
        (1, _("Maker or NGO (no sales at the fair, free booth)")),
        (2, _("Maker with the intention of selling something at the fair (79 Euro per booth)")),
        (3, _("Startup exhibitor")),
        (4, _("Professional exhibitor")),
)

CLANG = (
        (1, _("german")),
        (2, _("english")),
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

BAREA = (
        (0, _("in progress")),
        (1, _("3D Printing")),
        (2, _("AR & VR")),
        (3, _("Biohacking/ Citizen Science")),
        (4, _("Creativity, Art & Sound")),
        (5, _("Design & Craft")),
        (6, _("DIY")),
        (7, _("Electronic Innovators")),
        (8, _("FabLab")),
        (9, _("FashTech")),
        (10, _("Foodmaker")),
        (11, _("Funk & Radio")),
        (12, _("Green Maker")),
        (13, _("Robotics")),
        (14, _("Tools")),
        (15, _("Workshops")),
)

BSTATE = (
        (1, _("Submitted")),
        (2, _("Accepted")),
        (3, _("Rejected")),
        (4, _("Booth detailing")),
        (5, _("Service completed")),
)

BHSTATE = (
        (1, _("Discrepancy in the hall plan")),
        (2, _("in the hall plan")),
)

CHAIRS = (
        (0, _("No chair")),
        (1, _("1")),
        (2, _("2")),
        (3, _("3")),
        (4, _("4")),
        (5, _("5")),
        (6, _("6")),
        (7, _("7"))
)

TABLES = (
        (0, _("No table")),
        (1, _("1")),
        (2, _("2")),
        (3, _("3")),
        (4, _("4")),
        (5, _("5")),
        (6, _("6")),
        (7, _("7")),
        (8, _("8")),
        (9, _("9")),
        (10, _("10")),
)

BENCHES = (
        (0, _("No bench")),
        (1, _("1")),
        (2, _("2")),
        (3, _("3")),
        (4, _("4")),
        (5, _("5")),
        (6, _("6")),
        (7, _("7")),
        (8, _("8")),
)

POWER = (
        (1, _("no power required")),
        (2, _("up to 5A, 230V -> max. 1150W")),
        (3, _("up to 10A, 230V -> max. 2300W")),
        (4, _("up to 16A, 230V -> max. 3200W")),
)

EXTRAS = (
        (1, _("More floor space (please specify below)")),
        (2, _("More tables or chairs")),
        (3, _("I don't need tables, I have my own system")),
        (4, _("My booth needs a back wall")),
        (5, _("Outdoor space")),
        (6, _("Internet access")),
        (7, _("Three-phase AC")),
        (8, _("A corner booth (without back wall)")),
        (9, _("My project uses radio frequencies (please specify below)")),
)


class Project(models.Model):
        projectName = models.CharField(max_length=128, verbose_name=_("Project name"))
        projectStatus = models.PositiveIntegerField(choices=PSTATE, verbose_name=_("Project state"), default=1)
        createDate = models.DateField(auto_now_add=True,editable=False)
        modifyDate = models.DateField(auto_now=True, editable=False)
        modifyBy = models.TextField(blank=True, verbose_name=_("Modify by"))
        firstname = models.CharField(max_length=30, blank=True, verbose_name=_("Firstname"))
        lastname = models.CharField(max_length=30, blank=True, verbose_name=_("Lastname"))
        email = models.EmailField(blank=True, verbose_name=_("Email"))
        phone = models.CharField(max_length=20, blank=True, verbose_name=_("Phone"))
        homepage = models.URLField(blank=True, verbose_name=_("Project homepage url"))
        projecttype = models.PositiveIntegerField(choices=PTYPE, verbose_name=_("Project type"), default=1)
        language = models.PositiveIntegerField(choices=CLANG, verbose_name=_("Which language do you want to communicate?"), default=1)
        hear = models.CharField(max_length=20, blank=True, verbose_name=_("How did you hear from us?"))
        recommendation = models.CharField(max_length=50, blank=True, verbose_name=_("Recommendation"))
        generalComment = models.TextField(blank=True, verbose_name=_("Comment"))
        internalComment = models.TextField(blank=True, verbose_name=_("Internal Comment"))


        descriptionDE = models.TextField(max_length=900, blank=True, verbose_name=_("Description text of your project (German)"))
	descriptionEN = models.TextField(max_length=900, blank=True, verbose_name=_("Description text of your project (English)"))
        projectArea = MultiSelectField(choices=AREAS, max_choices=7, verbose_name=_("Which area is your booth in?"))
        logoOrg = models.ImageField(blank=True,upload_to="projects/logos", verbose_name=_("Org logo"))
        logo = models.ImageField(blank=True,upload_to="projects/logos", verbose_name=_("Project logo"))
        logoTeam = models.ImageField(blank=True,upload_to="projects/logos", verbose_name=_("Team logo"))
        video = models.URLField(blank=True, verbose_name=_("Project video url"))


        boothDescription = models.TextField(max_length=300, blank=True, verbose_name=_("Booth Description"))		
	boothLocation = models.CharField(max_length=10, blank=True, verbose_name=_("Location"))
        boothArea = models.PositiveIntegerField(choices=BAREA, verbose_name=_("Booth area"), default=0)
        boothStatus = models.PositiveIntegerField(choices=BSTATE, verbose_name=_("Booth state"), default=1)
        boothHallStatus = models.PositiveIntegerField(choices=BHSTATE, verbose_name=_("Hall state"), default=1)
	boothTables = models.PositiveIntegerField(choices=TABLES, verbose_name=_("How many tables do you need?"), default=0)
	boothChairs = models.PositiveIntegerField(choices=CHAIRS, verbose_name=_("How many chairs do you need?"), default=0)
        boothBenches = models.PositiveIntegerField(choices=BENCHES, verbose_name=_("How many benches do you need?"), default=0)
        boothTablesPlan = models.PositiveIntegerField(default=0, blank=True, verbose_name=_("Tables Planned"))
        boothTablesRes = models.PositiveIntegerField(default=0, blank=True, verbose_name=_("Tables Reserve"))
        boothChairsPlan = models.PositiveIntegerField(default=0, blank=True, verbose_name=_("Chairs Planned"))
        boothChairsRes = models.PositiveIntegerField(default=0, blank=True, verbose_name=_("Chairs Reserve"))
        boothBenchesPlan = models.PositiveIntegerField(default=0, blank=True, verbose_name=_("Benches Planned"))
        boothBenchesRes = models.PositiveIntegerField(default=0, blank=True, verbose_name=_("Benches Reserve"))
        boothSize = models.CharField(max_length=20, blank=True, verbose_name=_("Booth size"))
        boothSizePlan = models.CharField(max_length=20, blank=True, verbose_name=_("Booth size Planned"))
        boothPower = models.PositiveIntegerField(choices=POWER, verbose_name=_("Power"), default=1)
        boothPowerPlan = models.PositiveIntegerField(choices=POWER, verbose_name=_("Power Planned"), default=1)
        boothExtras = MultiSelectField(choices=EXTRAS, max_choices=9, verbose_name=_("Booth extras"))
        boothExtrasComment = models.TextField(max_length=300, blank=True, verbose_name=_("Here you have the chance to leave us further comments regarding your booth:"))
        boothOwn = models.TextField(max_length=300, blank=True, verbose_name=_("Own equipment"))
        boothSafety= models.TextField(max_length=300, blank=True, verbose_name=_("safety precautions"))
        boothComment = models.TextField(blank=True, verbose_name=_("Internal comment:"))
        boothLastMinute = models.TextField(blank=True, verbose_name=_("Here you have the chance to leave us further comments regarding your booth:"))


        talkComment = models.TextField(blank=True, verbose_name=_("Here you have the chance to leave us further comments regarding your talk:"))

        workshopComment = models.TextField(blank=True, verbose_name=_("Here you have the chance to leave us further comments regarding your workshop:"))

        owner = models.ForeignKey(User,editable=False,related_name="projects")
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
