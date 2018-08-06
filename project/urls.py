from django.conf.urls import include, url
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q, Sum

from project.forms import ProjectGeneralForm, ProjectDescriptionForm, ProjectBoothForm, ProjectTalkForm, ProjectWorkshopForm
from project.models import Project, ProjectParticipants
from sabot.decorators import user_is_staff
from sabot.multiYear import YSListView, YSXMLListView, YSOwnerSettingCreateView, getActiveYear
from sabot.views import ParticipantsView, OwnerSettingCreateView, PermCheckUpdateView, EmailOutputView, XMLListView, MultipleListView, PropertySetterView, PermCheckPropertySetterView, PermCheckSimpleDeleteView, ArchiveCreatorView


urlpatterns = [
	url(r'^new$',
		login_required(YSOwnerSettingCreateView.as_view(
			model = Project,
			form_class = ProjectGeneralForm,
			template_name = "project/create.html",
			success_url = "/projects/{id}")),
		name="project_new"),
	url(r'^(?P<pk>[0-9]+)$',
		login_required(PermCheckUpdateView.as_view(
			model = Project,
			form_class = ProjectGeneralForm,
			template_name = "project/general.html",
			success_url = "/projects/{id}")),
		name = "project_update_general"),
	url(r'^(?P<pk>[0-9]+)/description$',
		login_required(PermCheckUpdateView.as_view(
			model = Project,
			form_class = ProjectDescriptionForm,
			template_name = "project/description.html",
			success_url = "/projects/{id}/description")),
		name = "project_update_texts"),
	url(r'^(?P<pk>[0-9]+)/booth$',
		login_required(PermCheckUpdateView.as_view(
			model = Project,
			form_class = ProjectBoothForm,
			template_name = "project/booth.html",
			success_url = "/projects/{id}/booth")),
		name = "project_update_booth"),
	url(r'^(?P<pk>[0-9]+)/talk$',
		login_required(PermCheckUpdateView.as_view(
			model = Project,
			form_class = ProjectTalkForm,
			template_name = "project/talk.html",
			success_url = "/projects/{id}/talk")),
		name = "project_update_talk"),
	url(r'^(?P<pk>[0-9]+)/workshop$',
		login_required(PermCheckUpdateView.as_view(
			model = Project,
			form_class = ProjectWorkshopForm,
			template_name = "project/workshop.html",
			success_url = "/projects/{id}/workshop")),
		name = "project_update_workshop"),
	url(r'^(?P<pk>[0-9]+)/participants$',
		login_required(ParticipantsView.as_view(
			object_class = Project,
			connection_table_class = ProjectParticipants,
			template_name = "project/participants.html")),
		name="project_participants"),
	url(r'^(?P<pk>[0-9]+)/accept$',
		user_is_staff(PropertySetterView.as_view(
			model = Project,
			property_name = "accepted",
			property_value = True,
			next_view = "project_list")),
		name="project_accept"),
	url(r'^(?P<pk>[0-9]+)/unaccept$',
		user_is_staff(PropertySetterView.as_view(
			model = Project,
			property_name = "accepted",
			property_value = False,
			next_view = "project_list")),
		name="project_unaccept"),
	url(r'^participants/remove/(?P<pk>[0-9]+)$',
		login_required(PermCheckSimpleDeleteView.as_view(
			model = ProjectParticipants,
			permission_checker = lambda obj, user: obj.project.has_write_permission(user),
			redirect = lambda obj, kwargs: reverse("project_participants", kwargs = { "pk" : obj.project_id }) )),
		name="project_participants_delete"),
	url(r'^participants/makeadmin/(?P<pk>[0-9]+)$',
		login_required(PermCheckPropertySetterView.as_view(
			model = ProjectParticipants,
			permission_checker = lambda obj, user: obj.project.has_write_permission(user),
			property_name = "isAdmin",
			property_value = True,
			redirect = lambda obj, kwargs: reverse("project_participants", kwargs = { "pk" : obj.project_id }) )),
		name="project_participants_make_admin"),
	url(r'^participants/revokeadmin/(?P<pk>[0-9]+)$',
		login_required(PermCheckPropertySetterView.as_view(
			model = ProjectParticipants,
			permission_checker = lambda obj, user: obj.project.has_write_permission(user),
			property_name = "isAdmin",
			property_value = False,
			redirect = lambda obj, kwargs: reverse("project_participants", kwargs = { "pk" : obj.project_id }) )),
		name="project_participants_revoke_admin"),
	url(r'^list\+planning/?',
		user_is_staff(YSListView.as_view(
			queryset = Project.objects.select_related(),
			template_name = "project/list+planning.html")),
			name="project_list_planning"),
	url(r'^list/?',
		user_is_staff(YSListView.as_view(
			queryset = Project.objects.select_related(),
			template_name = "project/list.html")),
			name="project_list"),
	url(r'^del/(?P<pk>[0-9]+)$',
		user_is_staff(DeleteView.as_view(
			model = Project,
			template_name= "project/del.html",
			success_url="/projects/list")),
			name="project_del"),
	url(r'^export/adminmail',
		user_is_staff(EmailOutputView.as_view(
			queryset = lambda req, kwargs : User.objects.filter(
				Q(projectparticipants__isAdmin=True,
				  projectparticipants__project__accepted=True,
				  projectparticipants__project__year=getActiveYear(req)) |
				Q(projects__accepted=True,projects__year=getActiveYear(req))
				).distinct(),
			template_name = "mail.html")),
			name="project_export_adminmail"),
	url(r'export/allmail',
		user_is_staff(EmailOutputView.as_view(
			queryset = lambda req, kwargs : User.objects.filter(
				Q(projectparticipants__project__accepted=True,
				  projectparticipants__project__year=getActiveYear(req)) |
				Q(projects__accepted=True,projects__year=getActiveYear(req))
				).distinct(),
			template_name = "mail.html")),
			name="project_export_allmail"),
	url(r'^export/xml',
		user_is_staff(YSXMLListView.as_view(
			queryset = Project.objects.select_related().filter(accepted=True),
			template_name = "project/xmlexport.html")),
			name="project_export_xml"),
]
