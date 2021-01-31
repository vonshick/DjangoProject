from django.contrib.auth.views import FormView
from django.contrib import messages
from django.urls import reverse_lazy
from my_app.models import NewUser
from django.views.generic import CreateView


class CreateNewUserView(CreateView):
    model = NewUser
    fields = ('email', 'username', 'date_of_birth', 'password')
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        for field in CreateNewUserView.fields:
            if(form.data[field] is None or form.data[field] == ''):
                messages.error(
                    self.request,
                    f'The {field} field can not be empty'
                )
                return self.form_invalid(form)

        user = form.save(commit=False)
        user.set_password(form.data['password'])
        user.save()
        
        messages.success(
            self.request,
            'New user created successfully'
        )

        return super().form_valid(form)
