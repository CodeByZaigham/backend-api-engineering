to run celery:
```json
celery -A Celeryfile worker --loglevel=info --pool=solo
```
to run fastapi:
```json
uvicorn main:app --reload
```
complete working flow:

                    ┌──────────────┐
                    │   FastAPI    │
                    └──────┬───────┘
                           │
                      .delay()
                           │
                           ▼
                    ┌──────────────┐
                    │    Redis     │
                    │   Broker     │
                    └──────┬───────┘
                           │
                      task message
                           │
                           ▼
                    ┌──────────────┐
                    │    Celery    │
                    │    Worker    │
                    └──────┬───────┘
                           │
                           ▼
                    process_task()
                           │
                           ▼
                    ┌──────────────┐
                    │    Redis     │
                    │ Result Store │
                    └──────────────┘