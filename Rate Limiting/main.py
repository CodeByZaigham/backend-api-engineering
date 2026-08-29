from fastapi import FastAPI , Request , Response
from fastapi.responses import JSONResponse
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler
from limiter import limiter

app=FastAPI(title="Rate limiting example")
app.state.limiter=limiter

app.add_exception_handler(
     RateLimitExceeded,
     _rate_limit_exceeded_handler
     # lambda request,exc :JSONResponse(
     #      status_code=429,
     #      content={
     #           "detail":"Rate Limit Exceeded"
     #      }
     # )
)

app.add_middleware(SlowAPIMiddleware)


@app.get("/",response_model=dict)
@limiter.limit("2/minute")
def health(request:Request,response:Response):
     return {"message":"test route working"}