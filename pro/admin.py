from django.contrib import admin
from .models import Event, EventSession, Registration, QuestionAndAnswer, Networking, Feedback, ChatbotLog

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'created_by', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('start_time', 'end_time', 'created_at')


@admin.register(EventSession)
class EventSessionAdmin(admin.ModelAdmin):
    list_display = ('session_title', 'event', 'start_time', 'end_time', 'speaker')
    search_fields = ('session_title', 'speaker')
    list_filter = ('start_time', 'end_time')


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'registration_date')
    search_fields = ('user_username', 'event_title')
    list_filter = ('registration_date',)


@admin.register(QuestionAndAnswer)
class QuestionAndAnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'user', 'session', 'created_at')
    search_fields = ('question', 'user_username', 'session_session_title')
    list_filter = ('created_at',)


@admin.register(Networking)
class NetworkingAdmin(admin.ModelAdmin):
    list_display = ('user', 'match_user', 'chat_room_link', 'created_at')
    search_fields = ('user_username', 'match_user_username')
    list_filter = ('created_at',)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'rating', 'created_at')
    search_fields = ('event_title', 'user_username')
    list_filter = ('rating', 'created_at')


@admin.register(ChatbotLog)
class ChatbotLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'query', 'created_at')
    search_fields = ('user__username', 'query')
    list_filter = ('created_at',)