# chat/views.py
import json, pytz
from django.template import loader
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from django.shortcuts import render
from django.utils import timezone
from .models import Message, User
from .utils.color import generate_random_color
from django.template import RequestContext


def index(request):
    messages = Message.objects.all()
    context = {
        "messages": messages,
    }
    return render(request, "chat/chatroom.html", context)


def login_page(request):
    return render(request, "chat/loginpage.html")


def history_page(request):
    # Get the current user's name
    current_user_name = request.session.get("name")

    # Retrieve messages sent by the current user
    if current_user_name:
        messages = Message.objects.filter(user__name=current_user_name)
    else:
        # If user is not logged in, return an empty queryset
        messages = Message.objects.none()

    context = {"messages": messages}
    return render(request, "chat/history.html", context)


def all_users(request):
    users = User.objects.all()
    user_json = serialize("json", users)
    user_data = json.loads(user_json)
    return JsonResponse({"messages": user_data})


def create_user(request):
    if request.method == "POST":
        candidate_name = request.POST.get("name")
        if len(candidate_name) == 0:
            return render(
                request, "chat/loginpage.html", {"error": "Username can't be blank!"}
            )
        # Check if the name already exists
        if User.objects.filter(name=candidate_name).exists():
            return render(
                request, "chat/loginpage.html", {"error": "Username already exists!"}
            )

        # Create a new user
        user = User.objects.create(name=candidate_name, color=generate_random_color())

        # Store the username in the session
        request.session["name"] = candidate_name

        # Pass the success variable to the template
        return render(request, "chat/loginpage.html", {"success": True})

    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"})


def logout_user(request):
    if request.method == "POST" or request.method == "GET":
        # Check if the user is logged in (has a name in the session)
        if "name" in request.session:
            # Delete the username from the session
            username = request.session["name"]
            # Delete the username from the session
            del request.session["name"]
            return JsonResponse(
                {"status": "success", "message": "User logged out successfully"}
            )

        else:
            return JsonResponse({"status": "error", "message": "User is not logged in"})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"})


def all_messages(request):
    messages = Message.objects.all()
    messages_json = serialize("json", messages)
    messages_data = json.loads(messages_json)
    return JsonResponse({"messages": messages_data})


def get_message(request, message_id):
    try:
        # Retrieve the message object with the specified ID
        message = Message.objects.select_related("user").get(pk=message_id)

        # Convert the timestamp to Pacific time
        pacific_timezone = pytz.timezone("America/Los_Angeles")
        pacific_timestamp = message.timestamp.astimezone(pacific_timezone)

        formatted_hour = (
            pacific_timestamp.strftime("%I").lstrip("0") or "12"
        )  # Remove leading zero, or keep "12" if it's midnight
        formatted_meridian = pacific_timestamp.strftime(
            "%p"
        ).lower()  # Convert meridian to lowercase

        formatted_day = pacific_timestamp.strftime("%d").lstrip("0") or "1"

        # Combine formatted hour, meridian, and day
        formatted_hour_meridian = (
            f"{formatted_hour}:{pacific_timestamp.strftime('%M')} {formatted_meridian}"
        )
        formatted_timestamp = (
            pacific_timestamp.strftime("%B ")
            + formatted_day
            + pacific_timestamp.strftime(", %Y, ")
            + formatted_hour_meridian
        )

        # Extract data from the message and related user object
        message_data = {
            "id": message.id,
            "user": {
                "id": message.user.id,
                "name": message.user.name,
                "color": message.user.color,
                # Add more user fields as needed
            },
            "message": message.message,
            "timestamp": formatted_timestamp,
            # Add more message fields as needed
        }

        return JsonResponse(message_data)

    except Message.DoesNotExist:
        return JsonResponse(
            {"error": f"Message with ID {message_id} does not exist"}, status=404
        )


def post_message(request):
    if request.method == "POST":
        # Get the username from the session variable
        username = request.session.get("name")

        if username:
            # Retrieve the user object based on the username
            try:
                user = User.objects.get(name=username)
            except User.DoesNotExist:
                return JsonResponse(
                    {"status": "error", "message": "User does not exist"}
                )

            # Get the message data from the request body
            data = json.loads(request.body)
            message = data.get("message")

            if message:
                # Create the message object with the user and message content
                new_message = Message.objects.create(user=user, message=message)
                return JsonResponse({"status": "success", "message_id": new_message.pk})
            else:
                return JsonResponse(
                    {"status": "error", "message": "Message content is empty"}
                )
        else:
            return JsonResponse({"status": "error", "message": "User is not logged in"})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"})
