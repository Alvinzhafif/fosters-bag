from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

def show_main(request):

    products = Product.objects.all()

    context = {
        'name': 'Alvin Zhafif Afilla',
        'class': 'PBP KKI',
        'general': 'This is a project that is under work, this will be an rpg-themed inventory management project',
        'lore': 'Foster is a merchant in the city of sorus, he is known to be the best trader in the city with never before seen items and weapons.However, currently he has problems with managing his inventory and needs your help',
        'status': 'here is one of his most priced item',
        'weapon': 'Blade of the damned',
        'weapon_desc': 'a weapon found in the edge of the underworld',
        'amount' : '1',
        'products': products,
    }

    return render(request, 'main.html', context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.all()

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")




# Create your views here.
