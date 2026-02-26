from django.shortcuts import render,redirect
from Administrator.models import *
from User.models import *
from Guest.models import *
from datetime import date
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Prefetch

from django.db.models import Sum, F, ExpressionWrapper, DecimalField
from dateutil import relativedelta
from datetime import datetime
from decimal import Decimal

from django.http import JsonResponse
from django.db.models.functions import TruncMonth
from django.db.models import Sum
from datetime import datetime
from collections import OrderedDict

# Create your views here.
def Adminregistration(request):
    admin=tbl_admin.objects.all()
    if request.method=='POST':
        tbl_admin.objects.create(admin_name=request.POST.get('txtname'),
                                 admin_email=request.POST.get('txtemail'),
                                 admin_password=request.POST.get('txtpass'),)
        return redirect('Admin:Adminregistration')
    else:
        return render(request,'Administrator/Adminregistration.html',{'admin':admin})

#...............................delete Admin.................................
def deleteadmin(request,aid):
    tbl_admin.objects.get(id=aid).delete()
    return redirect('Admin:Adminregistration')
#.............................edit Admin......................................
def editadmin(request,aid):
    adm=tbl_admin.objects.get(id=aid)
    if request.method=="POST":
        adm.admin_name=request.POST.get('txtname')
        adm.admin_contact=request.POST.get('txtcontact')
        adm.admin_email=request.POST.get('txtemail')
        adm.admin_password=request.POST.get('txtpass')
        adm.save()
        return redirect('Admin:Adminregistration')
    else:
         return render(request,'Administrator/Adminregistration.html',{'editadm':adm})
#district
def District(request):
    district=tbl_district.objects.all()
    if request.method=='POST':
        districtcount=tbl_district.objects.filter(district_name=request.POST.get('txtdis')).count()
        if districtcount > 0:
            return render(request,'Administrator/District.html',{'msg':"Already Exisit"})
        else:
            tbl_district.objects.create(district_name=request.POST.get('txtdis'),)
        return redirect('Admin:District')
    else:
        return render(request,'Administrator/District.html',{'district':district})
#...............................delete district.................................
def deletedistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect('Admin:District')
#.............................edit district......................................
def editdistrict(request,did):
    dist=tbl_district.objects.get(id=did)
    if request.method=="POST":
        dist.district_name=request.POST.get('txtdis')
        dist.save()
        return redirect('Admin:District')
    else:
         return render(request,'Administrator/District.html',{'editdis':dist})
# #=gory
def Category(request):
    category=tbl_category.objects.all()
    if request.method=='POST':
         categorycount=tbl_category.objects.filter(category_name=request.POST.get('txtcategory')).count()
         if categorycount > 0:
            return render(request,'Administrator/Category.html',{'msg':"Already Exisit"})
         else:
            tbl_category.objects.create(category_name=request.POST.get('txtcategory'),)
         return redirect('Admin:Category')
    else:
        return render(request,'Administrator/Category.html',{'category':category})
#...........................................delete category................................
def deletecategory(request,cid):
    tbl_category.objects.get(id=cid).delete()
    return redirect('Admin:Category')
#.............................edit category......................................
def editcategory(request,cid):
    cate=tbl_category.objects.get(id=cid)
    if request.method=="POST":
        cate.category_name=request.POST.get('txtcategory')
        cate.save()
        return redirect('Admin:Category')
    else:
         return render(request,'Administrator/Category.html',{'editcate':cate})

#.............................................place......................................
def place(request):
    district=tbl_district.objects.all()   
    place=tbl_place.objects.all()
    if request.method=='POST':
        placecount=tbl_place.objects.filter(place_name=request.POST.get('txtplace')).count()
        if placecount > 0:
            return render(request,'Administrator/Place.html',{'msg':"Already Exisit"})
        else:
            placename=request.POST.get("txtplace")
            district=tbl_district.objects.get(id=request.POST.get("dept"))
            tbl_place.objects.create(place_name=placename,district=district)
        return redirect('Admin:place')
    else: 
        return render(request,'Administrator/Place.html',{'district':district,'place':place})  
#.............................................Subcategory......................................
def subcategory(request):
    category=tbl_category.objects.all()
    subcategory=tbl_subcategory.objects.all()
    if request.method=='POST':
        subcategoryname=request.POST.get("txtsub")
        category=tbl_category.objects.get(id=request.POST.get("cate"))
        tbl_subcategory.objects.create(subcategory_name=subcategoryname,category=category)
        return redirect('Admin:subcategory')
    else: 
        return render(request,'Administrator/Subcategory.html',{'category':category,'subcategory':subcategory})
        #----------------------------------delete_place---------------
