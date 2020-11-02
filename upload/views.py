from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .forms import BookForm
from .models import Book 
# Create your views here.
class classhomeview(TemplateView):
    template_name='home.html'



def upload(request):
    context={}
    if request.method=='POST':
        uploaded_file=request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs=FileSystemStorage()
        name=fs.save(uploaded_file.name,uploaded_file)
        #url=fs.url(name)
        context['url']=fs.url(name)
    return render(request,'upload.html',context)




def book_list(request):
    text=Book.objects.all()
    return render(request,'book_list.html',{'text':text})


def upload_book(request):
    if request.method=='POST':

        form=BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book')
            
    else:
        form=BookForm()
    return render(request,'upload_book.html',{'form':form})