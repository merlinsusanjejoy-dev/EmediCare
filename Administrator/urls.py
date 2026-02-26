from django.urls import path,include
from Administrator import views
app_name='Admin'
urlpatterns = [
 #.....................Admin....................................   
    path('Adminregistration/',views.Adminregistration,name='Adminregistration'),
    path('deleteadmin/<int:aid>',views.deleteadmin,name='deleteadmin'),   #delete_admin
    path('editadmin/<int:aid>',views.editadmin,name='editadmin'),   #edit_admin
#........................DISTRICT...............................................
    path('District/',views.District,name='District'),
    path('deletedistrict/<int:did>',views.deletedistrict,name='deletedistrict'),   #delete_district
    path('editdistrict/<int:did>',views.editdistrict,name='editdistrict'),   #edit_district
 #......................CATEGORY............................................
    path('Category/',views.Category,name='Category'),
    path('deletecategory/<int:cid>',views.deletecategory,name='deletecategory'),    #delete_category
    path('editcategory/<int:cid>',views.editcategory,name='editcategory'),   #edit_district
#...............................PLACE....................................
    path('place/',views.place,name='place'),
    path('deleteplace/<int:pid>',views.deleteplace,name='deleteplace'),
    path('editplace/<int:pid>',views.editplace,name='editplace'),   #edit_district  
#...............................SUBCATEGORY....................................
    path('subcategory/',views.subcategory,name='subcategory'),
     path('deletesubcategory/<int:sid>',views.deletesubcategory,name='deletesubcategory'), 
     path('editsubcategory/<int:sid>',views.editsubcategory,name='editsubcategory'),   #edit_district 
     #...............................department....................................
    path('departmemnt/',views.departmemnt,name='departmemnt'),
    path('deletedepartment/<int:deid>',views.deletedepartment,name='deletedepartment'), 
    path('editdepartment/<int:deid>',views.editdepartment,name='editdepartment'),   #edit_district 
 #...............................department....................................
    path('designation/',views.designation,name='designation'),
    path('deletedesignation/<int:dsid>',views.deletedesignation,name='deletedesignation'), 
    path('editdesignation/<int:dsid>',views.editdesignation,name='editdesignation'), 
#...............................employeeee....................................
    path('employeeinsertselect/',views.employeeinsertselect,name='employeeinsertselect'),
    path('deleteemployee/<int:empid>',views.deleteemployee,name='deleteemployee'), 
    path('editemployee/<int:empid>',views.editemployee,name='editemployee'), 

    path('homepage/',views.homepage,name='homepage'), 

    path('viewusercomplaint/',views.viewusercomplaint,name='viewusercomplaint'), 
    path('replaynow/<int:compid>',views.replaynow,name='replaynow'), 



    # path('viewpharmacy/',views.viewpharmacy,name='viewpharmacy'), 
    # path('viewdeliveryboy/',views.viewdeliveryboy,name='viewdeliveryboy'), 
    path('viewfeedback/',views.viewfeedback,name='viewfeedback'), 

    path('pharmacyverification/',views.pharmacyverification,name='pharmacyverification'),
    path('accept/<int:id>',views.accept,name='accept'),
    path('reject/<int:id>',views.reject,name='reject'),    

    path('logout/',views.logout,name='logout'),
    path('deliveryboyverification/',views.deliveryboyverification,name='deliveryboyverification'),
    path('daccept/<int:id>',views.daccept,name='daccept'),
    path('dreject/<int:id>',views.dreject,name='dreject'),    
    path('report/',views.report,name='report'),

    path('chartreport/',views.chartreport,name='chartreport'),
    path('ajaxchartreport/',views.ajaxchartreport,name='ajaxchartreport'),


]