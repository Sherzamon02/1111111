from django.db import models

# Create your models here.



#
# class File(models.Model):
# 	file = models.FileField(upload_to='documents/%Y/%m/%d')
# 	# title=models.CharField(max_length=50)
# 	# keyword=models.CharField(max_length=200,null=True,blank=True)
# 	# password=models.CharField(max_length=200,null=True,blank=True)
#
#
# 	def __str__(self):
# 		return "Fayllar"
#
#
#
#
#
#


class Upload(models.Model):
    upload_file = models.FileField()
    upload_date = models.DateTimeField(auto_now_add =True)


class FileDownload(models.Model):
    fileurl=models.TextField(null=True,blank=True)
    keyword=models.CharField(max_length=200,null=True,blank=True)
    password=models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.fileurl



