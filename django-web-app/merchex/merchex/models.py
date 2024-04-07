from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Advice(models.Model):
    idadvice = models.AutoField(db_column='idAdvice', primary_key=True) 
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    like = models.IntegerField(null=True)
    idcategory = models.ForeignKey('Category', models.DO_NOTHING, db_column='idCategory') 
    usrid = models.ForeignKey('user', models.DO_NOTHING, db_column='usrid')

    class Meta:
        managed = False
        db_table = 'advice'
        


class Care(models.Model):
    idcare = models.AutoField(db_column='idCare', primary_key=True)
    iduser = models.ForeignKey('User', models.DO_NOTHING, db_column='idusr')  
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=100)
    started_at = models.DateTimeField(blank=True, null=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    id_owner = models.IntegerField(db_column='Id_owner', default='iduser') 
    id_keeper = models.IntegerField(db_column='Id_keeper', blank=True, null=True) 
      

    class Meta:
        managed = False
        db_table = 'care'
        


class Category(models.Model):
    idcategory = models.AutoField(db_column='idCategory', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'category'
        


class Pictures(models.Model):
    idpictures = models.AutoField(db_column='idPictures', primary_key=True)
    url = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'pictures'
        


class Post(models.Model):
    idpost = models.AutoField(db_column='idPost', primary_key=True)
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=100)
    visibility = models.BooleanField()
    idcare = models.ForeignKey(Care, models.DO_NOTHING, db_column='idcare')
    idpictures = models.ForeignKey(Pictures, models.DO_NOTHING, db_column='idpicture',null=True)  
    read = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'post'
        

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('error email')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)
class User(models.Model):
    iduser = models.AutoField(db_column='idUser', primary_key=True)
    name = models.CharField(max_length=45)
    firstname = models.CharField(max_length=45)
    email = models.CharField(max_length=80, unique=True)
    adress = models.CharField(max_length=60)
    zip = models.IntegerField()
    city = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    password = models.CharField(max_length=80)
    role = models.CharField(max_length=45)
    lastconx = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'user'



class Verification(models.Model):
    idverif = models.AutoField(db_column='idVerif', primary_key=True)
    type = models.IntegerField()
    iduser = models.ForeignKey(User, models.DO_NOTHING, db_column='iduser')

    class Meta:
        managed = False
        db_table = 'verification'
        
