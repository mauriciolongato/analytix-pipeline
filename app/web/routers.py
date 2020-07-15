from parambi.api.viewsets import RegistroHeaderViewSet, RegistroDetalheViewSet
from simulation.api.viewsets import SimulationViewSet, SimulationDataViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('parambi-registro-header', RegistroHeaderViewSet)
router.register('parambi-registro-detalhe', RegistroDetalheViewSet)
router.register('simulation', SimulationViewSet)
router.register('simulation-data', SimulationDataViewSet)
