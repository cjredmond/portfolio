from django.shortcuts import render
from django.views.generic import TemplateView
from reportlab.pdfgen import canvas
from django.http import HttpResponse

class IndexView(TemplateView):
    template_name = "index.html"

class ResumeView(TemplateView):
    template_name = "resume.html"
# def resume_view(request):
#     response = HttpResponse(content_type="application/pdf")
#     response['Content-Disposition'] = 'attachment; filename="info/pdf/CJRresumeupdate.docx.pdf"'
#
#     p = canvas.Canvas(response)
#
#     p.showPage()
#     p.save()
#     return response
