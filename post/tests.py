from django.contrib.auth.models import User
from django.test import TestCase
from post.models import Post, Comment


class PostTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="poras", password="password")
        post = Post.objects.create(
            title="AI pros and cons",
            content="AI has caused a disruption in the lives of developers",
            author=user
        )
        Comment.objects.create(post=post, author=user, text="It is actually scary")

    def test_post_and_comments_creation(self):
        post = Post.objects.get(title="AI pros and cons")
        comment = Comment.objects.get(text="It is actually scary")
        self.assertEqual(post.__str__(), 'AI pros and cons')
        self.assertEqual(comment.__str__(), 'It is actually scary')
