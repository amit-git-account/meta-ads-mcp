class MetaAdsMcpError(Exception):
    pass

class ConfigError(MetaAdsMcpError):
    pass

class HttpError(MetaAdsMcpError):
    def __init__(self, status_code: int, message: str, payload=None):
        super().__init__(f"HTTP {status_code}: {message}")
        self.status_code = status_code
        self.payload = payload
