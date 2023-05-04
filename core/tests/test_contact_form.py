from django.contrib.messages import get_messages
from django.core import mail
from django.test import TestCase, Client


class ContactFormTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_successful_form_submission(self):
        response = self.client.get('/contact/')

        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            '/contact/',
            {
                'name': 'Test',
                'email': 'test@example.com',
                'phone': '0123456789',
                'subject': 'Test',
                'message': 'Test...',
            },
        )

        messages = list(get_messages(response.wsgi_request))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            'Thank you for your contact request. A member of our team will contact you within 24 hours.'
        )
        self.assertEqual(len(mail.outbox), 2)
        self.assertEqual(mail.outbox[0].subject, 'Clean Blog: Test')
        self.assertEqual(mail.outbox[1].subject, 'Clean Blog: Thank you for contacting us')
