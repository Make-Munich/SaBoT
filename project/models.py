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


SLEVEL = (
        (1, _("Maker")),
        (2, _("Maker with the intention of selling something")),
        (3, _("Professional Exhibitor")),
        (4, _("Platin Sponsor")),
        (5, _("Gold Sponsor")),
        (6, _("Silber Sponsor")),
        (7, _("Bronze Sponsor")),
        (8, _("Starter Sponsor")),
        (9, _("Supporter")),
)

ABRANDING = (
        (1, _("No Branding")),
        (2, _("3D Druck")),
        (3, _("AR & VR")),
        (4, _("Biohacking/ Citizen Science")),
        (5, _("Creativity, Art & Sound")),
        (6, _("Design & Handwerk")),
        (7, _("DIY")),
        (8, _("Electronic Innovators")),
        (9, _("FabLab")),
        (10, _("FashTech")),
        (11, _("Foodmaker")),
        (12, _("Funk & Radio")),
        (13, _("Green Maker")),
        (14, _("Robotic")),
        (15, _("Tools  ")),   
)

TALK = (
        (1, _("none agreed")),
        (2, _("1 time")),
        (3, _("2 times")),      
)

WORKSHOP = (
        (1, _("none")),
        (2, _("agreed")),
        (3, _("at own booth")),
        (4, _("in a workshop area")),
        (5, _("at booth & in workshop area")),     
)

TICKETS = (
        (0, _("0")),
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
        (11, _("11")),
        (12, _("12")),
        (13, _("13")),
        (14, _("14")),
        (15, _("15")),
        (16, _("16")),
        (17, _("17")),
        (18, _("18")),
        (19, _("19")),
        (20, _("20")),
)

PARKING = (
        (0, _("0")),
        (1, _("1")),
        (2, _("2")),
        (3, _("3")),
        (4, _("4")),
        (5, _("5")),
)

TSTATE = (
        (1, _(" ")),
        (1, _("in Progress")),
        (2, _("final")),      
)

DISTRIBUTION = (
        (1, _("during Check-in")),
        (2, _("desired in advance by mail")),
        (3, _("sended via mail")),
)


