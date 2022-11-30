from .forms import DocumentForm
import os.path
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.http import HttpResponseRedirect


from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Upload,FileDownload


def Download(request):
    if request.method=='POST':
        context = {}
        keyword=request.POST['keyword1']
        pwd=request.POST['pwd1']
        print(keyword)
        print(pwd)
        try:
            file2=FileDownload.objects.filter(keyword=keyword ,password=pwd)
            print("file mavjud")
            file=file2.last()

            context['url2'] =file.fileurl
            print(context)


            return render(request, 'index.html',context)
        except:
            print("mavjudmas")
            context['xat'] ="Hech qanday fayl topilmadi"
            print(context)


            return render(request, 'index.html',context)


    return render(request,'index.html')



def Home(request):



    return render(request=request,template_name='index.html')


    # return render(request=request, template_name='index.html')




# def SendFile(request):
# 	if request.method == 'POST':
# 		uploaded_file = request.FILES['document']
# 		fs = FileSystemStorage()
# 		name = fs.save(uploaded_file.name, uploaded_file)
#
#
#
# 	return render(request, 'index.html', )
#

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        keyword=request.POST['keyword']
        pwd=request.POST['pwd']


        fs = FileSystemStorage("media")
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        context['keyword'] = keyword
        context['pwd'] = pwd
        user=FileDownload.objects.create(fileurl=fs.url(name),keyword=keyword,password=pwd)
        user.save()






    return render(request, 'index.html', context)
















			# Redirect to the document list after POST
#
# class UploadView(CreateView):
# 	model = Upload
# 	fields = ['upload_file', ]
# 	success_url = reverse_lazy('fileupload')
#
# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		context['documents'] = Upload.objects.all()
# 		return context
#
#




#
# def handle_uploaded_file(f):
#     with open('some/file/name.txt', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)



def download(request,path):
	file_path=os.path.join(settings.MEDIA_ROOT,path)
	if os.path.exists(file_path):
		with open(file_path,"rb") as fh:
			response=HttpResponse(fh.read(),content_type="application/resume")
			response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
			return  response


