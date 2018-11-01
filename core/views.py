from django.shortcuts import render
from .forms import ContactForm
from django.views.generic import View, TemplateView, CreateView
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()

# def index(request):
#     return render(request, 'index.html')


class IndexView(TemplateView):

    template_name = 'index.html'


def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_email()
        success = True
    elif request.method == 'POST':
        messages.error(request, 'Formulário inválido.')
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html', context)


# class RegisterView(CreateView):
#
#     form_class = UserCreationForm
#     template_name = 'register.html'
#     model = User
#     success_url = reverse_lazy('index')


index = IndexView.as_view()
# register = RegisterView.as_view()