def deleteplace(request,pid):
    tbl_place.objects.filter(id=pid).delete()
    return redirect('Admin:place')
    #---------------------------------------delete subcat-------------------
def deletesubcategory(request,sid):
    tbl_subcategory.objects.get(id=sid).delete()
    return redirect('Admin:subcategory')
    #.............................edit subcategory......................................
def editsubcategory(request,sid):
    category=tbl_category.objects.all()
    scate=tbl_subcategory.objects.get(id=sid)
    if request.method=="POST":
        scate.subcategory_name=request.POST.get('txtsub')
        scate.category=tbl_category.objects.get(id=request.POST.get("cate"))
        scate.save()
        return redirect('Admin:subcategory')
    else:
         return render(request,'Administrator/Subcategory.html',{'editscate':scate,'category':category})
         #-------------------------------------------------------------------
def editplace(request,pid):
    district=tbl_district.objects.all()
    pla=tbl_place.objects.get(id=pid)
    if request.method=="POST":
        pla.place_name=request.POST.get('txtplace')
        pla.district=tbl_district.objects.get(id=request.POST.get("dept"))
        pla.save()
        return redirect('Admin:place')
    else:
         return render(request,'Administrator/Place.html',{'editpla':pla,'district':district})

#*********************DEPARTMENT*********************************************
def departmemnt(request):
    departmemnt=tbl_department.objects.all()
    if request.method=='POST':
        tbl_department.objects.create(department_name=request.POST.get('txtdeptname'),)
        return redirect('Admin:departmemnt')
    else:
        return render(request,'Administrator/Department.html',{'departmemnt':departmemnt})

def deletedepartment(request,deid):
    tbl_department.objects.get(id=deid).delete()
    return redirect('Admin:departmemnt')
   
def editdepartment(request,deid):
    dept=tbl_department.objects.get(id=deid)
    if request.method=="POST":
        dept.department_name=request.POST.get('txtdeptname')
        dept.save()
        return redirect('Admin:departmemnt')
    else:
         return render(request,'Administrator/Department.html',{'editdept':dept})
#-------------------------DESIGNATION------------------------------------------

def designation(request):
    designation=tbl_designation.objects.all()
    if request.method=='POST':
        tbl_designation.objects.create(designation_name=request.POST.get('txtdesigname'),)
        return redirect('Admin:designation')
    else:
        return render(request,'Administrator/Designation.html',{'designation':designation})

def deletedesignation(request,dsid):
    tbl_designation.objects.get(id=dsid).delete()
    return redirect('Admin:designation')

def editdesignation(request,dsid):
    dsig=tbl_designation.objects.get(id=dsid)
    if request.method=="POST":
        dsig.designation_name=request.POST.get('txtdesigname')
        dsig.save()
        return redirect('Admin:designation')
    else:
         return render(request,'Administrator/Designation.html',{'editdsig':dsig})


 #**********************************************EMPLOYEE*******************************
def employeeinsertselect(request):
    department=tbl_department.objects.all()
    designation=tbl_designation.objects.all()
    employee=tbl_employees.objects.all()
    if request.method=="POST":
        employeename=request.POST.get('txt_ename')
        employeecontact=request.POST.get('txt_contact')
        employeeemail=request.POST.get('txt_mail')
        employeeadd=request.POST.get('txt_add')
        employeebs=request.POST.get('txt_bs')

        departmentid=tbl_department.objects.get(id=request.POST.get('sel_department'))
        designationid=tbl_designation.objects.get(id=request.POST.get('sel_designation'))

        tbl_employees.objects.create(
            emp_name=employeename,emp_contact=employeecontact,emp_email=employeeemail,emp_address=employeeadd,emp_bs=employeebs,department_name=departmentid,designation_name=designationid
        )
        return redirect('Admin:employeeinsertselect')
    else:
        return render(request,'Administrator/Employee.html',{'department':department,'designation':designation,'employee':employee}) 

def deleteemployee(request,empid):
    tbl_employees.objects.get(id=empid).delete()
    return redirect('Admin:employeeinsertselect')

def editemployee(request,empid):
    department=tbl_department.objects.all()
    designation=tbl_designation.objects.all()
    employee=tbl_employees.objects.all()    
    emplo=tbl_employees.objects.get(id=empid)
    if request.method=="POST":
        emplo.employee_name=request.POST.get('txt_ename')
        emplo.employee_contact=request.POST.get('txt_contact')
        emplo.employee_email=request.POST.get('txt_mail')
        emplo.employee_address=request.POST.get('txt_add')
        emplo.employee_basic=request.POST.get('txt_bs')
        emplo.department=tbl_department.objects.get(id=request.POST.get('sel_department'))
        emplo.designation=tbl_designation.objects.get(id=request.POST.get('sel_designation'))
        emplo.save()
        return redirect('Admin:employeeinsertselect')
    else:
        return render(request,'Administrator/Employee.html',{'editemp':emplo,'department':department,'designation':designation,'employee':employee})

