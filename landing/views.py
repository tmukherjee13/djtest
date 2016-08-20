from django.shortcuts import render
from landing.models import Portfolio, Cms, Service
from landing.forms import ContactForm
from django.http import HttpResponseRedirect, HttpResponse
import mimetypes
import json
import os

# Create your views here.


def home(request):
    portfolios = Portfolio.objects.all()
    services = Service.objects.all()
    content = Cms.objects.get(pk=1)
    form = ContactForm()

    template = "home.html"
    context = {"portfolios": portfolios,
               "content": content,
               "services": services, "form": form}

	#print services

    return render(request, template, context)


def resume(request):
    filename = 'tarun_mukherjee_resume.doc'
    file_path = "media/resume/" + filename
    original_filename = filename
    fp = open(file_path, 'rb')
    response = HttpResponse(fp.read())
    fp.close()
    type, encoding = mimetypes.guess_type(original_filename)
    if type is None:
        type = 'application/octet-stream'
    response['Content-Type'] = type
    response['Content-Length'] = str(os.stat(file_path).st_size)
    if encoding is not None:
        response['Content-Encoding'] = encoding

    # To inspect details for the below code, see http://greenbytes.de/tech/tc2231/
    if u'WebKit' in request.META['HTTP_USER_AGENT']:
        # Safari 3.0 and Chrome 2.0 accepts UTF-8 encoded string directly.
        filename_header = 'filename=%s' % original_filename.encode('utf-8')
    elif u'MSIE' in request.META['HTTP_USER_AGENT']:
        # IE does not support internationalized filename at all.
        # It can only recognize internationalized URL, so we do the trick via routing rules.
        filename_header = ''
    else:
        # For others like Firefox, we follow RFC2231 (encoding extension in HTTP headers).
        filename_header = 'filename*=UTF-8\'\'%s' % urllib.quote(original_filename.encode('utf-8'))
    response['Content-Disposition'] = 'attachment; ' + filename_header
    return response


def contact(request):

	if request.method == 'POST':

		contact = ContactForm(request.POST)
        post_data = request.POST
        # Have we been provided with a valid form?
        if contact.is_valid():
            contact.save(commit=True)
            response_data = {}
            response_data['result'] = "success"
            response_data['data'] = post_data

            return HttpResponse(json.dumps(response_data),content_type="application/json")

            
        else:
            return HttpResponseRedirect('/')
