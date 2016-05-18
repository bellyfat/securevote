from django.test import TestCase
from django.contrib.auth.models import User
from model_mommy import mommy
from polls.models import Poll
from random import choice as random_choice


class TestCase(TestCase):

    def setUp(self):
        self.users = mommy.make(User, _quantity=10)
        self.polls = mommy.make(Poll, _quantity=100)

    def tearDown(self):
        del self.users
        del self.polls

    def test_users_count(self):
        self.assertEqual(
                len(self.users), 10)

    def test_polls_count(self):
        self.assertEqual(
                len(self.polls), 100)

    def test_random_change(self):
        random_poll = random_choice(self.polls)
        self.assertIsInstance(random_poll, Poll)

        random_poll.question = 'foobar'
        self.assertEqual(random_poll.question, 'foobar')
