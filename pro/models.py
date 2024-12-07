from django.db import models
from django.contrib.auth.models import User  # For authentication

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events_created")
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title


class EventSession(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="sessions")
    session_title = models.CharField(max_length=255)
    speaker = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    live_stream_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.session_title} ({self.event.title})"


class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="registrations")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="registrations")
    registration_date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.user.username} -> {self.event.title}"


class QuestionAndAnswer(models.Model):
    session = models.ForeignKey(EventSession, on_delete=models.CASCADE, related_name="q_and_a")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="questions")
    question = models.TextField()
    answer = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Q: {self.question[:50]}... - {self.user.username}"


class Networking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="networking_initiated")
    match_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="networking_matched")
    chat_room_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.user.username} ↔ {self.match_user.username}"


class Feedback(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="feedback")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feedback_given")
    feedback_text = models.TextField()
    rating = models.PositiveSmallIntegerField()  # Add validation for 1-5 in forms
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Feedback by {self.user.username} for {self.event.title}"


class ChatbotLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chatbot_logs")
    query = models.TextField()
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Query: {self.query[:50]}..."