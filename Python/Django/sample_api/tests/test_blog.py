from django.test import TestCase

from django.contrib.auth.models import User

from sample_app.models import Blog

class BlogModelTestCase(TestCase):
    
    def test_blog_creation(self):
        user = User.objects.create_user(username="Amos", email="email@mail.com", password="Pass12345")
        blog = Blog.objects.create(author=user, title="Test Blog", content="This is a test blog.")
        self.assertEqual(blog.title, "Test Blog")
        self.assertEqual(blog.content, "This is a test blog.")
        self.assertEqual(blog.author, user)