def homepage(request):
    if 'aid'  in request.session:
        admin=tbl_admin.objects.get(id=request.session["aid"])
        
        #complaintdata
        totalc=tbl_usercomplaint.objects.all().count()
        solved=tbl_usercomplaint.objects.filter(Complaint_status=1).count()
        unsolved=int(totalc)-int(solved)

        cdata=[
            {'label':'Total','value':totalc},
            {'label':'Solved','value':solved},
            {'label':'Pending','value':unsolved},
        ]

        return render(request,'Administrator/Homepage.html',{"admin":admin,'cdata':cdata})
    else:
        return redirect('Guest:index')


def viewusercomplaint (request):
    complaint=tbl_usercomplaint.objects.filter(Complaint_status=0)
    solvedcomplaint=tbl_usercomplaint.objects.filter(Complaint_status=1)   
    if request.method=='POST':
        return redirect('Admin:viewusercomplaint')
    else:
        return render(request,'Administrator/Viewusercomplaint.html',{"complaint":complaint,"solvedcomplaint":solvedcomplaint})

def replaynow(request,compid):
    comp=tbl_usercomplaint.objects.get(id=compid)
    if request.method=='POST':
        comp.Complaint_replay=request.POST.get('txt_replay')
        comp.Complaint_replaydate=date.today()
        comp.Complaint_status=1
        comp.save()
        return redirect('Admin:viewusercomplaint')
    else:
        return render(request,'Administrator/Replaynow.html',{"comp":comp,"date":date})


#*****************************************************************************

# def viewdeliveryboy(request):
#     return render(request,'Administrator/viewdeliveryboy.html')
def viewfeedback(request):
    feedback=tbl_feedback.objects.all()
    if request.method=='POST':
        return redirect('Admin:viewfeedback')
    else:
        return render(request,'Administrator/Viewfeedback.html',{"feedback":feedback})
     

def pharmacyverification(request):
    pharmacy=tbl_pharmacy.objects.filter(pharmacy_status=0)
    accept=tbl_pharmacy.objects.filter(pharmacy_status=1)
    reject=tbl_pharmacy.objects.filter(pharmacy_status=2)
    return render(request,'Administrator/pharmacyverification.html',{'pharmacy':pharmacy,'accept':accept,'reject':reject})

def accept(request,id):
    pharmacy=tbl_pharmacy.objects.get(id=id)
    pharmacy.pharmacy_status=1
    pharmacy.save()
      # Sending verification email
    subject = "Pharmacy Verification Successful"
    body = (f"Respected {pharmacy.pharmacy_name},\n\n"
            f"Your pharmacy '{pharmacy.pharmacy_name}' has been successfully verified.\n\n"
            f"Registered Details:\n"
           
            f"Address: {pharmacy.pharmacy_address}\n"
            f"Contact: {pharmacy.pharmacy_contact}\n\n"
            "You can now start using our platform for medicine bookings and sales.\n\n"
            "Best Regards,\n Team")
    
    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [pharmacy.pharmacy_email],
        fail_silently=False,
    )
    
    return redirect('Admin:pharmacyverification')

def reject(request,id):
    pharmacy=tbl_pharmacy.objects.get(id=id)
    pharmacy.pharmacy_status=2
    pharmacy.save()
    subject = "Pharmacy Verification rejected"
    body = (f"Respected {pharmacy.pharmacy_name},\n\n"
            f"Your pharmacy '{pharmacy.pharmacy_name}' has been rejected.\n\n"
            f"Registered Details:\n"
           
            f"Address: {pharmacy.pharmacy_address}\n"
            f"Contact: {pharmacy.pharmacy_contact}\n\n"
            "Sorry \n\n"
            "Best Regards,\n Team")
    
    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [pharmacy.pharmacy_email],
        fail_silently=False,
    )
    return redirect('Admin:pharmacyverification')

def deliveryboyverification(request):
    deliveryboy=tbl_deliveryboy.objects.filter(deliveryboy_status=0)
    daccept=tbl_deliveryboy.objects.filter(deliveryboy_status=1)
    dreject=tbl_deliveryboy.objects.filter(deliveryboy_status=2)
    return render(request,'Administrator/deliveryboyverification.html',{'deliveryboy':deliveryboy,'daccept':daccept,'dreject':dreject})

