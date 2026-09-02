from celery import shared_task
import time

@shared_task
def process_task(data:str):
     print(f"Processing: {data}")

     time.sleep(10)

     return {
          "message": f"Processed {data}"
     }

# remember that in celery worker tasks, you cant give
# async functions. it only works with sync tasks but 
# the hack you can apply is : result=asyncio.run(....)

# Celery has been evolving its async support, so the exact 
# answer depends on the Celery version and maybe when you see
# this repo, celery already had a promotion!!