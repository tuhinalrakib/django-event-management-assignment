from django.shortcuts import render, redirect, get_object_or_404
from events.models import Category, Event
from events.forms import CategoryForm, EventForm, Participant, ParticipantForm

# CRUD Operations for Category
def category_list_create(request):
    categories = Category.objects.all();
    form = CategoryForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("category_list")
    
    return render(request, "category_list.html",{
        "categories" : categories,
        "form" : form
    })

def category_update(request, id):
    category = get_object_or_404(Category, id = id)
    form = CategoryForm(request.POST or None, instance=category)

    if form.is_valid():
        form.save()
        return redirect("category_list")
    
    return render(request, "category_form.html", {
        "form" : form
    })

def category_delete(request, id):
    category = get_object_or_404(Category, id = id)

    if request.method == "POST":
        category.delete()
        return redirect("category_list")

    return render(request, "confirm_delete.html", {
        "object" : category
    })

# CRUD Operations for Events
def event_list(request):
    events = Event.objects.select_related("category")
    
    return render(request, "events_list.html", {
        "events": events
    })

def event_create(request):
    form = EventForm(request.POST)
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("events_list")
    
    return render(request, "create_event.html", {
        "form": form
    })

def event_update(request, id):
    event = get_object_or_404(Event, id=id)
    form = EventForm(request.POST or None, instance=event)

    if form.is_valid():
        form.save()
        return redirect("event_list")

    return render(request, "event_form.html", {"form": form})

def event_delete(request, id):
    event = get_object_or_404(Event, id=id)

    if request.method == "POST":
        event.delete()
        return redirect("event_list")

    return render(request, "confirm_delete.html", {"object": event})

def participant_list_create(request):
    participants = Participant.objects.prefetch_related("events").all()
    form = ParticipantForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("participants_list")

    return render(request, "participants_list.html", {
        "participants": participants,
        "form": form
    })

def participant_update(request, id):
    participant = get_object_or_404(Participant, id=id)
    form = ParticipantForm(request.POST or None, instance=participant)

    if form.is_valid():
        form.save()
        return redirect("participant_list")

    return render(request, "participant_form.html", {"form": form})

def participant_delete(request, id):
    participant = get_object_or_404(Participant, id=id)

    if request.method == "POST":
        participant.delete()
        return redirect("participant_list")

    return render(request, "confirm_delete.html", {"object": participant})

def manager_dashboard(request):
    return render(request, "dashboard/manager_dashboard.html")