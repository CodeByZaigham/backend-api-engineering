from redis import Redis
from dotenv import load_dotenv
import os
load_dotenv()

host=os.getenv("REDIS_HOST")
port=os.getenv("REDIS_PORT")
db=os.getenv("REDIS_DB")

redis=Redis(port=port,host=host,db=db,decode_responses=True)