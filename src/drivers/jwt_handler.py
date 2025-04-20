from datetime import datetime, timedelta, timezone
from typing import Dict

import jwt

from src.configs.jwt_configs import jwt_infos


class JwtHandler:
    def create_jwt_token(self, body: Dict = {}) -> str:
        token = jwt.encode(
            payload={
                "exp": datetime.now(timezone.utc)
                + timedelta(hours=float(jwt_infos["JWT_HOURS"])),  # type: ignore
                **body,
            },
            key=jwt_infos["KEY"],
            algorithm=jwt_infos["ALGORITHM"],
        )
        return token

    def decode_jwt_token(self, token: str) -> Dict:
        return jwt.decode(
            token,
            key=jwt_infos["KEY"],
            algorithms=[jwt_infos["ALGORITHM"]],  # type: ignore
        )
