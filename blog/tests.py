from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Category

class Test_Create_Post(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        test_user1 = User.objects.create_user(username='test_user1')
        test_post = Post.objects.create(category_id=1, title='Post Title', text='Post Content', slug='post-title', author_id=1, status='published')

    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        category = Category.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        text = f'{post.text}'
        status = f'{post.status}'
        self.assertEqual(author, 'test_user1')
        self.assertEqual(title, 'Post Title')
        self.assertEqual(text, 'Post Content')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), "Post Title")
        self.assertEqual(str(category), "django")
