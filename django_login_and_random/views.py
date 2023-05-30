from django.http import HttpResponse
import random

Correct_login = "Deerpa"
Correct_password = "1234"


def index(request):
    login = request.POST.get("username", None)
    password = request.POST.get("password", None)

    if login == Correct_login and password == Correct_password:
        code = random.random()
        code = code * 10000
        code = int(code)

        return HttpResponse(f"<h1>Код: {code}</h1>")

    if login != Correct_login or password != Correct_password:
        error_msg = ""

        if login != Correct_login:
            error_msg += "<h1>Неверный логин!</h1>"

        if password != Correct_password:
            error_msg += "<h1>Неверный пароль!</h1>"

        error_msg += "<h1>Необходимо войти в систему снова!</h1>"
        error_msg += (
            '<a href="/login"><input type="button" value="Попробовать снова"></a>'
        )

        return HttpResponse(error_msg)

    return HttpResponse(
        f"""<h1>Необходимо войти в систему!</h1>
            <a href="/login"><input type="button" value="Войти"></a>"""
    )
