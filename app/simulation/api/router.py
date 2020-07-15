from .viewsets import SimulationViewSet, SimulationDataSerializer
from rest_framework import routers


router = routers.DefaultRouter()
router.register('simulation', SimulationViewSet)
router.register('simulation-data', SimulationDataSerializer)
