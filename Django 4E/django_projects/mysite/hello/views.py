from django.http import HttpResponse


def index(request):
    if (counter_value := request.session.get("counter", 0) + 1) > 4:
        counter_value = 1

    request.session["counter"] = counter_value
    response = HttpResponse(f"View count={counter_value}")
    response.set_cookie("dj4e_cookie", "5e9ef26d", max_age=1000)

    return response
