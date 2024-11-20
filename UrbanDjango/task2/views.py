from django.shortcuts import render


# Create your views here.
# Create your views here.
# def class_temp(request):
#     return render(request, 'class_template.html')

def func_temp(request):
    return render(request, 'second_task/func_template.html')

# class class_temp(TemplateView):
#     template_name = 'second_task/class_template.html'
