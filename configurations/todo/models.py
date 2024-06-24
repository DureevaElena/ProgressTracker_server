from django.db import models

from django.contrib.auth import get_user_model



class NoteTodo(models.Model): 
    titletodo=models.CharField(max_length=56,null=False)
    notetodo=models.TextField(max_length=500, null=True, blank=True)
    authortodo=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    cattodo = models.ForeignKey('CategoryTodo', on_delete=models.PROTECT, null=True)
    note_picturetodo = models.ImageField(null=True, blank=True)
    dataendtodo = models.DateField(null=True, blank=True)
    statustodo = models.ForeignKey('StatusTodo', on_delete=models.PROTECT, null=True)

    
class CategoryTodo(models.Model):
    namecategorytodo = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.namecategorytodo 


class StatusTodo(models.Model):
    namestatustodo = models.CharField(max_length=50, db_index=True)


    def __str__(self): 
        return self.namestatustodo
    
class StageNoteTodo(models.Model):
    titlestagetodo = models.CharField(max_length=56, null=False)
    notestagetodo = models.TextField(max_length=500, null=True, blank=True)
    idnotetodo = models.ForeignKey(NoteTodo, on_delete=models.CASCADE, related_name='idnoteisstage')
    authorstagetodo = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    donetodo = models.ForeignKey('DoneTodo', on_delete=models.PROTECT, null=True)
 
class DoneTodo(models.Model):
    namedonetodo = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.namedonetodo 

