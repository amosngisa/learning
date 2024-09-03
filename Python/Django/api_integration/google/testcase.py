from django.test import TestCase
from django.core import mail

class ContactTest(TestCase):
    def test_post(self):
        with self.captureOnCommitCallbacks(execute=True) as callbacks:
            response = self.client.post(
                '/contact',
                {'message': 'I like your site'}
            )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(callbacks), 1)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Contact Form')
        self.assertEqual(mail.outbox[0].body, 'I like your site')

# class TestClass(TestCase):
#     @classmethod
#     def setUp(self):
#         # set up data for the whole case
#         pass

