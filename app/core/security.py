# Generate a JWT 
# user sends to your API to prove who they are without having to send their password with every request
#from datetime import datetime, timedelta 
# ==> the datetime.utcnow() is  deprecated as of Python 3.12 and scheduled for removal in a future version
from datetime import datetime, timedelta, timezone
from jose import jwt
from app.core.config import settings

def create_access_token(subject:str) -> str:
    # use universal time zone and add 30 minute for expire
    # example: creation at 4:00PM , if users send at 4:15 it allowed , if 4:31 it reject
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    payload = {
        "sub": subject,
        "exp": expire
    }
    return jwt.encode(
        payload,
        settings.JWT_SECRET,
        algorithm=settings.JWT_ALGORITHM
    )