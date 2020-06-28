from celery.task import task
from celery.utils.log import get_task_logger
from .emails import  send_feedback_email
from .recolor import recolor_blog_picture

logger = get_task_logger(__name__)


@task(name="send_feedback_email_task")
def send_feedback_email_task(message, email):
    logger.info("Sent Prayer request confirmation email")
    return send_feedback_email(message, email)


@task(name="recolor_blog_picture_task")
def recolor_blog_picture_task(picture):
    logger.info("I have recolor the blog picture")
    return recolor_picture(picture)
