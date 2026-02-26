from django.urls import path,include
from Pharmacy import views
app_name='Pharmacy'
urlpatterns = [ 
    path('myprofile/',views.myprofile,name='myprofile'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('medicine/', views.medicine, name='medicine'),
    path('deletemedicine/<int:mid>/', views.deletemedicine, name='deletemedicine'),
    path('editmedicine/<int:mid>/', views.editmedicine, name='editmedicine'),
    path('addstock/<int:id>/',views.addstock,name='addstock'),  
    path('pharmacyhomepage/',views.pharmacyhomepage,name='pharmacyhomepage'),
    path('viewuserbooking/',views.viewuserbooking,name='viewuserbooking'),
    path('viewusercart/<int:id>',views.viewusercart,name='viewusercart'),
    path('packorder/<int:id>',views.packorder,name='packorder'),
   
    path('verified/<int:id>',views.verified,name='verified'),
    path('logout/',views.logout,name='logout'),

    path('chat/<int:id>',views.chat,name="chat"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),

    #  path('viewuserorder/',views.viewuserorder,name='viewuserorder'),

   
]