import json
from django.shortcuts import render, get_object_or_404
from django.utils.safestring import mark_safe


# sample in-memory "projects". Replace with DB model if you want.
PROJECTS = [
    {"Name": "Python Development", "slug": "python", "Type": "We build scalable backends with Django, FastAPI, and SQL, paired with Tkinter GUIs for desktop apps.", "Image": "images/python.jpeg", "Published": "View","link":"/python"},
    {"Name": "Custom AI Training", "slug": "ocr", "Type": "We train domain-specific AI models for businesses that need more than generic solutions.", "Image": "images/custom_ai.jpg", "Published": "View","link":"/customai"},
    {"Name": "PDF Parsing", "slug": "pdf-parsing", "Type": "We extract structured tables and text from scanned/digital PDFs using Python libraries like Camelot and Tabula.", "Image": "images/pdfparse.jpeg", "Published": "View","link":"/pdf-parsing"},
    {"Name": "Gen AI", "slug": "genai", "Type": "We design optimized prompts to enable accurate, context-aware outputs from generative AI models.", "Image": "images/genai.jpeg", "Published": "View","link":"/genai"},
    {"Name": "Chatbot And LLM Integration", "slug": "chatbot", "Type": "We specialize in Chatbot development with LLM integration, creating context-aware AI assistants for FAQs.", "Image": "images/chatbot.jpeg", "Published": "View","link":"/chatbot"},
    {"Name": "Image Processing", "slug": "image-processing", "Type": "We build AI processes images for real-time pattern, object, and content recognition and visual inspection.", "Image": "images/imageprocessing.jpg", "Published": "View","link":"/imgprocess"},
    {"Name": "Web Scraping", "slug": "data-viz", "Type": "We build Python Selenium/Playwright web scraping systems, automating data extraction and saving you manual effort.", "Image": "images/webacrap.jpeg", "Published": "View","link":"/webscraping"},
    {"Name": "Optical Character Recognition", "slug": "voice-ai", "Type": "We convert scanned documents to editable, searchable data using OCR (Tesseract, EasyOCR, PaddleOCR) and AI.", "Image": "images/ocr.jpeg", "Published": "View","link":"/ocr"},
    {"Name": "Prompt Engineering", "slug": "security", "Type": "We optimize AI prompts for accurate legal, PDF, and automated replies using LLMs.", "Image": "images/prompt.jpg", "Published": "View","link":"/prompt"},
    {"Name": "Natural Language Processing", "slug": "blockchain", "Type": "We craft NLP solutions for entity extraction, sentiment analysis, and text automation.", "Image": "images/nlp.jpeg", "Published": "View","link":"/nlp"},
    {"Name": "Workflow Automation", "slug": "workflow-automation",
     "Type": "We automate repetitive business processes using Python, RPA tools, and APIs to improve efficiency and reduce errors.",
     "Image": "images/workflowautomation.jpeg", "Published": "View", "link": "/workflow"},
    {"Name": "AI Voice Agent", "slug": "voice-agent",
     "Type": "We build AI-powered voice agents for customer support, appointment booking, and lead qualification, enabling natural, real-time conversations.",
     "Image": "images/voice_agent.png", "Published": "View", "link": "/voice-agent"},
]
def services_index(request):
    # Convert the PROJECTS list to JSON so JavaScript can use it
    projects_json = json.dumps(PROJECTS)

    # Render the template work_ring.html and pass the JSON
    return render(
        request,
        "work_ring.html",
        {"projects_json": mark_safe(projects_json)}
    )

# View for individual service detail page
def service_detail(request, slug):
    project = next((p for p in PROJECTS if p["slug"] == slug), None)
    if not project:
        from django.http import Http404
        raise Http404("Service not found")
    return render(request, "service_detail.html", {"project": project})
def pdf_parsing(request):
    return render(request,'pdf_parsing.html')
def imageprocess_page(request):
    return render(request,"image_processing.html")

def ocr_page(request):
    return render(request,"ocr.html")

def genai_page(request):
    return render(request,"gen_ai.html")

def nlp_page(request):
    return render(request,"nlp.html")

def customai_page(request):
    return render(request,"customai.html")

def webscraping_page(request):
    return render(request,"webscraping.html")

def workflow_page(request):
    return render(request,"workflow.html")

def prompt_page(request):
    return render(request,"prompt.html")


def python_page(request):
    return render(request, "python_dev.html")

def voice_agent(request):
    return render(request, 'voice_agent.html')

def chatbot(request):
    return render(request,'chatbot.html')