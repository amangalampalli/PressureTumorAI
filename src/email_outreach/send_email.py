import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = "aditya.mangalampalli@gmail.com"
EMAIL_PASSWORD = ""


def parse_contacts(filename):
    names = []
    emails = []
    with open(filename, mode="r", encoding="utf-8") as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split(",")[0].split(" ")[1])
            emails.append(a_contact.split(",")[1])
    return names, emails


def sendEmail(name, recipient):
    msg = EmailMessage()
    msg[
        "Subject"
    ] = "Guidance on Research Project - Using Pressure Data to Detect and Localize Tumors"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = str(recipient)
    msg.set_content(
        """Hello Dr. """
        + str(name)
        + """,

My name is Aditya Mangalampalli and I am a 12th grader at Mission San Jose High School in Fremont, CA. I am reaching out to you today due to your experience and research with cancers and I am looking for guidance and your thoughts on my research project, a system that is able to detect tumors in the body by sampling various points of pressure and finding abnormalities in the pressure readings. Your experience as a researcher in this field will be priceless for the growth of this project.

I have been interested in using Computer Science and aplying to biology to solve problems in modern healthcare and have created many projects. In the most recent years, I have won many awards for my previous research experience with my most recent project, a system to predict neurological conditions though eye movements, ranking internationally in the International Science and Engineering Fair. I am excited to be able to use my experience to help others in this field and thus would want your guidance to help develop this project.

Do you happen to have time to schedule a quick call sometime to discuss this further?

I look forward to hearing from you and as always, feel free to contact me if you ever have any questions.

Sincerely,
Aditya Mangalampalli
aditya.mangalampalli@gmail.com
+1 (510) 456-6559"""
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print("Sending message to: " + name)


if __name__ == "__main__":
    names, emails = parse_contacts(
        "/Users/aditya/Programming/PressureTumorAI/src/email_outreach/contacts.csv"
    )
    for name, email in zip(names, emails):
        sendEmail(name, email)


# mvtgkkisjlebsohs
