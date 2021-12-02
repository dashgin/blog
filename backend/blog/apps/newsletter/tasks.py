from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.management import call_command  # NEW

logger = get_task_logger(__name__)


# NEW
@shared_task
def reset_post_votes():
    call_command(
        "reset_votes",
    )
