import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gevent'
worker_connections = 1000
timeout = 30
keepalive = 2
max_requests = 1000
max_requests_jitter = 200
preload_app = True
bind = "0.0.0.0:8000"

# Logging
accesslog = '-'
errorlog = '-'
loglevel = 'info'