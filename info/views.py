from django.shortcuts import render
from django.views.generic import TemplateView
from reportlab.pdfgen import canvas
from django.http import HttpResponse

class IndexView(TemplateView):
    template_name = "index.html"

class ResumeView(TemplateView):
    template_name = "resume.html"
# def resume_view(request):
#     with open('info/static/pdf/CJRresumeupdate.docx.pdf' , 'r') as pdf:
#         response = HttpResponse(pdf.read(), mimetype='application/pdf')
#         response['Content-Disposition'] = 'inline;filename=/info/static/pdf/CJRresumeupdate.docx.pdf'
#         return response
#     pdf.close()
#     return response
