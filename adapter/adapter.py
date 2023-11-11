class GeneralEmailService:
    def send_email(self, recipient, message):
        print(f'Sending email to {recipient} with message: {message}')

class EmailService:
    def send_email(self, to, subject, body):
        pass

class GeneralEmailAdapter(EmailService):
    def __init__(self, legacy_email_service):
        self.legacy_email_service = legacy_email_service

    def send_email(self, to, subject, body):
        recipient = to
        message = f"Subject: {subject}\n{body}"
        self.legacy_email_service.send_email(recipient, message)

class SpecialEmailService(EmailService):
    def send_email(self, to, subject, body):
        print(f'Sending email to {to} with subject: {subject}\n{body}')

modern_email_service = SpecialEmailService()
general_email_service = GeneralEmailService()

modern_email_service.send_email("user@example.com", "Test 1", "This is an email")

general_adapter = GeneralEmailAdapter(general_email_service)
general_adapter.send_email("user@example.com", "Test 2", "This is a new email")
