from copy import deepcopy
import operator
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from travel.models import Travel
from travel.forms import OrderForm
from functools import reduce


def travel_view(request, pk):
    try:
        travel = Travel.objects.get(pk=int(pk))
    except Travel.DoesNotExist:
        return redirect("home")

    context = {"pk": pk, "travel": travel}
    return render(request, "travel_view.html", context)


def home_view(request):
    context = {}
    travel = Travel.objects.filter(promoted=True)
    travels = Travel.objects.all()
    active_travel = Travel.objects.all()[0:2]
    inactive_travels = travel[3:len(travel) - 1]
    print(travel)
    context["main_travel"] = travel.first()
    context["travels"] = Travel.objects.filter(promoted=False)
    return render(request, "home_new.html", context)


def order_view(request, pk):
    context = {}
    context["order_form"] = OrderForm()
    try:
        context["data"] = Travel.objects.get(pk=pk)
    except Travel.DoesNotExist:
        return redirect("home")

    if request.POST:

        post = deepcopy(request.POST)
        post["travel"] = Travel.objects.get(pk=pk)
        post["price"] = str(
            Travel.objects.get(pk=pk).price_adult * int(request.POST.get("adult_count")) + Travel.objects.get(
                pk=pk).price_child * int(request.POST.get("children_count")))
        form = OrderForm(post)
        if int(post["adult_count"]) <= Travel.objects.get(pk=pk).number_places_adults and int(
                post["children_count"]) <= Travel.objects.get(pk=pk).number_places_children:
            travel = Travel.objects.get(pk=pk)
            travel.number_places_adults -= int(post["adult_count"])
            travel.number_places_children -= int(post["children_count"])

            if form.is_valid():
                form.save()
                travel.save()
                messages.success(request, 'Successfully Booked!')
                return redirect("home")
            else:
                messages.error(request, "Cant create order please enter valid data")
        else:
            messages.error(request, "Too many adults or children")
        context["order_form"] = form

    return render(request, "order.html", context)


def search_view(request):
    context = {}
    if request.GET.get("query"):
        context["query"] = Travel.objects.filter(Q(name__icontains=request.GET.get("query")))
        return render(request, "search.html", context)
    elif request.GET:
        q = []

        if request.GET.get("origin"):
            q.append(Q(city_from__name__icontains=request.GET.get("origin")) |
                     Q(airport_from__name__icontains=request.GET.get("origin")) |
                     Q(city_from__country__name__icontains=request.GET.get("origin")) |
                     Q(city_from__country__continent__name__icontains=request.GET.get("origin")))
        if request.GET.get("destination"):
            q.append(Q(city_to__country__continent__name__icontains=request.GET.get("destination")) |
                     Q(city_to__country__name__icontains=request.GET.get("destination")) |
                     Q(airport_from__name__icontains=request.GET.get("destination")) |
                     Q(city_to__name__icontains=request.GET.get("destination")), )
        if request.GET.get("departure_date"):
            dep_date = request.GET.get("departure_date").split("/")[2] + "-" + \
                       request.GET.get("departure_date").split("/")[0] + "-" + \
                       request.GET.get("departure_date").split("/")[1]
            q.append(Q(departure_date__icontains=dep_date))
        if request.GET.get("return_date"):
            ret_date = request.GET.get("return_date").split("/")[2] + "-" + request.GET.get("return_date").split("/")[
                0] + "-" + request.GET.get("return_date").split("/")[1]
            q.append(Q(return_date__icontains=ret_date),)
        if q != []:
            query = Travel.objects.filter(reduce(operator.or_, q))
        else:
            return redirect("search")
        types = []
        if request.GET.get("bb") == "on":
            types.append(1)
        if request.GET.get("hb") == "on":
            types.append(2)
        if request.GET.get("fb") == "on":
            types.append(3)
        if request.GET.get("ai") == "on":
            types.append(4)
        if len(types) > 0:
            context["query"] = query.filter(type__in=types)
        else:
            context["query"] = query.filter
        return render(request, "search.html", context)
    if request.GET.get("query"):
        context["query"] = Travel.objects.filter(Q(name__icontains=request.GET.get("query")))
        return render(request, "search.html", context)
    else:
        return render(request, "search_filter.html")
##
