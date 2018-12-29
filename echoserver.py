from bottle import request, route, default_app
import json


@route("/<url:re:.+>")
def hello(url):
    req = {'headers': dict(request.headers), 'path': request.path, 'query_string': request.query_string}
    print(json.dumps(req, indent=2))
    return json.dumps(req)

app = default_app()

#run(server='gunicorn')

