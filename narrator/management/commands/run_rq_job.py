import json

from django.core.management.base import BaseCommand
from django_rq import get_queue, get_worker
from structlog import get_logger

logger = get_logger(__name__)


class Command(BaseCommand):
    """
    This is a command to help run jobs/tasks in the code from the command line.

    @:argument task:
        Task module path, usually starting with narrator.tasks.TASK_NAME
    @:argument kwargs:
        The keyword arguments to be passed to the job

    Usage:
        python manage.py run_rq_job
                -task narrator.tasks.dummy_task
                -kwargs {"number": 123}
    """

    help = "Run a specific job in RQ synchronously"

    def add_arguments(self, parser):
        parser.add_argument("-task", type=str, help="Task name")
        parser.add_argument(
            "-kwargs", type=json.loads, help="Task keywords arguments as a json"
        )

    def handle(self, *args, **options):
        # Get the RQ queue
        queue = get_queue("default")

        task = options["task"]
        kwargs = options["kwargs"] or {}

        # Run the task synchronously
        job = queue.enqueue(task, *args, **kwargs, job_timeout=360000)
        job_processed = get_worker().work(burst=True)

        if not job_processed:
            logger.info(
                "No task was processed. Make sure you passed the right task name \
                and arguments!"
            )
            return
        logger.info(f"Task executed successfully. Result: {job.result}")
