import json

from django.http import HttpResponse

from .bot import chatbot


def api_chatbot(request):
    response = {'status': None}

    if request.method == 'POST':
        data = json.loads(request.body)
        message = data['message']
        chat_response = chatbot.get_response(message).text
        response['message'] = {'text': chat_response, 'user': False, 'chat_bot': True }
        response['status'] = 'ok'
        
    else:
        response['error'] = 'No post data'
        
    return HttpResponse(json.dumps(response), content_type='application/json')