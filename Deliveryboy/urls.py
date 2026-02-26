from django.urls import path,include
from Deliveryboy import views
app_name='Deliveryboy'
urlpatterns = [ 

     path('myprofile/',views.myprofile,name='myprofile'), 
     path('editprofile/',views.editprofile,name='editprofile'), 
     path('changepassword/',views.changepassword,name='changepassword'), 
     path('deliveryhomepage/',views.deliveryhomepage,name='deliveryhomepage'), 
     path('viewbooking/',views.viewbooking,name='viewbooking'),
     path('viewcart/<int:id>',views.viewcart,name='viewcart'),
     path('ordercollect/<int:id>',views.ordercollect,name='ordercollect'),
     path('delivered/<int:id>',views.delivered,name='delivered'),
     path('myorder/',views.myorder,name='myorder'),
     path('logout/',views.logout,name='logout'),
]