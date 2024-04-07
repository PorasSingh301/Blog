from post.models import Post
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class TestPostApis(APITestCase):
    def setUp(self):
        self.post_url = reverse("post-list")

        self.user = User.objects.create_user(username='admin', password='admin')
        self.token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.post_data = {
            "title": "Sample post",
            "content": "Sample content",
            "author": self.user.id
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_post_creation(self):
        resp = self.client.post(self.post_url, self.post_data)
        self.assertEqual(resp.status_code, 201)

        response = resp.json()
        self.assertEqual(response["id"], 1)
        self.assertEqual(resp.status_code, 201)

    def test_post_list(self):
        self.client.post(self.post_url, self.post_data)

        resp = self.client.get(self.post_url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["count"], 1)

    def test_post_update(self):
        resp = self.client.post(self.post_url, self.post_data)
        response = resp.json()
        id = response['id']

        data_update = {
            "title": "new title"
        }
        resp = self.client.patch(f"{self.post_url}{id}/", data_update)
        self.assertEqual(resp.status_code, 200)

        self.assertEqual(resp.json()["title"], "new title")

    def test_post_delete(self):
        resp = self.client.post(self.post_url, self.post_data)
        response = resp.json()
        id = response['id']

        resp = self.client.delete(f"{self.post_url}{id}/")
        self.assertEqual(resp.status_code, 204)

    def test_post_like(self):
        resp = self.client.post(self.post_url, self.post_data)
        response = resp.json()
        id = response['id']
        self.assertEqual(response["likes"], 0)
        resp = self.client.put(f"{self.post_url}{id}/like/")
        self.assertEqual(resp.json()["likes"], 1)

    def test_count_likes(self):
        resp = self.client.post(self.post_url, self.post_data)
        response = resp.json()
        id = response['id']
        resp = self.client.get(f"{self.post_url}{id}/count_likes/")
        self.assertEqual(resp.json()["likes"], 0)


class TestCommentApis(APITestCase):
    def setUp(self):
        self.comment_url = reverse("comment")

        self.user = User.objects.create_user(username='admin', password='admin')
        self.token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.post = Post.objects.create(title="Title", content="Content", author=self.user)

        self.comment_data = {
            "post": self.post.id,
            "author": self.user.id,
            "text": "Text"
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_comment_creation(self):
        resp = self.client.post(f"{self.comment_url}", self.comment_data)
        self.assertEqual(resp.status_code, 201)

        response = resp.json()
        self.assertEqual(response["id"], 1)
        self.assertEqual(resp.status_code, 201)

    def test_comment_list(self):
        self.client.post(self.comment_url, self.comment_data)

        resp = self.client.get(self.comment_url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["count"], 1)

    def test_comment_update(self):
        resp = self.client.post(self.comment_url, self.comment_data)
        response = resp.json()
        id = response['id']

        data_update = {
            "text": "new text"
        }
        resp = self.client.patch(f"{self.comment_url}{id}/", data_update)
        self.assertEqual(resp.status_code, 404)

    def test_comment_delete(self):
        resp = self.client.post(self.comment_url, self.comment_data)
        response = resp.json()
        id = response['id']

        resp = self.client.delete(f"{self.comment_url}{id}/")
        self.assertEqual(resp.status_code, 404)