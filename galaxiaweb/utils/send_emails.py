from django.conf import settings

from .constants import TASK_SUCCESS, TASK_TIMEOUT, TASK_FAIL


def send_email(to, job_key, link, output_link, jobstate): #needs url
    ''' sends email using a HTML template '''
    # Import the email modules

    from django.core.mail import EmailMultiAlternatives
    from django.template import Template, Context

    if jobstate == TASK_TIMEOUT:
        # Handle timeout or failed jobs
        html_template = Template("Dear Galaxia User,\n Your job {{ job_id }} did not finish successfully.\n "
                                 "The requested simulation is either too large to be delivered or would "
                                 "take too long to compute.\n Please retry with different parameters.\n"
                                 "Alternatively, you can download galaxia code from: http://www.galaxia.sourceforge.net and run it locally.\n"
                                 "You can also download the parameter file here: {{ job_link }} \n")

        txt_template = ("Dear Galaxia User,\n Your job {{ job_id }} did not finish successfully. "
                        "No output file was generated.\n"
                        "Alternatively, you can download galaxia code from http://www.galaxia.sourceforge.net and run it locally.\n"
                        "You can also download the parameter file here: {{ job_link }} \n")

        html_context = Context({'job_id': job_key, 'job_link': link})

    elif jobstate == TASK_FAIL:
        # Handle timeout or failed jobs
        html_template = Template("Dear Galaxia User,\n Your job {{ job_id }} did not finish successfully. "
                                 "No output file was generated \n"
                                 "Alternatively, you can download galaxia code from: http://www.galaxia.sourceforge.net and run it locally.\n"
                                 "You can also download the parameter file here: {{ job_link }} \n")

        txt_template = ("Dear Galaxia User,\n Your job {{ job_id }} did not finish successfully. "
                        "No output file was generated.\n"
                        "Alternatively, you can download galaxia code from http://www.galaxia.sourceforge.net and run it locally.\n"
                        "You can also download the parameter file here: {{ job_link }} \n")

        html_context = Context({'job_id': job_key, 'job_link': link})

    else:
        html_template = Template('Dear Galaxia User,\n Your job {{ job_id }} is complete. \n'
                                 ' You can download the parameter file here: {{ job_link }} \n'
                                 ' And the output file by following this link: {{ output_link }}')
        html_context = Context({'job_id': job_key, 'job_link': link, 'output_link': output_link})

        txt_template = ('Dear Galaxia User,\n Your job {{ job_id }} is complete. \n'
                        ' You can download the parameter file here: {{ job_link }} \n'
                        ' And the output file by following this link: {{ output_link }}')

    html_final_content = html_template.render(html_context)

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
