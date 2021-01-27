from .index_view import IndexView
from .positions_view import AllPositionView
from .positions_view import DetailPositionView
from .positions_view import CreatePositionView
from .positions_view import UpdatePositionView
from .positions_view import DeletePositionView
from .worker_view import WorkerListView
from .worker_view import CreateWorkerView
from .worker_view import AvgWorkersView
from .worker_view import UpdateWorkerView
from .worker_view import DeleteWorkerView
from .login_view import NewLoginView
from .login_view import NewLogoutView


__all__ = [
    'IndexView',
    'AllPositionView',
    'DetailPositionView',
    'CreatePositionView',
    'UpdatePositionView',
    'DeletePositionView',
    'WorkerListView',
    'CreateWorkerView',
    'NewLoginView',
    'NewLogoutView',
    'AvgWorkersView',
    'UpdateWorkerView',
    'DeleteWorkerView'
]
