from django.urls import path
from events.views import category_list_create, event_list, participant_list_create, category_delete, category_update, event_update, event_delete, participant_update, participant_delete, manager_dashboard,event_create

urlpatterns = [
    path("manager-dashboard/", manager_dashboard, name="manager-dashboard"),
    
    path("categories/", category_list_create, name= "category_list"),
    path("categories/update/<int:id>/", category_update, name="category_update"),
    path("categories/delete/<int:id>/", category_delete, name="category_delete"),
    
    path("create-event/", event_create, name="create-event"),
    path("events/", event_list, name="events_list"),
    path("events/update/<int:id>/", event_update),
    path("events/delete/<int:id>/", event_delete),
    
    path("participants/", participant_list_create, name= "participants_list"),
    path("participants/update/<int:id>/", participant_update, name="participant-update"),
    path("participants/delete/<int:id>/", participant_delete, name="participant-delete"),
] 
