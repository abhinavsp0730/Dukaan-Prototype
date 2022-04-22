from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import UpdateView, ListView
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse_lazy
from distutils.util import strtobool
from .forms import NewProductForm, BuyProductForm, UpdateForm
from .models import Product, Order
from django.contrib.auth.models import User as mu
from django.views.decorators.csrf import csrf_exempt
from cacheops import cached_view


@login_required
def new_product(request):
    """ 
    save new products to Product model. 
    """
    if request.method == 'POST':
        try:
            form = NewProductForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                new_prod = Product.objects.create(**data, User=request.user
                )
            domain =  request.build_absolute_uri('/')[:-1]
            order.invalidate(domain+"/order/{}".format(request.user.username), usr= request.user.username)
            return HttpResponseRedirect(reverse_lazy('yc'))
        except:
            form = NewProductForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                new_prod = Product.objects.create(**data, User=request.user
                )
            return HttpResponseRedirect(reverse_lazy('yc'))

    else:
        form = NewProductForm()
        return render(request, 'new_product.html', {'form': form})

@login_required
def yc(request):
    """
    returns filtered Product instance based on partiular user
    """
    products = Product.objects.filter(User=request.user)
    return render(request, 'your_products.html', {'products': products}) 


@cached_view(timeout=60*15)
@csrf_exempt
def order(request, usr):
    """
    generates form for placing order and saving them in Order models
    via user's unique link.
    """
    model_user =  mu.objects.get(username=usr)
    choices = [(i.name, "Product Name: {} \n MRP: {} \n  Discounted Price: {} \n Description: {}".format(i.name, i.mrp, i.discounted_price, i.details)) for i in Product.objects.filter(User=model_user).filter(available=True)]
    if request.method == 'POST':
        form = BuyProductForm(request.POST, choices=choices)
                     
        if form.is_valid():
            data = form.cleaned_data 
            qty = data['qty']
            user_name = data['user_name']
            adress = data['adress']
            mobile = data['mobile']
            name_product = Product.objects.get(name=data['name'])
            new_prod = Order.objects.create(product_name=name_product, name=data['name'], price= name_product.discounted_price,  qty=qty, 
            user_name=user_name, mob=mobile, adress=adress, user= model_user)
        return HttpResponse("Your Product has been placed succefully")
    else:
        form = BuyProductForm(choices=choices)
        return render(request, 'order.html', {'form': form})


@login_required
def yord(request):
    """
    display placed orders for particular user.
    """
    products = Order.objects.filter(user=request.user)
    return render(request, 'yord.html', {'products': products}) 

@login_required 
def available(request, pk, avail):
    """
    changes "avaliable" boolen field of the instance of a Product model.
    """
    pk = int(pk)
    avail = strtobool(avail)
    try:
        if avail:
            Product.objects.filter(id = pk).update(available = True)
        else:
            Product.objects.filter(id = pk).update(available = False)
        domain =  request.build_absolute_uri('/')[:-1]
        order.invalidate(domain+"/order/{}".format(request.user.username), usr= request.user.username)
        return HttpResponseRedirect(reverse_lazy('yc'))
    except:
        if avail:
            Product.objects.filter(id = pk).update(available = True)
        else:
            Product.objects.filter(id = pk).update(available = False)
        return HttpResponseRedirect(reverse_lazy('yc'))


@login_required
def update(request, id):
    """
    update the fields of a particular Product.
    """
    instance = get_object_or_404(Product, id=id)
    form = UpdateForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponse("Succefully Updated")
    return render(request, 'update.html', {'form': form})
