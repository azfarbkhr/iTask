from urllib import response
from django.contrib import admin
from .models import contributors, clients, projects, activities, completion_statuses, priorities, tasks, point_types, meetings, meetings_attendees, meetings_points, contributors_performance_scores
from datetime import datetime
from django.http import HttpResponse

admin.site.site_header = 'iTask Administration'
admin.site.site_title = 'iTask Administration'
admin.site.index_title = 'iTask Administration'
admin.site.site_url = None

admin.site.register(contributors, 
    list_display=['id', 'full_name', 'short_name', 'email_address', 'status', 'creation_date', 'last_update_date'], 
    list_display_links=['id', 'full_name', 'short_name', 'email_address', 'status', 'creation_date', 'last_update_date'],
    list_filter=['status', 'creation_date', 'last_update_date'],
    search_fields=['full_name', 'short_name', 'email_address'],
    ordering=['id']
)

admin.site.register(clients,
    list_display=['id', 'name', 'owner_contributor_id', 'status', 'creation_date', 'last_update_date'],
    list_display_links=['id', 'name', 'owner_contributor_id', 'status', 'creation_date', 'last_update_date'],
    list_filter=['status', 'creation_date', 'last_update_date'],
    search_fields=['name'],
    ordering=['id']
)

admin.site.register(projects,
    list_display=['id', 'name', 'focal_person_contributor_id', 'client_id', 'status', 'creation_date', 'last_update_date'],
    list_display_links=['id', 'name', 'focal_person_contributor_id', 'client_id', 'status', 'creation_date', 'last_update_date'],
    list_filter=['status', 'creation_date', 'last_update_date'],
    search_fields=['name'],
    ordering=['id']
)

admin.site.register(activities,
    list_display=['id', 'name', 'short_name', 'status', 'creation_date', 'last_update_date'],
    list_display_links=['id', 'name', 'short_name', 'status', 'creation_date', 'last_update_date'],
    list_filter=['status', 'creation_date', 'last_update_date'],
    search_fields=['name', 'short_name'],
    ordering=['id']
)

admin.site.register(completion_statuses,
    list_display=['id', 'name', 'status', 'creation_date', 'last_update_date'],
    list_display_links=['id', 'name', 'status', 'creation_date', 'last_update_date'],
    list_filter=['status', 'creation_date', 'last_update_date'],
    search_fields=['name'],
    ordering=['sort_id']
)

admin.site.register(priorities,
    list_display=['id', 'name', 'status', 'creation_date', 'last_update_date'],
    list_display_links=['id', 'name', 'status', 'creation_date', 'last_update_date'],
    list_filter=['status', 'creation_date', 'last_update_date'],
    search_fields=['name'],
    ordering=['sort_id']
)

class TasksAdmin(admin.ModelAdmin):
    readonly_fields = ('creation_date', 'last_update_date', 'id')
    fieldsets = (
        (None, {
            'fields': ('id',( 'tasks_types', 'completion_status_id'), ('name', 'assigned_to_contributor_id'), )
        }), 
        ('Important Dates', {
            'fields': (('date', 'creation_date', 'last_update_date'),)
        }),
        ('Planning', {
            'fields': (('activity_id', 'priority_id', 'business_value'), ('client_id', 'project_id'))

        }),
        ('Completion Fields', {
            'fields': (('completed_by_contibutor_id', 'completed_date', 'retro_remarks'), )
        })
    )
    

@admin.action(description='Mark selected tasks as completed')
def mark_completed(modeladmin, request, queryset):
    queryset.update(completion_status_id=5, completed_by_contibutor_id=1, completed_date=datetime.now())


@admin.action(description="Mark selected tasks for today")
def mark_today(modeladmin, request, queryset):
    queryset.update(date=datetime.now())


