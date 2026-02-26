from django.shortcuts import render,redirect
from Deliveryboy.models import *
from Guest.models import *
from Pharmacy.models import *
from User.models import *


# Create your views here.
def viewbooking(request):
    return render(request,'Deliveryboy/Viewbooking.html')

def myprofile(request):
    deliveryboy=tbl_deliveryboy.objects.get(id=request.session["dbid"])
    return render(request,'Deliveryboy/Myprofile.html',{"deliveryboy":deliveryboy})

def editprofile(request):
    deliveryboy=tbl_deliveryboy.objects.get(id=request.session["dbid"])
    if request.method=='POST':
        deliveryboy.deliveryboy_name=request.POST.get("txt_ename")
        deliveryboy.deliveryboy_email=request.POST.get("txt_mail")
        deliveryboy.deliveryboy_contact=request.POST.get("txt_contact")
        deliveryboy.deliveryboy_address=request.POST.get("txt_add")
        deliveryboy.save()
        return redirect('Deliveryboy:editprofile')
    else: 
        return render(request,'Deliveryboy/Editprofile.html',{"deliveryboy":deliveryboy})
def changepassword(request):
    return render(request,'Deliveryboy/Changepassword.html')

def changepassword(request):
    deliveryboy=tbl_deliveryboy.objects.get(id=request.session["dbid"])
    dbpass=deliveryboy.deliveryboy_password
    if request.method=='POST':
        oldpassword=request.POST.get("txtopass")
        newpassword=request.POST.get("txtnepass")
        confirmpassword=request.POST.get("txtcpass")
        if oldpassword==dbpass:
            if newpassword==confirmpassword:
                deliveryboy.deliveryboy_password=newpassword
                deliveryboy.save()
                return redirect('Deliveryboy:changepassword')
            else:
                return render(request,'Deliveryboy/Changepassword.html',{'msg':'valid'})
        else:
            return render(request,'Deliveryboy/Changepassword.html',{'msg':'invalid'})
    else:
        return render(request,'Deliveryboy/Changepassword.html',{"deliveryboy":deliveryboy})

def deliveryhomepage(request):
    if 'uid'  in request.session:  
        return render(request,'Deliveryboy/Deliveryhomepage.html')
    else:
        return redirect('Guest:index')

def viewbooking(request):
    db = tbl_deliveryboy.objects.get(id=request.session["dbid"])
    place = request.session['place']
    Booking = tbl_booking.objects.filter(booking_status__gte=3,booking_status__lt=4,user__place__district=db.place.district.id)
    return render(request, 'Deliveryboy/ViewBooking.html', {'Booking': Booking})


def viewcart(request,id):
    Booking = tbl_cart.objects.filter(booking_id=id) 
    return render(request, 'Deliveryboy/Viewcart.html', {'Booking': Booking})


def ordercollect(request,id):
    collectorder=tbl_booking.objects.get(id=id)
    collectorder.booking_status=4
    collectorder.deliveryboy=tbl_deliveryboy.objects.get(id=request.session['dbid'])
    collectorder.save()
    return redirect('Deliveryboy:viewbooking')


def delivered(request,id):
    collectorder=tbl_booking.objects.get(id=id)
    collectorder.booking_status=5
    collectorder.save()
    return redirect('Deliveryboy:myorder')


def myorder(request):
    Booking = tbl_booking.objects.filter(deliveryboy=request.session['dbid'])
    return render(request, 'Deliveryboy/Myorder.html', {'Booking': Booking})

def logout(request):
    del request.session['dbid']
    return redirect('Guest:index')