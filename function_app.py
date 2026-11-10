import datetime
import logging
import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="hello", methods=["GET", "POST"])
def hello(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get("name")
    if not name:
        try:
            name = req.get_json().get("name")
        except (ValueError, AttributeError):
            name = None
    name = name or "world"
    logging.info("hello was called with name=%s", name)
    return func.HttpResponse(f"Hello, {name}! This is your first Azure Function.")

@app.timer_trigger(schedule="0 */1 * * * *", arg_name="mytimer", run_on_startup=False)
def timer_demo(mytimer: func.TimerRequest) -> None:
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    if mytimer.past_due:
        logging.info("Timer is past due (a scheduled run was missed)")
    logging.info("Timer fired at %s UTC", now)