class Project(models.Model):
        projectName = models.CharField(max_length=128, verbose_name=_("Project name"))
        projectStatus = models.PositiveIntegerField(choices=PSTATE, verbose_name=_("Project status"), default=1)
        createDate = models.DateField(auto_now_add=True,editable=False)
        modifyDate = models.DateField(auto_now=True, editable=False)
        modifyBy = models.TextField(blank=True, verbose_name=_("Modify by"))
        firstname = models.CharField(max_length=30, blank=True, verbose_name=_("Firstname"))
        lastname = models.CharField(max_length=30, blank=True, verbose_name=_("Lastname"))
        email = models.EmailField(blank=True, verbose_name=_("Email"))
        phone = models.CharField(max_length=20, blank=True, verbose_name=_("Phone"))
        homepage = models.URLField(blank=True, verbose_name=_("Project homepage url"))
        projecttype = models.PositiveIntegerField(choices=PTYPE, verbose_name=_("Project type"), default=1)
        language = models.PositiveIntegerField(choices=CLANG, verbose_name=_("In which language do you want to communicate?"), default=1)
        hear = models.CharField(max_length=20, blank=True, verbose_name=_("How did you hear from us?"))
        recommendation = models.CharField(max_length=50, blank=True, verbose_name=_("Recommendation"))
        generalComment = models.TextField(blank=True, verbose_name=_("Comment"))
        internalComment = models.TextField(blank=True, verbose_name=_("Internal comments"))


        descriptionDE = models.TextField(max_length=900, blank=True, verbose_name=_("Description text of your project (German)"))
	descriptionEN = models.TextField(max_length=900, blank=True, verbose_name=_("Description text of your project (English)"))
        projectArea = MultiSelectField(blank=True, choices=AREAS, max_choices=7, verbose_name=_("Which area is your project in?"))
        logoOrg = models.ImageField(blank=True,upload_to="projects/logos", verbose_name=_("Organisation logo"))
        logo = models.ImageField(blank=True,upload_to="projects/logos", verbose_name=_("Project logo"))
        logoTeam = models.ImageField(blank=True,upload_to="projects/logos", verbose_name=_("Team logo"))
        video = models.URLField(blank=True, verbose_name=_("Project video url"))


        boothDescription = models.TextField(max_length=300, blank=True, verbose_name=_("Booth description"))		
	boothLocation = models.CharField(max_length=10, blank=True, verbose_name=_("Booth location"))
        boothArea = models.PositiveIntegerField(choices=BAREA, verbose_name=_("Booth area"), default=0)
        boothStatus = models.PositiveIntegerField(choices=BSTATE, verbose_name=_("Booth status"), default=1)
        boothHallStatus = models.PositiveIntegerField(choices=BHSTATE, verbose_name=_("Hall state"), default=1)
	boothTables = models.PositiveIntegerField(choices=TABLES, verbose_name=_("How many tables do you need?"), default=0)
	boothChairs = models.PositiveIntegerField(choices=CHAIRS, verbose_name=_("How many chairs do you need?"), default=0)
        boothBenches = models.PositiveIntegerField(choices=BENCHES, verbose_name=_("How many benches do you need?"), default=0)
        boothTablesPlan = models.PositiveIntegerField(default=0, blank=True, verbose_name=_("Tables planned"))
        boothTablesRes = models.PositiveIntegerField(default=0, blank=True, verbose_name=_("Tables reserve"))
        boothChairsPlan = models.PositiveIntegerField(default=0, blank=True, verbose_name=_("Chairs planned"))
        boothChairsRes = models.PositiveIntegerField(default=0, blank=True, verbose_name=_("Chairs reserve"))
        boothBenchesPlan = models.PositiveIntegerField(default=0, blank=True, verbose_name=_("Benches planned"))
        boothBenchesRes = models.PositiveIntegerField(default=0, blank=True, verbose_name=_("Benches reserve"))
        boothSize = models.CharField(max_length=20, blank=True, verbose_name=_("Booth size"))
        boothSizePlan = models.CharField(max_length=20, blank=True, verbose_name=_("Booth size planned"))
        boothPower = models.PositiveIntegerField(choices=POWER, verbose_name=_("Power"), default=1)
        boothPowerPlan = models.PositiveIntegerField(choices=POWER, verbose_name=_("Power planned"), default=1)
        boothExtras = MultiSelectField(blank=True, choices=EXTRAS, max_choices=9, verbose_name=_("Booth extras"))
        boothExtrasComment = models.TextField(max_length=300, blank=True, verbose_name=_("Here you have the chance to leave us further comments regarding your booth"))
        boothOwn = models.TextField(max_length=300, blank=True, verbose_name=_("Own equipment"))
        boothSafety= models.TextField(max_length=300, blank=True, verbose_name=_("Safety precautions"))
        boothComment = models.TextField(blank=True, verbose_name=_("Internal comments"))
        boothLastMinute = models.TextField(blank=True, verbose_name=_("Last minute"))


        serviceTickets = models.PositiveIntegerField(choices=TICKETS, verbose_name=_("How many tickets do you need?"), default=0)
        serviceTicketsGiven = models.PositiveIntegerField(choices=TICKETS, verbose_name=_("How many tickets have been given"), default=0)
        serviceParking = models.PositiveIntegerField(choices=PARKING, verbose_name=_("How many parking tickets do you need?"), default=0)
        serviceParkingGiven = models.PositiveIntegerField(choices=PARKING, verbose_name=_("How many parking tickets have been given"), default=0)
        serviceStatus = models.PositiveIntegerField(choices=TSTATE, verbose_name=_("Ticket status"), default=0)
        serviceDistribution = models.PositiveIntegerField(choices=DISTRIBUTION, verbose_name=_("Distribution"), default=1)
        serviceDistributed = models.CharField(max_length=30, blank=True, verbose_name=_("Distributed"))
        serviceSponsorlevel = models.CharField(max_length=30, blank=True, verbose_name=_("Sponsorlevel"))
        serviceAreabranding = models.CharField(max_length=30, blank=True, verbose_name=_("Areabranding"))
        serviceWorkshop = models.PositiveIntegerField(choices=WORKSHOP, verbose_name=_("Workshop"), default=1)
        serviceTalk = models.PositiveIntegerField(choices=TALK, verbose_name=_("Talk"), default=1)
        serviceComments = models.TextField(max_length=300, blank=True, verbose_name=_("Agreements"))
        serviceInternalComments = models.TextField(max_length=300, blank=True, verbose_name=_("Internal comments"))


        talkComment = models.TextField(blank=True, verbose_name=_("Here you have the chance to leave us further comments regarding your talk"))

        workshopComment = models.TextField(blank=True, verbose_name=_("Here you have the chance to leave us further comments regarding your workshop"))

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
