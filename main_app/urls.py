from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name = 'wishlists'),
    path('about/', views.About.as_view(), name = 'about'),
    path('tools/', views.Tools.as_view(), name = 'tools'),
    path('tools/new/', views.ToolsAdd.as_view(), name = 'tools_add'),
    path('tools/<int:pk>/', views.ToolDetail.as_view(), name="tool_detail"),
    path('tools/<int:pk>/update/', views.ToolUpdate.as_view(), name = "tool_update"),
    path('tools/<int:pk>/delete/', views.ToolDelete.as_view(), name="tool_delete"),
    path('<int:pk>/delete/', views.WishlistDelete.as_view(), name="wishlist_delete"),
    path('tools/<int:pk>/reviews/new/', views.ReviewCreate.as_view(), name="review_create"),
    path('wishlists/<int:pk>/new/', views.WishlistCreate.as_view(), name="wishlist_create"),
    path('wishlists/<int:pk>/tools/<int:tool_pk>/', views.WishlistToolAssoc.as_view(), name="wishlist_tool_assoc"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
]