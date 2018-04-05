from config import universal, constants
from database import db, db_models
from flask import render_template
from util import sendgrid_wrapper as sgw

DEFAULT_SENDER = sgw.Email(universal.CONTACT_EMAIL, universal.BUSINESS_NAME)
# BCC_RECIPIENTS = [sgw.Email('founders@blocklancer.vn', 'Founders')]

EMAILS = {
    'welcome': {
        'subject': 'Welcome to Sharing Economy Protocol'
    },
    'contact': {
        'subject': 'Thanks for your interest in Sharing Economy!'
    },
    'demo_dapp_announcement': {
        'subject': 'Sharing Economy Demo DApp is now live on testnet'
    },
    'build_on_origin': {
        'subject': 'Thanks for your interest in Sharing Economy!'
    },
    'march_2018_newsletter': {
        'subject': 'News from Sharing Economy Protocol (March 2018)'
    },
}

def send_email_type(email_type, from_email, to_email):
    msg_subject = EMAILS.get(email_type).get('subject')

    msg_text = render_template('email/%s.txt' % email_type, universal=universal, to_email=to_email)
    msg_html = render_template('email/%s.html' % email_type, universal=universal, to_email=to_email)

    send_email_msg(from_email, to_email, 
        msg_subject, email_type, msg_text, msg_html)


def has_existing_message(to_email, msg_purpose):
    ML = db_models.MessageLog
    existing_msgs = ML.query.filter(ML.email == to_email)

    if msg_purpose:
        existing_msgs = existing_msgs.filter(ML.msg_purpose == msg_purpose)

    return existing_msgs.count()

def send_email_msg(from_email, to_email, msg_subject, msg_purpose,
    msg_text, msg_html):

    if not has_existing_message(to_email, msg_purpose):
        try:

            add_to_message_log(to_email, msg_purpose, msg_text, msg_subject, msg_html)

            try:    
                categories = [msg_purpose]

                if 'localhost' in constants.HOST or 'pagekite' in constants.HOST:
                    sgw.send_message(
                        sender=from_email,
                        recipients=[sgw.Email(constants.DEV_EMAIL, constants.DEV_EMAIL)],
                        subject='DEV: ' + msg_subject,
                        body_text=msg_text,
                        body_html=msg_html,
                        categories=categories)
                else:
                    sgw.send_message(
                        sender=from_email,
                        recipients=[sgw.Email(to_email, to_email)],
                        subject=msg_subject,
                        body_text=msg_text,
                        body_html=msg_html,
                        categories=categories)

            except Exception as e:
                sgw.notify_admins("Unable to send email message for " + to_email + " because \n\n" + str(e))

        except Exception as e:
            sgw.notify_admins("Unable to write to message log for " + to_email + " because \n\n" + str(e))

def add_to_message_log(email, msg_purpose, msg_text, msg_subject=None, msg_html=None):
    message_log = db_models.MessageLog(
    email=email,
    msg_purpose=msg_purpose,
    msg_subject=msg_subject,
    msg_text=msg_text,
    msg_html=msg_html)

    db.session.add(message_log)
    db.session.commit()
