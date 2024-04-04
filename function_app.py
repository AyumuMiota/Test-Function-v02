import azure.functions as func
import logging
from datetime import datetime

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

def get_name(req: func.HttpRequest) -> str:
    """
    HTTP リクエストから名前を取得するヘルパー関数。
    クエリパラメータまたはリクエストボディから名前を取得します。
    """
    name = req.params.get('name')
    if not name:
        try:
            name = req.get_json().get('name')
        except ValueError:
            pass
    return name

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    name = get_name(req)
    if name:
        return func.HttpResponse(
            f"Hello, {name}. This HTTP triggered function executed successfully at {timestamp}.")
    else:
        return func.HttpResponse(
            f"This HTTP triggered function executed successfully at {timestamp}. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
        )