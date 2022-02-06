from django.db import models
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.dispatch import receiver

# core
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

class priorities(models.Model):
    name = models.CharField(max_length=255)
    sort_id = models.IntegerField()
    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Priorities"
        verbose_name = "Priority"

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

# tasks
class tasks(models.Model):
    tasks_types = (
        ('single_task', 'Single Task'),
        ('daily_routine', 'Daily Routine'),
        ('long_term_goal', 'Long Term Goal'),
    )
    tasks_types = models.CharField(max_length=255, choices=tasks_types, default='single_task')
    date = models.DateTimeField(default=now)
    activity_id = models.ForeignKey(activities, on_delete=models.CASCADE, null=True, blank=True)
    priority_id = models.ForeignKey(priorities, on_delete=models.CASCADE)
    assigned_to_contributor_id = models.ForeignKey(contributors, on_delete=models.CASCADE, null=True, blank=True, related_name='assigned_to_contributor_id')
    name = models.CharField(max_length=255)
    business_value = models.IntegerField(null=True, blank=True)
    completion_status_id = models.ForeignKey(completion_statuses, on_delete=models.CASCADE)
    completed_by_contibutor_id = models.ForeignKey(contributors, on_delete=models.CASCADE, null=True, blank=True, related_name='completed_by_contibutor_id')
    completed_date = models.DateTimeField(null=True, blank=True)
    retro_remarks = models.CharField(max_length=255, null=True, blank=True)
    client_id = models.ForeignKey(clients, on_delete=models.CASCADE, null=True, blank=True)
    project_id = models.ForeignKey(projects, on_delete=models.CASCADE, null=True, blank=True)
    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tasks_types + " - " + self.name
    
    class Meta:
        verbose_name_plural = "Tasks"
        verbose_name = "Task"

# meetings
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

# performance
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