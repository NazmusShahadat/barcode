from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import *
from django.views.decorators.csrf import csrf_exempt
import barcode
from barcode.writer import ImageWriter
from barcode import Code128
from pyzbar.pyzbar import decode
from PIL import Image
from pdf417 import encode, render_image, render_svg

# Create your views here.


def showlist(request):
    if request.method == "POST":
        brand = request.POST['brand']
        category = request.POST['category']
        model = request.POST['model']
        type = request.POST['type']
        size = request.POST['size']      
        b_id = '00' + brand
        b = (b_id[-2:])
        print(b)
        c_id = '000' + category
        c = (c_id[-3:])
        print(c)
        m_id = '00' + model
        m = (m_id[-2:])
        print(m)
        t_id = '000' + type
        t = (t_id[-3:])
        print(t)
        s_id = '000' + size
        s = (s_id[-2:])
        print(s)
        out = b + c + m + t + s 
        """ print(out) """
        """ a = barcode.get_barcode_class('code128')
        b = a(out, writer=ImageWriter())
        c = b.save('filename') """
        EAN = barcode.get_barcode_class('ean13')
        ean = EAN(f'{b}{c}{m}{t}{s}', writer=ImageWriter())
        d = ean.save('bar')

        img = Image.open('bar.png')
        result = decode(img)
        for i in result:
            num = []
            print(i.data.decode("utf-8"))
            num.append(i.data.decode("utf-8"))

        string = (num[0])
        print(string)
        brand_match = int(string[0:2])
        category_match = int(string[2:5])
        model_match = int(string[5:7])
        type_match = int(string[7:10])
        size_match = int(string[10:12])
        print(brand_match)
        print(category_match)
        print(model_match)
        print(type_match)
        print(size_match) 
        br = Brand.objects.get(pk=brand_match)
        print(br.brand)
        ca = Category.objects.get(pk=category_match)
        print(ca.category)
        mo = Model.objects.get(pk=model_match)
        print(mo.model)
        ty = Type.objects.get(pk=type_match)
        print(ty.type)
        si = Size.objects.get(pk=size_match)
        print(si.size)

        
        """ buffer = BytesIO()
        ean.write(buffer)
        self.barcode.save('bar.png', File(buffer), save=False) """
        return redirect('showlist')
        return render(request, 'templates/home.html')
        return brand, category, model, type, size
 
    results = Brand.objects.all()
    category = Category.objects.all()
    model = Model.objects.all()
    type = Type.objects.all()
    size = Size.objects.all()
    context = {'results':results, 'category':category, 'model':model, 'type':type, 'size':size}
    return render(request, 'templates/home.html', context)

    """ def readlist(request):
        img = Image.open('barcode.png'
        result = decode(img)
        print(result)
        for i in result:
            print(i.data.decode("utf-8")) """
    
    """ s1 = 0
    s2 = 10

    def createlist(s1, s2):
        return [item for item in range(s1, s2)]
    results = ((createlist(s1, s2)))
    results = [str(i) for i in results]
    for item in results:
        codes = encode(str(item), columns=3, security_level=2)
        image = render_image(codes, scale=5, ratio=2, padding=5, fg_color="Indigo", bg_color="#ddd")  # Pillow Image object
        image.save('barcode.jpg') """

    