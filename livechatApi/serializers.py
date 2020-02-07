from rest_framework import serializers
from django.utils.dateparse import parse_datetime
from datetime import datetime
from livechatApi.models import Sender, Recipient, Category, Request, LCRoom, MeetingReview, MeetingReviewChoice
from users.models import User, MeetingRequest

class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value

class LCRequestSerializer(serializers.ModelSerializer):
    discussion_topic = StringSerializer(many=True)
    sender = StringSerializer(many=False)
    recipient = StringSerializer(many=True)
    article = StringSerializer(many=False)
    room_name = StringSerializer(many=False)
    room_url = StringSerializer(many=False)

    class Meta:
        model = Request
        fields = ("date_to_appointment", "created", "notified", 
                "scheduled", "canceled", "discussion_topic", "sender", 
                "recipient", "article", "room_name", "room_url")

    def create(self, request):
        data = request.data
        print("DATA")
        print(data)
        print(parse_datetime(data["date"]))
        parsed_date = parse_datetime(data["date"])
        print(datetime.strptime(data["date"], "%Y-%m-%dT%H:%M:%S.%fZ").date())
        request = Request()
        request.notified = True
        request.scheduled = True
        request.date_to_appointment = data["date"]
        request.article_id = data["articleId"]
        print("MR CORSO")
        print(User.objects.get(username=data["user"]).id)
        request.sender_id = User.objects.get(username=data["user"]).id
        
        request.save()
        request.recipient.add(User.objects.get(username=data["recipient"]).id)
        for c in data['topic']:
            print(c)
            newC = Category()
            newC.category = c
            print(newC.category)
            request.discussion_topic.set(newC.category)

        request.save()
        
        userNotification = MeetingRequest()
        userNotification.from_user = User.objects.get(username=data["user"])
        userNotification.to_user = User.objects.get(username=data["recipient"])
        userNotification.save()

        return request

class LCRequestUserListSerializer(serializers.ListSerializer):
    child = LCRequestSerializer()
    allow_null = True
    many = True

class LCRequestListDetailSerializer(serializers.ModelSerializer):
    discussion_topic = StringSerializer(many=True)
    sender = StringSerializer(many=False)
    recipient = StringSerializer(many=True)
    article = StringSerializer(many=False)
    room_name = StringSerializer(many=False)
    room_url = StringSerializer(many=False)
    class Meta:
        model = Request
        fields = ("date_to_appointment", "created", "notified", 
                "scheduled", "canceled", "discussion_topic", "sender", 
                "recipient", "article", "room_name", "room_url")


class LCRoomSerializer(serializers.ModelSerializer):
    room_id = StringSerializer(many=False)
    room_name = StringSerializer(many=False)
    url = StringSerializer(many=False)
    participants = StringSerializer(many=True)
    article = StringSerializer(many=False)

    class Meta:
        model = LCRoom
        fields = ("__all__")

class LCCreateRoomSerializer(serializers.ModelSerializer):
    room_id = StringSerializer(many=False)
    room_name = StringSerializer(many=False)
    url = StringSerializer(many=False)
    participants = StringSerializer(many=True)
    request = StringSerializer(many=False)

    class Meta:
        model = LCRoom
        fields = ("__all__")

    def create(self, request):
        data = request
        print("DATA")
        room = LCRoom()
        room.room_id = data["id"]
        room.room_name = data["name"]
        room.created_at = data["created_at"]
        room.date_to_appointment = data["d_t_a"]
        room.api_created = True
        room.url = data["url"]
        room.privacy = data["privacy"]
        room.article = data["article"]
        room.save()
        for i in data["rp"]:
            room.participants.add(User.objects.get(id=i)) 
        # room.request = True
        print("MR CORSO")
        room.save()
        
        return room

class LCRoomListDetailSerializer(serializers.ListSerializer):
    child = LCRoomSerializer()
    allow_null = True
    many = True

class LCRoomDetailSerializer(serializers.ModelSerializer):
    room_id = StringSerializer(many=False)
    room_name = StringSerializer(many=False)
    url = StringSerializer(many=False)
    participants = StringSerializer(many=True)
    article = StringSerializer(many=False)
    class Meta:
        model = LCRoom
        fields = ("__all__")

class LCMeetingReviewSerializer(serializers.ModelSerializer):
    user = StringSerializer(many=False)
    room = StringSerializer(many=False)
    meeting_rate = StringSerializer(many=False)
    conversation_rate = StringSerializer(many=False)
    attendace = StringSerializer(many=False)
    accept_working_with = StringSerializer(many=False)
    issues = StringSerializer(many=False)
    issue_type = StringSerializer(many=False)
    comment = StringSerializer(many=False)
    attended = StringSerializer(many=True)
    not_attended = StringSerializer(many=True)

    class Meta:
        model = MeetingReview
        fields = ("__all__")
    
    def create(self, request):
        data = request.data
        print("DATA")
        print(data)
        meeting_review = MeetingReview()
        print("worked 1")
        meeting_review.user = User.objects.get(username=data["user"])
        print("worked 2")
        meeting_review.room = LCRoom.objects.get(id=data["room"])
        print("worked 3")
        meeting_review.meeting_rate = data["meeting_rate"]
        meeting_review.conversation_rate = data["worthiness"]
        meeting_review.attendace = data["attendace"]
        meeting_review.accept_working_with = False
        print("worked 4")
        meeting_review.issues = data["issues"]
        print("worked 5")
        print("worked 6")
        meeting_review.comment = data["comment"]
        meeting_review.issue_type = MeetingReviewChoice.objects.get(id=data["issue_type"])
        meeting_review.save()
        if data["attendace"] == True:
            for i in data["attended"]:
                meeting_review.attended.add(User.objects.get(id=i)) 
            # room.request = True
            print("MR CORSO")
            for i in data["not_attended"]:
                meeting_review.not_attended.add(User.objects.get(id=i)) 
            meeting_review.save()
        
        return meeting_review