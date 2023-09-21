from django.shortcuts import render
from .models import message
from .froms import messageForm
# Create your views here.
def index(request):
    message_list = message.objects.all()
    context_dict = {'categories': message_list}
    return render(request, 'index.html', context_dict)

def add_message(request):
    form = messageForm()
    if request.method == "POST":
        form = messageForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    return render(request,"show_message.html",{'form':form})