admin.site.register(tasks,TasksAdmin, 
    list_display=['date', 'priority_id', 'name', 'completion_status_id','completed_date', 'project_id'],
    list_display_links=['priority_id', 'name','completion_status_id','completed_date', 'project_id'],
    list_editable=['date'],
    list_filter=['date', 'priority_id', 'completion_status_id', 'client_id', 'completed_date'],
    search_fields=['name'],
    actions = [mark_completed, mark_today],
    ordering=['id']
)

admin.site.register(point_types,
    list_display=['id', 'name', 'description', 'sort_id', 'status', 'creation_date', 'last_update_date'],
    list_display_links=['id', 'name', 'description', 'sort_id', 'status', 'creation_date', 'last_update_date'],
    list_filter=['status', 'creation_date', 'last_update_date'],
    search_fields=['name'],
    ordering=['sort_id']
)

class meeting_attendees_inline(admin.TabularInline):
    model = meetings_attendees

class meeting_points_inline(admin.TabularInline):
    model = meetings_points

class meeting_header(admin.ModelAdmin):
    inlines = [
        meeting_attendees_inline,
        meeting_points_inline
    ]

@admin.action(description='Download minutes for selected meetings')
def download_minutes(modeladmin, request, queryset):

    minutes_txt = ""
    for meeting in queryset:
        
        attendees = ""
        for attendee in meeting.meetings_attendees_set.all().values('contributor_id__full_name'):
            attendees += attendee['contributor_id__full_name'] + ", "
        
        points = ""
        for point in meeting.meetings_points_set.all().values('point_type_id__name', 'related_contributor_id__full_name', 'description'):
            points += (point['point_type_id__name'] or "") + \
                            " - " + (point['related_contributor_id__full_name'] or "") + " - " + \
                                point['description'] + "\n\t\t"


        minute_txt = f"""
        {"#" * 10}
        Meeting Title: {meeting.title}
        Start Time: {meeting.start_date}
        End Time: {meeting.end_date}
        Meeting Attendees:
        - {attendees}

        Meeting Points:
        {points}
        {"#" * 10}
        """
        minutes_txt += minute_txt
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="minutes.txt"'
    response.write(minutes_txt)
    return response



admin.site.register(meetings, meeting_header, 
    list_display=['id', 'title', 'start_date','project_id', ],
    list_display_links=['id', 'title', 'start_date','project_id', ],
    list_filter=['client_id', 'project_id', 'start_date', 'end_date', 'status', 'creation_date', 'last_update_date'],
    search_fields=['title'],
    actions = [download_minutes],
    ordering=['start_date']
)

admin.site.register(meetings_attendees,
    list_display=['id', 'contributor_id', 'meeting_id', 'status', 'creation_date', 'last_update_date'],
    list_display_links=['id', 'contributor_id', 'meeting_id', 'status', 'creation_date', 'last_update_date'],
    list_filter=['contributor_id', 'meeting_id', 'status', 'creation_date', 'last_update_date'],
    search_fields=['meeting_id'],
    ordering=['meeting_id']
)


admin.site.register(meetings_points,
    list_display=['id', 'meeting_id', 'description', 'related_contributor_id', 'point_type', ],
    list_display_links=['id', 'meeting_id', 'description', 'related_contributor_id', 'point_type',],
    list_filter=['meeting_id', 'point_type', 'status', 'creation_date', 'last_update_date'],
    search_fields=['description'],
    ordering=['meeting_id', 'id']
)

admin.site.register(contributors_performance_scores,
    list_display=['id', 'contributor_id', 'date', 'activity_id', 'remarks', 'score', 'status', 'creation_date', 'last_update_date'],
    list_display_links=['id', 'contributor_id', 'date', 'activity_id', 'remarks', 'score', 'status', 'creation_date', 'last_update_date'],
    list_filter=['contributor_id', 'date', 'activity_id', 'status', 'creation_date', 'last_update_date'],
    search_fields=['remarks'],
    ordering=['contributor_id', 'date']
)
