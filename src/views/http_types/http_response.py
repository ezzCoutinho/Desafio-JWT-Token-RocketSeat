from typing import Dict, Optional


class HttpResponse:
    def __init__(self, status_code: int, body: Optional[Dict] = None) -> None:
        self.status_code = status_code
        self.body = body
