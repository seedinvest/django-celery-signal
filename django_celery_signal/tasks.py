from celery.task import Task
from celery.registry import tasks


class SignalTask(Task):
    def run(self, receiver, sender, **named):
        logger = self.get_logger(**named)
        logger.info("Running SignalTask for %s with args %s." % (receiver, named))
        receiver(sender=sender, **named)
        return True

tasks.register(SignalTask)