import datetime
import logging
import azure.functions as func

app = func.FunctionApp()

@app.timer_trigger(schedule="0 */1 * * * *", arg_name="mytimer", run_on_startup=False)
def timer_demo(mytimer: func.TimerRequest) -> None:
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    if mytimer.past_due:
        logging.info("Timer is past due (a scheduled run was missed)")
    logging.info("Timer fired at %s UTC", now)
