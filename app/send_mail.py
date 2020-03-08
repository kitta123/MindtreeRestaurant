from datetime import datetime

from flask import jsonify
from flask_mail import Message

from app import mail


def send_email(email, name):

    date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )
    try:
        msg = Message("Reservation made successfully!",
                      sender="noreply@demo.com",
                      recipients=str([email]))
        # msg.body = f"""Hi {name},\nYou have made a reservation successfully in our restaurant on {"Date&Time"+date}.
        #     \nFeel free to contact us for any inquiries. Thank you.\nRestaurant Staff""".format(name, date)
        mail.send(msg)
        return (jsonify({'status': 'Reservation added successfully'}))

    except Exception as e:
        return (jsonify({'status': 'Reservation added successfully but email not sent'}))
