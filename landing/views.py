from django.http import HttpRequest, JsonResponse
from .forms import TemplateForm
from django.views.generic import TemplateView
from django.views import View

from django.shortcuts import render

# Create your views here.
class MyFormView(View):
    def get(self, request):
        form = TemplateForm()
        return render(request, 'landing/index.html', context={"form": form})

    def post(self, request):
        received_data=request.POST
        form=TemplateForm(received_data)
        if form.is_valid():
            Full_name = form.cleaned_data.get("Full_name")
            Email = form.cleaned_data.get("Email")
            Message = form.cleaned_data.get("Message")
            Subject = form.cleaned_data.get("Subject")
            # Заголовок HTTP_X_FORWARDED_FOR используется для идентификации исходного IP-адреса клиента,
            # который подключается к веб-серверу через HTTP-прокси или балансировщик нагрузки.
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]  # Получение IP
            else:
                ip = request.META.get('REMOTE_ADDR')  # Получение IP

            user_agent = request.META.get('HTTP_USER_AGENT')
            data = {
                'name': Full_name,
                'email': Email,
                'message': Message,
                'Subject': Subject,
                'ip_address': ip,
                'user_agent': user_agent
            }

            return JsonResponse(data, json_dumps_params={'ensure_ascii': False, 'indent': 4})

        return JsonResponse(form.cleaned_data, json_dumps_params={'ensure_ascii': False, 'indent': 4})
        # return render(request, 'landing/index.html', context={"form": form})