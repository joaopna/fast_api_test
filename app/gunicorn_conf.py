from multiprocessing import cpu_count
import os

bind_path = os.path.dirname(__file__)

# Socket Path
bind = "unix:" + bind_path + "/gunicorn.sock"

# Worker Options
workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'

# Logging Options
loglevel = 'debug'
accesslog = bind_path + "/access_log"
errorlog = bind_path + "/error_log"
