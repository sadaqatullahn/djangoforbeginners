from django.test import TestCase
from django.urls import reverse

from .models import Posts

# Create your tests here.
class PostModelTest(TestCase):
    """Test Case for Posts Model"""

    def setUp(self):
        Posts.objects.create(text='just a test')

    def test_text_content(self):
        post = Posts.objects.get(id=1)
        expected_object = f'{post.text}'
        self.assertEqual(expected_object, 'just a test')

class HomePageViewTest(TestCase):
    """Tests for HomePageView"""

    def setUp(self):
        Posts.objects.create(text='testing Home Page View')

    def test_view_url_exist_at_propoer_location(self):
        resp = self.client.get('/posts')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('HomePage'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('HomePage'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'homepage.html')