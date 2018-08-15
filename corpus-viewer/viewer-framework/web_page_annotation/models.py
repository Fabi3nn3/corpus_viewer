from django.db import models

# Create your models here.
class Annotation_Model(models.Model):
    hit = models.IntegerField(default=0)
    task = models.CharField(max_length=250)
    rating_m = models.CharField(max_length=250)



#class Annotation(models.Model):
    # primarykey: first album has id of one, each album added, increment id by one
    # foreignkey:
    #variable = column in database
    #this is what a album is made of, class actually called album
    #artist = models.CharField(max_length=250)
    #album_title = models.CharField(max_length=500)
    #genre = models.CharField(max_length=100)
    #album_logo = models.CharField(max_length=1000)
#could create another class song
#class Song(models.Model):
#how do we link album and song?
#cascade wenn album gelöscht wird werden auch songs gelöscht
    #album = models.ForeignKey(Album, on_delete=models.CASCADE)
    #file_type = models.CharField(max_length=10)
    #song_title = models.CharField(max_length=250)
