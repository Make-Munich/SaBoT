# Create your views here.
def get_form_kwargs(self):
    kwargs = super(project_update_talk, self).get_form_kwargs()
    kwargs.update({'user': self.request.user})
    return kwargs