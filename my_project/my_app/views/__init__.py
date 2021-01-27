from .index_view import IndexView
from .tournaments_view import AllTournamentView
from .tournaments_view import DetailTournamentView
from .tournaments_view import CreateTournamentView
from .tournaments_view import UpdateTournamentView
from .tournaments_view import DeleteTournamentView
from .worker_view import WorkerListView
from .worker_view import CreateWorkerView
from .worker_view import AvgWorkersView
from .worker_view import UpdateWorkerView
from .worker_view import DeleteWorkerView
from .login_view import NewLoginView
from .login_view import NewLogoutView


__all__ = [
    'IndexView',
    'AllTournamentView',
    'DetailTournamentView',
    'CreateTournamentView',
    'UpdateTournamentView',
    'DeleteTournamentView',
    'WorkerListView',
    'CreateWorkerView',
    'NewLoginView',
    'NewLogoutView',
    'AvgWorkersView',
    'UpdateWorkerView',
    'DeleteWorkerView'
]
