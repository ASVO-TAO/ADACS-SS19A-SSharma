def send_email(to,job_key,link): #needs url
    ''' sends email using a Jinja HTML template '''


    # Import the email modules
    from django.core.mail import EmailMultiAlternatives

    from django.template import Template,Context


    url = link #'media/'+job_key+'/'+job_key

    html_template = Template('Dear Galaxia User,\n Your job {{ job_id }} is complete. \n'
                             ' You can download the parameter and'
                             ' output files by following this link: {{ job_link }}')
    html_context = Context({'job_id': job_key,'job_link': url})

    html_final_content = html_template.render(html_context)

   # print (html_final_content)

    txt_template = ('Dear Galaxia User,\n Your job {{ job_id }} is complete. \n'
                    ' You can download the parameter and'
                    ' output files by following this link: {{ job_link }}')


    msg = EmailMultiAlternatives(subject='test', from_email="noreply@swin.edu.au",to=to, body=html_final_content)
    msg.attach_alternative(txt_template, "html/text")
    msg.send()


