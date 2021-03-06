from django.test import TestCase
from forum.forms import CommentForm, ThreadForm
from forum.models import Thread
from django.urls import reverse
from django.contrib.auth.models import User
from django.test.client import Client
from django.template.defaultfilters import slugify


# form tests
class TestCommentForm(TestCase):

    def test_item_topic_is_required(self):
        """ test topic field is required """
        form = ThreadForm({'topic': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('topic', form.errors.keys())
        self.assertEqual(form.errors['topic'][0],
                         'This field is required.')

    def test_item_description_is_required(self):
        """ test description field is required """
        form = ThreadForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['description'][0],
                         'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """ test correct fields are displayed in the form """
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ['body'])


# view tests
class TestForumViews(TestCase):

    def setUp(self):
        """ create user for tests """
        self.client = Client()
        self.user = User.objects.create_user('david',
                                             'dbeckham@fscr.com',
                                             'userpassword')

    def test_get_all_threads(self):
        """ test forum view, with logged in user """
        self.client.login(username='david', password='userpassword')
        response = self.client.get(reverse('forum'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/forum.html')

    def test_get_thread_detail(self):
        """ test thread detail view, with logged in user """
        self.client.login(username='david', password='userpassword')
        new_thread = Thread.objects.create(slug='test', author=self.user)
        response = self.client.get(reverse('thread_detail', args=(
                                           new_thread.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/thread_detail.html')

    def test_get_add_thread(self):
        """ test add thread view, with logged in user """
        self.client.login(username='david', password='userpassword')
        response = self.client.get(reverse('add_thread'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/add_thread.html')

    def test_get_edit_thread(self):
        """ test edit thread view, with logged in user """
        self.client.login(username='david', password='userpassword')
        new_thread = Thread.objects.create(id='1', author=self.user)
        response = self.client.get(reverse('edit_thread', args=(
                                            new_thread.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/edit_thread.html')

    def test_thread_has_slug(self):
        """ test threads are given slugs correctly when saving """
        thread = Thread.objects.create(topic="My first thread")
        thread.author = self.user
        thread.save()
        self.assertEqual(thread.slug, slugify(thread.topic))

    def test_can_add_thread(self):
        """ test can add thread successfully """
        self.client.login(username='david', password='userpassword')
        form_data = {'topic': 'test topic', 'body': 'test body',
                     'author': self.user}
        response = self.client.post(reverse(
                                'add_thread'),
                                    data=form_data)
        self.assertEqual(response.status_code, 200)
