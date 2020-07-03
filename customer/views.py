from django.shortcuts import render
from .forms import ClientForm
from .models import Client
from django.views.generic.edit import FormView

# Create your views here.


class SignUp(FormView):
    template_name = 'blogApi/tenant_registration.html'
    form_class = ClientForm

    def get(self, request, *args, **kwargs):
        form = ClientForm()
        context = {'form': form}
        return render(request, 'blogApi/tenant_registration.html', context)

    def post(self, request, *args, **kwargs):
        form = ClientForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            schema_name = form.cleaned_data['schema_name']
            domain_url = name + ".localhost"
            Client.objects.create(name=name, schema_name=schema_name, domain_url=domain_url)
            return render(request, 'blogApi/tenant_registration.html', {'form': form})
        return render(request, 'blogApi/tenant_registration.html', {'form': form})





