from django.http import HttpRequest
from django.shortcuts import render
from .models import Broduct
from django.db.models import Q
from math import ceil
from re import findall


# Create your views here.

# TODO: sort out the hat;
# TODO: add cart and checkout page;
# TODO: fix bug when searching a;
# TODO: fix sidebar, add roll-down there;
# TODO: fix header;


def paginated(typeofproduct, request_pag, passed_count=None):
    total_q = typeofproduct.count()
    current_address = HttpRequest.get_full_path(request_pag)

    try:
        name_current = findall(r"(?<=/)([a-z]+)(?=/)", current_address)[0]
    except:
        name_current = 'broducts'

    try:
        page_current = int(findall(r"(?<=/)(\d)(?=/)", current_address)[0])
    except:
        page_current = 1

    has_next, has_previous = False, False
    first_item = (page_current - 1) * 9
    last_item = first_item + 9
    if page_current > 1:
        has_previous = True

    if total_q > last_item:
        broducts = typeofproduct[first_item:last_item]
        has_next = True
    elif total_q == last_item:
        broducts = typeofproduct[first_item:last_item]
    else:
        broducts = typeofproduct[first_item:]

    if not passed_count:
        number_of_pages = range(1, ceil(total_q / 9) + 1)
    else:
        number_of_pages = range(1, passed_count)

    return {'products': broducts,
            'has_previous': has_previous,
            'has_next': has_next,
            'page_current': page_current,
            'page_next': str(page_current + 1),
            'page_previous': str(page_current - 1),
            'number_of_pages': number_of_pages,
            'last_item': last_item,
            'name_current': name_current}


def broducts_view(request):
    typeofproduct = Broduct.objects.all().order_by('name')
    return render(request, 'index.html', paginated(typeofproduct, request))


def searchbar_view(request):
    q = request.GET.get('q')
    search_result = Broduct.objects.filter(Q(name__icontains=q))
    search_counted = search_result.count()
    a = paginated(search_result, request, passed_count=ceil(search_counted / 9))
    a['q'] = q
    return render(request, 'search.html', a)


def froots_view(request):
    typeofproduct = Broduct.objects.filter(category=0)
    return render(request, 'froots.html', paginated(typeofproduct, request))


def tools_view(request):
    typeofproduct = Broduct.objects.filter(category=1)
    return render(request, 'tools.html', paginated(typeofproduct, request))


def new_view(request):
    typeofproduct = Broduct.objects.filter(category=2)
    return render(request, 'new.html', {'products': typeofproduct})


def contacts_view(request):
    return render(request, 'contacts.html')
