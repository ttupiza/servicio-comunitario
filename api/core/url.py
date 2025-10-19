from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet
from .views import MedicamentoViewSet
from .views import PagoViewSet
from .views import BeneficiarioViewSet
from .views import PersonalViewSet
from .views import FamiliarViewSet
from .views import PatologiaViewSet
from .views import PrivilegioViewSet
from .views import RolViewSet
from .views import Historial_usuarioViewSet
from .views import CuidadoViewSet 
from .views import Usuario_beneficiarioViewSet
from .views import CalleViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'medicamentos', MedicamentoViewSet)
router.register(r'pagos', PagoViewSet)
router.register(r'beneficiarios', BeneficiarioViewSet)
router.register(r'personales', PersonalViewSet)
router.register(r'familiar', FamiliarViewSet)
router.register(r'patologias', PatologiaViewSet)
router.register(r'privilegios', PrivilegioViewSet)
router.register(r'roles', RolViewSet)
router.register(r'historial_usuarios', Historial_usuarioViewSet)
router.register(r'cuidados', CuidadoViewSet)
router.register(r'usuarios_beneficiarios', Usuario_beneficiarioViewSet)
router.register(r'calles', CalleViewSet)

urlpatterns = router.urls
