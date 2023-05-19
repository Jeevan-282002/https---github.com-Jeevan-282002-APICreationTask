from django.db import models

# Create your models here.

#creating client model

class Client(models.Model):
    
    client_id = models.IntegerField(primary_key= True)
    client_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models. CharField(max_length=100)

    def __str__(self): 
        return self.client_name

# creating users for project
class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=100)

    def __str__(self): 
        return self.user_name 
    



# creating project model

class Project(models.Model):
    
    project_id = models.IntegerField(primary_key=True)
    project_name = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    users = models.ForeignKey(User ,on_delete=models.CASCADE,  related_name='pro_users')
    
    

    def __str__(self): 
        return self.project_name 
    
    
    


