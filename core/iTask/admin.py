from django.contrib import admin
from .models import contributors, clients, projects, activities, completion_statuses, priorities, tasks, plans, plans_tasks, point_types, meetings, meetings_attendees, meetings_points, contributors_performance_scores

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

admin.site.register(tasks,
    list_display=['id', 'tasks_types', 'date', 'activity_id', 'name', 'business_value', 'completion_status_id', 'completed_by_contibutor_id', 'client_id', 'project_id', 'status', 'creation_date', 'last_update_date'],
    list_display_links=['id', 'tasks_types', 'date', 'activity_id', 'name', 'business_value', 'completion_status_id', 'completed_by_contibutor_id', 'client_id', 'project_id', 'status', 'creation_date', 'last_update_date'],
    list_filter=['tasks_types', 'date', 'activity_id', 'completion_status_id', 'completed_by_contibutor_id', 'client_id', 'project_id', 'status', 'creation_date', 'last_update_date'],
    search_fields=['name'],
    ordering=['id']
)


# class tasks_inline(admin.TabularInline):
#     model = tasks


# class plans_admin(admin.ModelAdmin):
#     inlines = [tasks_inline]

admin.site.register(plans, 
    list_display=['id', 'name', 'period_start', 'period_end', 'status', 'creation_date', 'last_update_date'],
    list_display_links=['id', 'name', 'period_start', 'period_end', 'status', 'creation_date', 'last_update_date'],
    list_filter=['status', 'creation_date', 'last_update_date'],
    search_fields=['name'],
    ordering=['period_start']
)


admin.site.register(plans_tasks,
    list_display=['id', 'task_id', 'plan_id', 'priority_id', 'assigned_to_contributor_id', 'completion_status_id', 'retro_remarks', 'creation_date', 'last_update_date'],
    list_display_links=['id', 'task_id', 'plan_id', 'priority_id', 'assigned_to_contributor_id', 'completion_status_id', 'retro_remarks', 'creation_date', 'last_update_date'],
    list_filter=['task_id', 'plan_id', 'priority_id', 'assigned_to_contributor_id', 'completion_status_id', 'creation_date', 'last_update_date'],
    search_fields=['retro_remarks'],
    ordering=['plan_id', 'task_id', 'id']
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

admin.site.register(meetings, meeting_header, 
    list_display=['id', 'client_id', 'project_id', 'start_date', 'end_date', 'title', 'status', 'creation_date', 'last_update_date'],
    list_display_links=['id', 'client_id', 'project_id', 'start_date', 'end_date', 'title', 'status', 'creation_date', 'last_update_date'],
    list_filter=['clisent_id', 'project_id', 'start_date', 'end_date', 'status', 'creation_date', 'last_update_date'],
    search_fields=['title'],
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
    list_display=['id', 'meeting_id', 'description', 'related_contributor_id', 'point_type', 'status', 'creation_date', 'last_update_date'],
    list_display_links=['id', 'meeting_id', 'description', 'related_contributor_id', 'point_type', 'status', 'creation_date', 'last_update_date'],
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
