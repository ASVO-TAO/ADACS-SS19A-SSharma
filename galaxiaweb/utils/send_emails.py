from django.conf import settings


def send_email(to, job_key, link, output_link): #needs url
    ''' sends email using a HTML template '''
    # Import the email modules

    from django.core.mail import EmailMultiAlternatives
    from django.template import Template,Context

    html_template = Template('Dear Galaxia User,\n Your job {{ job_id }} is complete. \n'
                             ' You can download the parameter file here: {{ job_link }} \n'
                             ' And the output file by following this link: {{ output_link }}')
    html_context = Context({'job_id': job_key,'job_link': link, 'output_link': output_link})

    html_final_content = html_template.render(html_context)

    txt_template = ('Dear Galaxia User,\n Your job {{ job_id }} is complete. \n'
                    ' You can download the parameter file here: {{ job_link }} \n'
                    ' And the output file by following this link: {{ output_link }}')

    msg = EmailMultiAlternatives(subject='Your Galaxia Job status', from_email="noreply@swin.edu.au",to=to, body=html_final_content)
    msg.attach_alternative(txt_template, "html/text")
    msg.send()


def get_absolute_site_url(request):
    site_name = request.get_host()
    if request.is_secure():
        protocol = 'https'
    else:
        protocol = settings.HTTP_PROTOCOL
    address = protocol + '://' + site_name
    # if settings.ROOT_SUBDIRECTORY_PATH != '':
    #     address += '/' + settings.ROOT_SUBDIRECTORY_PATH[:-1]
    return address
