from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(
    key_func=get_remote_address,
    storage_uri="memory://", #will add redis here soon
    headers_enabled=True,
    strategy="fixed-window" #also support sliding and moving window
)