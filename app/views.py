import os

from django.http import (
    HttpResponseRedirect,
    StreamingHttpResponse,
    HttpResponseNotFound,
)
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from event.models import Event
from event.utils import get_next_or_past_event
from user.enums import UserType
from user.models import User


def files(request, file_):
    path, file_name = os.path.split(file_)
    path_splitted = path.split("/")
    downloadable_path = None
    if request.user.is_authenticated:
        if len(path_splitted) > 0 and path_splitted[0] == "user":
            if len(path_splitted) > 1 and path_splitted[1] == "picture":
                user = get_object_or_404(User, picture=file_)
                if (
                    not user.picture_public_participants
                    and request.user.type == UserType.PARTICIPANT.value
                ):
                    HttpResponseNotFound()
                if (
                    not user.picture_public_sponsors_and_recruiters
                    and request.user.type
                    in [UserType.SPONSOR.value, UserType.RECRUITER.value]
                ):
                    HttpResponseNotFound()
                downloadable_path = user.picture.path
            if downloadable_path:
                response = StreamingHttpResponse(open(downloadable_path, "rb"))
                response["Content-Type"] = ""
                return response
            else:
                HttpResponseNotFound()
    else:
        if len(path_splitted) > 0 and path_splitted[0] == "event":
            if len(path_splitted) > 1 and path_splitted[1] == "picture":
                event = get_object_or_404(Event, picture=file_)
                downloadable_path = event.picture.path
        if downloadable_path:
            response = StreamingHttpResponse(open(downloadable_path, "rb"))
            response["Content-Type"] = ""
            return response
        else:
            HttpResponseNotFound()
    return HttpResponseRedirect(reverse("user_login"))


def home(request):
    current_data = dict()
    event = get_next_or_past_event()
    if event:
        current_data["event"] = event
        if event.custom_home:
            return render(request, "custom/" + event.code + "/index.html", current_data)
    return render(request, "home.html", current_data)


def redirect_to(request):
    try:
        return request.headers["Referer"]
    except KeyError:
        return reverse("app_home")
