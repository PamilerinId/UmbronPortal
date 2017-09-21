from django.conf.urls import url, include
from rest_framework import routers
import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token


router = routers.DefaultRouter()
# router.register(r'users', views.CustomUserView)
#  Still thinking of removing this, should not be accessible except
#  to client and /register/ serves dual purpose of view and create
# *******DUAL PURPOSE BECAUSE OF VIEWSET CLASS USED instead of CBV********
router.register(r'session', views.SessionViewSet)
router.register(r'term', views.TermViewSet)
router.register(r'schools', views.SchoolViewSet)
router.register(r'classes', views.ClassViewSet)
router.register(r'subjects', views.SubjectViewSet)
router.register(r'principals', views.PrincipalViewSet)
router.register(r'teachers', views.TeacherViewSet)
router.register(r'guardians', views.GuardianViewSet)
router.register(r'students', views.StudentViewSet)



urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^register/$', views.UserRegistration.as_view()),
    url(r'^login/', obtain_jwt_token),
    # url(r'^authenticate/', views.CustomObtainAuthToken.as_view()),
    url(r'^token-refresh/', refresh_jwt_token),
    url(r'^token-verify/', verify_jwt_token),
    url(r'^users/?$', views.CustomUserView.as_view()),
]
