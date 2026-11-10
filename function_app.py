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
