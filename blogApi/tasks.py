from celery.task import task
from celery.utils.log import get_task_logger
from .models import PrayerRequest

logger = get_task_logger(__name__)


@task(name="send_feedback_email_task")
def send_feedback_email_task(message, email):
    logger.info("Sent feedback email")
    return send_feedback_email_task(message, email)
