from django.test import TestCase
from django.contrib.auth.models import User
from django.db.models import Max
from model_mommy import mommy
from polls.models import Poll, Choice
from random import choice as random_choice, randint


class TestCase(TestCase):

    def setUp(self):
        self.users = mommy.make(User, _quantity=10)
        self.polls = mommy.make(Poll, _quantity=100)

        for poll in self.polls:
            choice_num = randint(5, 10)
            poll.choice_set = mommy.make(
                Choice,
                poll=poll,
                _quantity=choice_num)
            poll.save()

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

    def test_polls(self):
        for i in range(1, 10):
            print("Round {}".format(i))
            for poll in Poll.objects.all():
                print("Voting in poll {}".format(poll.id))
                choice = random_choice(poll.choice_set.all())
                poll.vote_for(choice_id=choice.id)

        for poll in Poll.objects.all():
            winner_choice = poll.get_winner_choice()
            print("Winner choice for poll {} is {} with {} votes".format(
                poll.id, winner_choice.id, winner_choice.votes))
