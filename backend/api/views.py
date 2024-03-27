from django.http import JsonResponse
import json

def api_home (request, *args, **kwargs):
    response = {}
    params = request.GET
    print("params: ", params)

    if request.method == 'POST':
        try:
            request_data = json.loads(request.body)
            print("request_data: ", request_data)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data in request body"}, status = 400)
    
    response['params'] = dict(params)
    response['headers'] = dict(request.headers)
    response['content_type'] = request.content_type
    print("response: ", response)
    return JsonResponse(response)