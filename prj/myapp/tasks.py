from celery import shared_task
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)
@shared_task()
def add(x, y):
    return x + y

@shared_task()
def show(x,y):
    logger.info('Adding {0} + {1}'.format(x, y))