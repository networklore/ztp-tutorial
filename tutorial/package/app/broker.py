import redis
import rq
from app import configuration as C


def trigger_job(host, filename):
    redis_conn = redis.Redis.from_url(C.REDIS_URL)
    timeout = 600
    q = rq.Queue('ztp_tasks', connection=redis_conn)
    job_id = '{}_{}'.format(host, filename)
    try:
        rq_job = rq.job.Job.fetch(job_id, connection=redis_conn)
        if rq_job.status in ['finished', 'failed']:
            rq_job.delete()
            q.enqueue('app.tasks.ztp_start', host, filename, job_id=job_id,
                      timeout=timeout)
    except (redis.exceptions.RedisError, rq.exceptions.NoSuchJobError):
        q.enqueue('app.tasks.ztp_start', host, filename, job_id=job_id,
                  timeout=timeout)
