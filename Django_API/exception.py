from django.http import JsonResponse


def error_404(request, *args, **argv):
    return JsonResponse({"Error": "Invalid Url or maybe some Parameters are missing"})

def error_400(request, *args, **argv):
    return JsonResponse({"Error": "Bad Request Gateway"})

def error_403(request, *args, **argv):
    return JsonResponse({"Error": "Forbidden Request"})

def error_500(request, *args, **argv):
    return JsonResponse({"Error": "Internal Server Error"})

def error_503(request, *args, **argv):
    return JsonResponse({"Error": "Service Unavailable"})