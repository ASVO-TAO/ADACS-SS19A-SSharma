def send_email(to,job_key,bcc=None): #needs url
    ''' sends email using a Jinja HTML template '''
    import smtplib
    import time


    # Import the email modules
    from email.mime.multipart import MIMEMultipart
    #from email.mime.text import MIMEText
    #from jinja2 import Template
    from django.template import Template,Context

    msg = MIMEMultipart('alternative')
    msg['From']    = 'noreply@swin.edu.au'
    msg['Subject'] = 'Your Galaxia job '+str(job_key)+ ' is complete'
    msg['To']      = to
    msg['Bcc']     = bcc

    server = smtplib.SMTP('mail.swin.edu.au', 25)
    html_template = Template('Dear Galaxia User, Your job {{ job_id }} is complete.'
                             ' You can download the parameter and'
                             ' output files by following this link: {{ job_link }}')
    html_context = Context({'job_id' : job_key}, {'job_link' : 'fakeurl'})

    html_final_content = html_template.render(html_context)

    #txt_template = ('Dear Galaxia User, Your job {{ job_id }} is complete.'
                   # ' You can download the parameter and'
                   # ' output files by following this link: {{ job_link }}')
    #text_part = MIMEText(txt_template, 'plain')

    #msg.attach(text_part)
    msg.attach(html_final_content)
    server.sendmail('noreply@swin.edu.au',to, msg.as_string())
    server.quit()

