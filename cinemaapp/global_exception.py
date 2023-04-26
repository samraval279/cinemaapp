from rest_framework.views import exception_handler
from rest_framework.response import Response

from cinemaapp.global_resposne import ResponseInfo


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first, 
    response = exception_handler(exc, context)
    # print(dir(response))
    handlers = {
        'ValidationError': _handle_generic_error,
        'Http404': _handle_http_error,
    }

    exception_class = exc.__class__.__name__


    if exception_class in handlers:
     
        return handlers[exception_class](exc, context, response)
    return response

def _handle_generic_error(exc, context, response):
                
    res = ResponseInfo(response.data, "Fail", 400)
    return Response(res.custom_success_payload())

def _handle_http_error(exc, context, response):
  
    res = ResponseInfo(response.data, "Does not exist", 404)
    return Response(res.custom_success_payload())