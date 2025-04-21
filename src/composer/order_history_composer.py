from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.user_repository import UserRepository
from src.controllers.order_history import OrderHistory
from src.views.order_history_views import OrderHistoryView


def order_history_composer() -> OrderHistoryView:
    conn = db_connection_handler.get_connection()
    model = UserRepository(conn)  # type: ignore
    controller = OrderHistory(model)
    view = OrderHistoryView(controller)
    return view
