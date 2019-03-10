import json

from bottle import run, template, Bottle, request, response, auth_basic, redirect, static_file, TEMPLATE_PATH

app = Bottle()
requests_handled = []
response_saved = []

@app.post("/set_response")
def set_response():
    body = b"".join(request.body)
    body = json.loads(body)
    response_saved.append(body)


@app.post("/sms/json")
@app.post("/sms/json")
def send_sms():
    postdata = request.body.read()
    body = {'from': request.forms.get("from"),
            'text': request.forms.get("text"),
            'to': request.forms.get("to")}
    requests_handled.append(body)
    if len(response_saved) > 0:
        response_to_send = response_saved.pop()
        response.status = response_to_send['status_code']
        return response_to_send['message']

@app.get("/stats")
def stats():
    body = {'requests': list(requests_handled)}
    return json.dumps(body)

run(app, host='0.0.0.0', port=8080, reloader=True)
