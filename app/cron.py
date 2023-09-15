from django_cron import CronJobBase, Schedule
import os
class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 120 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'app.cron'    

    def do(self):
        os.system('python assign1.py')