from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from posts.models import Post

# Create your tests here.
User = get_user_model()

class FollowFeedTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='alice', password='pass')
        self.user2 = User.objects.create_user(username='bob', password='pass')
        self.user3 = User.objects.create_user(username='carol', password='pass')

        self.token1 = Token.objects.create(user=self.user1)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token1.key)

        # user2 and user3 create posts
        Post.objects.create(author=self.user2, title='B Post', content='by bob')
        Post.objects.create(author=self.user3, title='C Post', content='by carol')

    def test_follow_and_feed(self):
        # initially feed empty
        resp = self.client.get(reverse('feed'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data['results']), 0)  # page results if pagination else check list

        # follow user2
        follow_url = reverse('follow_user', kwargs={'user_id': self.user2.id})
        resp = self.client.post(follow_url)
        self.assertEqual(resp.status_code, 200)

        # feed should now include user2's post
        resp = self.client.get(reverse('feed'))
        self.assertEqual(resp.status_code, 200)
        # depending on pagination: check resp.data['results'] or resp.data
        data_list = resp.data.get('results', resp.data)
        self.assertTrue(any(item['title'] == 'B Post' for item in data_list))
