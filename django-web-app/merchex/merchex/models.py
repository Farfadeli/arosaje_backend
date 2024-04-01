from django.db import models


class Advice(models.Model):
    idadvice = models.IntegerField(db_column='idAdvice', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    like = models.IntegerField()
    category_idcategory = models.ForeignKey('Category', models.DO_NOTHING, db_column='Category_idCategory')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'advice'
        


class Care(models.Model):
    idcare = models.IntegerField(db_column='idCare', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=100)
    started_at = models.DateTimeField(blank=True, null=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    active = models.IntegerField()
    id_owner = models.IntegerField(db_column='Id_owner')  # Field name made lowercase.
    id_keeper = models.IntegerField(db_column='Id_keeper', blank=True, null=True)  # Field name made lowercase.
    user_iduser = models.ForeignKey('User', models.DO_NOTHING, db_column='User_idUser')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'care'
        


class Category(models.Model):
    idcategory = models.IntegerField(db_column='idCategory', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'category'
        


class Pictures(models.Model):
    idpictures = models.IntegerField(db_column='idPictures', primary_key=True)  # Field name made lowercase.
    url = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'pictures'
        


class Post(models.Model):
    idpost = models.IntegerField(db_column='idPost', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=100)
    visibility = models.IntegerField()
    care_idcare = models.ForeignKey(Care, models.DO_NOTHING, db_column='Care_idCare')  # Field name made lowercase.
    pictures_idpictures = models.ForeignKey(Pictures, models.DO_NOTHING, db_column='Pictures_idPictures')  # Field name made lowercase.
    read = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'post'
        


class User(models.Model):
    iduser = models.IntegerField(db_column='idUser', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45)
    firstname = models.CharField(max_length=45)
    email = models.CharField(max_length=80)
    adress = models.CharField(max_length=60)
    zip = models.IntegerField()
    city = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    password = models.CharField(max_length=80)
    role = models.CharField(max_length=45)
    lastconx = models.DateTimeField()
    advice_idadvice = models.ForeignKey(Advice, models.DO_NOTHING, db_column='Advice_idAdvice')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'
        


class Verification(models.Model):
    idverif = models.IntegerField(db_column='idVerif', primary_key=True)  # Field name made lowercase.
    type = models.IntegerField()
    user_iduser = models.ForeignKey(User, models.DO_NOTHING, db_column='User_idUser')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'verification'
        
