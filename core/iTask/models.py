from this import d
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from matplotlib.pyplot import cla


# Table contributors as ct {
#   id int [pk, increment]
#   full_name varchar
#   short_name varchar
#   email_address varchar
#   status bit 
#   creation_date datetime
#   created_by_user_id int  
# }

class contributors(models.Model):
    full_name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255, null=True)
    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name_plural = "Contributors"
        verbose_name = "Contributor"


# Table clients as cl {
#   id int [pk, increment]
#   name varchar
#   owner_contributor_id int 
#   status bit 
#   creation_date datetime
#   created_by_user_id int 
# }

class clients(models.Model):
    name = models.CharField(max_length=255)
    owner_contributor_id = models.ForeignKey(contributors, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Clients"
        verbose_name = "Client"


# Table projects as pj {
#   id int [pk, increment]
#   name varchar
#   focal_person_contributor_id int 
#   client_id int 
#   status bit 
#   creation_date datetime
#   created_by_user_id int 
# }

class projects(models.Model):
    name = models.CharField(max_length=255)
    focal_person_contributor_id = models.ForeignKey(contributors, on_delete=models.CASCADE, null=True)
    client_id = models.ForeignKey(clients, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Projects"
        verbose_name = "Project"


# Table activities as a {
#   id int [pk, increment]
#   name varchar 
#   status bit 
#   creation_date datetime
#   created_by_user_id int 
# }

class activities(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.short_name + " - " + self.name
    
    class Meta:
        verbose_name_plural = "Activities"
        verbose_name = "Activity"

# Table completion_statuses as cs {
#   id int [pk, increment]
#   name varchar
#   sort_id int 
#   status bit
#   creation_date datetime
#   created_by_user_id int 
# }

class completion_statuses(models.Model):
    name = models.CharField(max_length=255)
    sort_id = models.IntegerField()
    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.sort_id) + " - " + self.name
    
    class Meta:
        verbose_name_plural = "Completion Statuses"
        verbose_name = "Completion Status"



# Table priorities as p {
#   id int [pk, increment]
#   name varchar
#   sort_id int
#   status bit 
#   creation_date datetime
#   created_by_user_id int 
# }

class priorities(models.Model):
    name = models.CharField(max_length=255)
    sort_id = models.IntegerField()
    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.sort_id) + " - " + self.name
    
    class Meta:
        verbose_name_plural = "Priorities"
        verbose_name = "Priority"


# Table tasks as t {
#   id int [pk, increment]
#   tasks_types tasks_types 
#   date datetime
#   activity_id int 
#   name varchar
#   business_value int
#   completion_status_id int
#   completed_by_contibutor_id int 
#   client_id int
#   project_id int 
#   status bit 
#   creation_date datetime
#   created_by_user_id int 
# } 

# enum tasks_types {
#   single_task
#   daily_routine
#   long_term_goal
# }

class tasks(models.Model):
    tasks_types = (
        ('single_task', 'Single Task'),
        ('daily_routine', 'Daily Routine'),
        ('long_term_goal', 'Long Term Goal'),
    )
    tasks_types = models.CharField(max_length=255, choices=tasks_types, default='single_task')
    date = models.DateTimeField(default=now)
    activity_id = models.ForeignKey(activities, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    business_value = models.IntegerField(null=True)
    completion_status_id = models.ForeignKey(completion_statuses, on_delete=models.CASCADE)
    completed_by_contibutor_id = models.ForeignKey(contributors, on_delete=models.CASCADE, null=True)
    client_id = models.ForeignKey(clients, on_delete=models.CASCADE, null=True)
    project_id = models.ForeignKey(projects, on_delete=models.CASCADE, null=True)
    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tasks_types + " - " + self.name
    
    class Meta:
        verbose_name_plural = "Tasks"
        verbose_name = "Task"

# Table plans as p {
#   name varchar
#   id int [pk, increment]
#   period_start datetime
#   period_end datetime
#   status bit 
#   creation_date datetime
#   created_by_user_id int 
# }

class plans(models.Model):
    name = models.CharField(max_length=255)
    period_start = models.DateTimeField(default=now)
    period_end = models.DateTimeField(default=now, null=True)
    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Plans"
        verbose_name = "Plan"


# Table plans_tasks as tp {
#   id int [pk, increment]
#   task_id int 
#   plan_id int
#   priority_id int
#   assigned_to_contributor_id int 
#   completion_status_id int
#   retro_remarks varchar
#   creation_date datetime
#   created_by_user_id int 
# }

class plans_tasks(models.Model):
    task_id = models.ForeignKey(tasks, on_delete=models.CASCADE)
    plan_id = models.ForeignKey(plans, on_delete=models.CASCADE)
    priority_id = models.ForeignKey(priorities, on_delete=models.CASCADE)
    assigned_to_contributor_id = models.ForeignKey(contributors, on_delete=models.CASCADE, null=True)
    completion_status_id = models.ForeignKey(completion_statuses, on_delete=models.CASCADE, null=True)
    retro_remarks = models.CharField(max_length=255, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task_id + " - " + self.plan_id + " - " + self.priority_id + " - " + self.assigned_to_contributor_id + " - " + self.completion_status_id + " - "
    
    class Meta:
        verbose_name_plural = "Plans Tasks"
        verbose_name = "Task Log"


# Table point_types as pt {
#   id int [pk, increment]
#   name varchar
#   description varchar
#   sort_id int 
#   status bit 
#   creation_date datetime
#   created_by_user_id int  
# }

class point_types(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    sort_id = models.IntegerField()
    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name_plural = "Point Types"
        verbose_name = "Point Type"


# Table meetings as m {
#   id int [pk, increment]
#   client_id int 
#   project_id int 
#   start_date datetime
#   end_date datetime
#   title varchar
#   status bit 
#   creation_date datetime
#   created_by_user_id int  
# }

class meetings(models.Model):
    client_id = models.ForeignKey(clients, on_delete=models.CASCADE, null=True)
    project_id = models.ForeignKey(projects, on_delete=models.CASCADE, null=True)
    start_date = models.DateTimeField(default=now, null=True)
    end_date = models.DateTimeField(default=now, null=True)
    title = models.CharField(max_length=255 , default="Catch up")
    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.client_id) + " - " + str(self.project_id) + " - " + self.title
    
    class Meta:
        verbose_name_plural = "Meetings"
        verbose_name = "Meeting"


# Table meetings_attendees as ma {
#   id int [pk, increment]
#   contributor_id int 
#   meeting_id int 
#   status bit 
#   creation_date datetime
#   created_by_user_id int  
# }

class meetings_attendees(models.Model):
    contributor_id = models.ForeignKey(contributors, on_delete=models.CASCADE, null=True)
    meeting_id = models.ForeignKey(meetings, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.contributor_id) + " - " + str(self.meeting_id) 
    
    class Meta:
        verbose_name_plural = "Meetings Attendees"
        verbose_name = "Meeting Attendee"




# Table meetings_points as mp {
#   id int [pk, increment]
#   meeting_id int 
#   description varchar
#   related_contributor_id int 
#   point_type points_types
#   status bit 
#   creation_date datetime
#   created_by_user_id int  
# }

class meetings_points(models.Model):
    meeting_id = models.ForeignKey(meetings, on_delete=models.CASCADE)
    description = models.CharField(max_length=1024)
    related_contributor_id = models.ForeignKey(contributors, on_delete=models.CASCADE, null=True, blank=True)
    point_type = models.ForeignKey(point_types, on_delete=models.CASCADE)
    priority_id = models.ForeignKey(priorities, on_delete=models.CASCADE, null=True, blank=True)
    point_score = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.meeting_id) + " - " + self.description + " - " + str(self.related_contributor_id) + " - " + str(self.point_type) + " - "
    
    class Meta:
        verbose_name_plural = "Meetings Points"
        verbose_name = "Meeting Point"


# Table contributors_performance_scores as cs {
#   id int [pk, increment]
#   contributor_id int 
#   date datetime 
#   activity_id int 
#   remarks varchar
#   score float
#   status bit 
#   creation_date datetime
#   created_by_user_id int  
# }

class contributors_performance_scores(models.Model):
    contributor_id = models.ForeignKey(contributors, on_delete=models.CASCADE)
    date = models.DateTimeField(default=now)
    activity_id = models.ForeignKey(activities, on_delete=models.CASCADE)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    score = models.FloatField()
    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.contributor_id) + " - " + self.remarks + " = " + str(self.score)
    
    class Meta:
        verbose_name_plural = "Performance Scores"
        verbose_name = "Performance Score"