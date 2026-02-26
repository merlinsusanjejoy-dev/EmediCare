from django.shortcuts import render,redirect
from Pharmacy.models import *
from User.models import *
from django.db.models import Count
from django.db.models import Q
from datetime import datetime
from django.db.models import Sum
# Create your views here.
def pharmacyhomepage(request):
    if 'pid'  in request.session:
        return render(request,'Pharmacy/Pharmacyhomepage.html')
    else:
        return redirect('Guest:index')

def myprofile(request):
    pharmacy=tbl_pharmacy.objects.get(id=request.session["pid"])
    return render(request,'Pharmacy/Myprofile.html',{"pharmacy":pharmacy})
def editprofile(request):
    pharmacy=tbl_pharmacy.objects.get(id=request.session["pid"])
    if request.method=='POST':
        pharmacy.pharmacy_name=request.POST.get("txt_ename")
        pharmacy.pharmacy_email=request.POST.get("txt_mail")
        pharmacy.pharmacy_contact=request.POST.get("txt_contact")
        pharmacy.pharmacy_address=request.POST.get("txt_add")
        pharmacy.save()
        return redirect('Pharmacy:editprofile')
    else: 
        return render(request,'Pharmacy/Editprofile.html',{"pharmacy":pharmacy})

def changepassword(request):
    pharmacy=tbl_pharmacy.objects.get(id=request.session["pid"])
    dbpass=pharmacy.pharmacy_password
    if request.method=='POST':
        oldpassword=request.POST.get("txtopass")
        newpassword=request.POST.get("txtnepass")
        confirmpassword=request.POST.get("txtcpass")
        if oldpassword==dbpass:
            if newpassword==confirmpassword:
                pharmacy.pharmacy_password=newpassword
                pharmacy.save()
                return redirect('Pharmacy:changepassword')
            else:
                return render(request,'Pharmacy/Changepassword.html',{'msg':'valid'})
        else:
            return render(request,'Pharmacy/Changepassword.html',{'msg':'invalid'})
    else:
        return render(request,'Pharmacy/Changepassword.html',{"pharmacy":pharmacy})
def medicine(request):
    medicine = tbl_medicine.objects.filter(Pharmacy=request.session['pid'])
    category=tbl_category.objects.all()
    for i in medicine:
        total_stock = tbl_stock.objects.filter(medicine=i.id).aggregate(total=Sum('stock_count'))['total']
        total_cart = tbl_cart.objects.filter(medicine_id=i.id,cart_status=1).aggregate(total=Sum('cart_qty'))['total']
        # print(total_stock)
        # print(total_cart)
        if total_stock is None:
            total_stock = 0
        if total_cart is None:
            total_cart = 0
        total =  total_stock - total_cart
        i.total_stock = total
    if request.method == 'POST':

        tbl_medicine.objects.create(
            medicine_name=request.POST.get('txt_medicine'),
            medicine_photo=request.FILES.get('medicine_photo'),
            medicine_description=request.POST.get('txt_deatails'),
            category=tbl_category.objects.get(id=request.POST.get("txtcategory")),
            medicine_rate=request.POST.get('txt_rate'),
            Pharmacy=tbl_pharmacy.objects.get(id=request.session["pid"]),
            medicine_status=request.POST.get("rdo")  
        )
        return redirect('Pharmacy:medicine')  

    else:
        return render(request, 'Pharmacy/Medicine.html', {'medicine': medicine,'category': category,'id':id})

def deletemedicine(request,mid):
    tbl_medicine.objects.get(id=mid).delete()
    return redirect('Pharmacy:medicine')
#.............................edit ......................................
def editmedicine(request, mid):
    medic = tbl_medicine.objects.get(id=mid)
    category = tbl_category.objects.all()
    if request.method == "POST":
        if 'medicine_photo' in request.FILES:
            medic.medicine_photo = request.FILES['medicine_photo']        
        medic.medicine_name = request.POST.get('txt_medicine')
        medic.medicine_description = request.POST.get('txt_deatails')
        category_id = request.POST.get('txtcategory')
        medic.category_id = category_id
        medic.medicine_rate = request.POST.get('txt_rate')
        medic.save()
        return redirect('Pharmacy:medicine')
    else:
        return render(request, 'Pharmacy/Medicine.html', {
            'editmedic': medic,
            'category': category
        })

def addstock(request, id):
    stock = tbl_stock.objects.filter(medicine_id=id)  
    if request.method == 'POST':
        tbl_stock.objects.create(
            stock_count=request.POST.get('txt_stock'),
            medicine=tbl_medicine.objects.get(id=id), 
        )
        return redirect('Pharmacy:addstock', id=id)
    else:
        return render(request, 'Pharmacy/Addstock.html', {'stock': stock})




def viewuserbooking(request):
    Booking = tbl_booking.objects.filter(tbl_cart__medicine_id__Pharmacy_id=request.session["pid"],booking_status__gt=1).distinct().order_by('id')

    return render(request, 'Pharmacy/Viewuserbooking.html', {'Booking': Booking})



def packorder(request,id):
    bookingdata=tbl_booking.objects.get(id=id)
    bookingdata.booking_status=3
    bookingdata.save()
    return redirect('Pharmacy:viewuserbooking')




def viewusercart(request, id):
    Booking = tbl_cart.objects.filter(booking_id=id)  # Fetch cart items

    print("DEBUG: Cart Items ->", Booking)  # Print to check if data is retrieved

    return render(  request, 'Pharmacy/Viewusercart.html', {'cart': Booking})


def verified(request,id):
    bookingdata=tbl_booking.objects.get(id=id)
    bookingdata.booking_status=7
    bookingdata.save()
    return redirect('Pharmacy:viewuserbooking')


def chat(request, id):
    user= tbl_user.objects.get(id=id)
    return render(request,"Pharmacy/Chat.html",{"user":user})

def ajaxchat(request):
    from_pharmacy = tbl_pharmacy.objects.get(id=request.session["pid"])
    to_user = tbl_user.objects.get(id=request.POST.get("tid"))
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),pharmacy_from=from_pharmacy,user_to=to_user,chat_file=request.FILES.get("file"))
    return render(request,"Pharmacy/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    pharmacy = tbl_pharmacy.objects.get(id=request.session["pid"])
    chat_data = tbl_chat.objects.filter((Q(pharmacy_from=pharmacy) | Q(pharmacy_to=pharmacy)) & (Q(user_from=tid) | Q(user_to=tid))).order_by('chat_time')
    return render(request,"Pharmacy/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(pharmacy_from=request.session["pid"]) & Q(user_to=request.GET.get("tid")) | (Q(user_from=request.GET.get("tid")) & Q(pharmacy_to=request.session["pid"]))).delete()
    return JsonResponse({"msg":"Chat Deleted Sucessfully...."})


def logout(request):
    del request.session['pid']
    return redirect('Guest:index')
    
# def viewuserorder(request):
#     Booking = tbl_booking.objects.filter(tbl_cart__medicine_id__Pharmacy_id=request.session["pid"],booking_status__gt=1).distinct().order_by('id')

#     return render(request, 'Pharmacy/viewuserorder.html', {'Booking': Booking})

