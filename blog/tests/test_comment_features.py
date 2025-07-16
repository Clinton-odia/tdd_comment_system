"""
Test user comment
"""

from django.test import TestCase
from django.urls import reverse
from blog.models import Post


class PostListViewTest(TestCase):
    def test_displays_all_posts(self):
        # create two dummy post
        Post.objects.create(title="First post", body="hello world")
        # Call the URL where the posts will be listed
        response = self.client.get(reverse("post_list"))
        # check if post list exist
        self.assertContains(response, "First post")


class PostDetailViewTest(TestCase):
    def test_displays_post_detail(self):
        # create a post
        Post.objects.create(title="First post", body="hello world")

        # reverse to post detail view using the post's ID
        url = reverse("post_detail", args=[Post.id])
        # client.get that URL
        response = self.client.get(url)

        # assert that the body text is in the response
        self.assertContains(response, "hello world")
