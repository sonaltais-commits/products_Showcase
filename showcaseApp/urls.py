from django.urls import path
from . import views

urlpatterns = [
    path("", views.services_index, name="services_index"),
    path("work/<slug:slug>/", views.service_detail, name="service_detail"),
    path("imgprocess",views.imageprocess_page,name='imgprocess'),
    path("ocr",views.ocr_page,name='ocr'),
    path("genai",views.genai_page,name='genai'),
    path("nlp",views.nlp_page,name='nlp'),
    path("customai",views.customai_page,name='customai'),
    path("webscraping",views.webscraping_page,name='webscraping'),
    path("workflow",views.workflow_page,name='workflow'),
    path("prompt",views.prompt_page,name='prompt'),
    path("python",views.python_page,name='python'),
    path("voice-agent/", views.voice_agent, name='voice_agent'),
    path("chatbot",views.chatbot,name='chatbot'),
path('pdf-parsing',views.pdf_parsing,name='pdf-parsing')

]
