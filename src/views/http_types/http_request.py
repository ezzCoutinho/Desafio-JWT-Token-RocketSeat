from typing import Dict, Optional
from werkzeug.datastructures import Headers


class HttpRequest:
    def __init__(
        self,
        body: Optional[Dict] = None,
        headers: Optional[Headers] = None,
        params: Optional[Dict] = None,
        token_info: Optional[Dict] = None,
    ) -> None:
        self.body = body
        self.headers = headers
        self.params = params
        self.token_info = token_info
