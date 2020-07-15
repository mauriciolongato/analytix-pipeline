from .viewsets import RegistroHeaderViewSet, RegistroDetalheViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('parambi-registro-header', RegistroHeaderViewSet)
router.register('parambi-registro-detalhe', RegistroDetalheViewSet)
