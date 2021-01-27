from rest_framework import routers

from rest.views import *


router = routers.DefaultRouter()
router.register('positions', PositionViewset)