def daccept(request,id):
    deliveryboy=tbl_deliveryboy.objects.get(id=id)
    deliveryboy.deliveryboy_status=1
    deliveryboy.save()
    subject = " delivery agent Verification Successful"
    body = (f"Respected {deliveryboy.deliveryboy_name},\n\n"
            f"Your  delivery agent '{deliveryboy.deliveryboy_name}' has been successfully verified.\n\n"
            f"Registered Details:\n"
           
            f"Address: {deliveryboy.deliveryboy_address}\n"
            f"Contact: {deliveryboy.deliveryboy_contact}\n\n"
            "You can now start using our platform for medicine bookings and sales.\n\n"
            "Best Regards,\n Team")
    
    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [deliveryboy.deliveryboy_email],
        fail_silently=False,
    )
    
    return redirect('Admin:deliveryboyverification')

def dreject(request,id):
    deliveryboy=tbl_deliveryboy.objects.get(id=id)
    deliveryboy.deliveryboy_status=2
    deliveryboy.save()
    subject = " delivery agent Verification  rejected"
    body = (f"Respected {deliveryboy.deliveryboy_name},\n\n"
            f"Your delivery agent '{deliveryboy.deliveryboy_name}' has been rejected.\n\n"
            f"Registered Details:\n"
           
            f"Address: {deliveryboy.deliveryboy_address}\n"
            f"Contact: {deliveryboy.deliveryboy_contact}\n\n"
            "Sorry.\n\n"
            "Best Regards,\n Team")
    
    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [deliveryboy.deliveryboy_email],
        fail_silently=False,
    )
    
    return redirect('Admin:deliveryboyverification')


def logout(request):
    del request.session['aid']
    return redirect('Guest:index')

def report(request):
    from_date = to_date = ''
    report_data = []

    if request.method == "POST":
        from_date = request.POST.get('txt_fromdate')
        to_date = request.POST.get('txt_todate')

        bookings = tbl_booking.objects.filter(
            booking_status__gte=1,
            booking_date__range=[from_date, to_date]
        )
# pharmacy get insted of all
        pharmacys = tbl_pharmacy.objects.all()   

        for pharmacy in pharmacys:
            pharmacy_total = 0
            medicine_data = []

            for booking in bookings:
                carts = tbl_cart.objects.filter(booking_id=booking, medicine_id__Pharmacy=pharmacy)

                for cart in carts:
                    medicine = cart.medicine_id
                    quantity = cart.cart_qty
                    try:
                        medicine_rate = float(medicine.medicine_rate)
                    except ValueError:
                        medicine_rate = 0
                    total_amount = medicine_rate * quantity
                    pharmacy_total += total_amount

                    medicine_data.append({
                        'date': booking.booking_date,
                        'amount': total_amount,
                        'user': booking.user,
                        'pharmacy': pharmacy.pharmacy_name,
                        'medicine': medicine.medicine_name,
                        'quantity': quantity
                    })

            if medicine_data:
                report_data.append({
                    'pharmacy': pharmacy.pharmacy_name,
                    'medicines': medicine_data,
                    'pharmacy_total': pharmacy_total
                })

    return render(request, 'Administrator/SalesReport.html', {
        'data': report_data,
        'from_date': from_date,
        'to_date': to_date
    })

def chartreport(request):
    return render(request,"Administrator/ChartReport.html")

from django.db.models import Count, Sum
from django.db.models.functions import TruncMonth
from collections import OrderedDict

def ajaxchartreport(request):
    today = datetime.today()
    current_year = today.year

    # =============================
    # 1. Bar Chart: Monthly Sales
    # =============================
    bookings = (
        tbl_booking.objects
        .filter(booking_date__year=current_year)
        .annotate(month=TruncMonth('booking_date'))
        .values('month')
        .annotate(total=Sum('booking_amount'))
        .order_by('month')
    )

    month_map = OrderedDict()
    for month in range(1, 13):
        month_label = datetime(current_year, month, 1).strftime('%b')
        month_map[month_label] = 0

    for b in bookings:
        month_label = b['month'].strftime('%b')
        if month_label in month_map:
            month_map[month_label] = float(b['total'])

    bar_chart_data = {
        'labels': list(month_map.keys()),
        'data': list(month_map.values())
    }

    # =============================
    # 2. Pie Chart: Medicine by Category
    # =============================
    category_data = (
        tbl_medicine.objects
        .values('category__category_name')
        .annotate(total=Count('id'))
        .order_by('category__category_name')
    )

    pie_chart_data = {
        'labels': [item['category__category_name'] for item in category_data],
        'data': [item['total'] for item in category_data]
    }

    # =============================
    # Combined Response
    # =============================
    return JsonResponse({
        'bar_chart': bar_chart_data,
        'pie_chart': pie_chart_data
    })
