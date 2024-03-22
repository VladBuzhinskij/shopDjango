from django.core.paginator import Paginator
from django.shortcuts import render
from products.models import Categories,SubCategories,Products
from products.utils import q_search
# Create your views here.




def assort (request ,category_slug=0,subcategory_slug=0):
    page=request.GET.get('page',1)
    order_by=request.GET.get('order_by',None)
    query=request.GET.get('q',None)
    slug_url='#'
    products=0
    if query:
        products=q_search(query)
    elif category_slug!='all':
        if subcategory_slug !=0:
            
            subcat_id=SubCategories.objects.filter(slug=subcategory_slug)
            products=Products.objects.filter (subcategory = subcat_id[0])
            slug_url=subcategory_slug
        else:
            cat_id=Categories.objects.filter(slug=category_slug)
            subcateg=SubCategories.objects.filter (category = cat_id[0])
            i=0
            for subcat in subcateg:
                if i==0:
                    products=Products.objects.filter (subcategory = subcat)
                else:
                    products=Products.objects.filter (subcategory = subcat)|products
                i=i+1
            slug_url=category_slug
    else: 
        products=Products.objects.all()
        slug_url=category_slug
    
    if products !=0:   
        if order_by and order_by !='None':
            products=products.order_by(order_by)
        paginator=Paginator(products,1)
        current_pag=paginator.page(int(page))
    else:
        current_pag=products
    current_page=current_pag
    categories=Categories.objects.all()
    subcategories=SubCategories.objects.all()
    
    
    
    # products=Products.objects.all()
    context={
        "title":"Home - Главная",
        "categories": categories,
        "subcategories":subcategories,
        "products":current_page,
        "category":category_slug,
        "subcategory":subcategory_slug,
        "slug_url":slug_url,
        "order_by":order_by
        
    }
    return render(request,'products/assort.html',context)


# def assortall (request,page=1):
#     products=Products.objects.all()
#     categories=Categories.objects.all()
#     subcategories=SubCategories.objects.all()

#     paginator=Paginator(products,1)
#     current_page=paginator.page(page)

#     context={
#         "title":"Home - Главная",
#         "categories": categories,
#         "subcategories":subcategories,
#         "products":current_page,
#     }
#     return render(request,'products/assort.html',context)


def product (request,product_slug):
    categories=Categories.objects.all()
    subcategories=SubCategories.objects.all()
    product_slug=Products.objects.get(slug=product_slug)
    context={
        "categories": categories,
        "subcategories":subcategories,
        'product': product_slug
    }
    return render(request,'products/product.html',context)
