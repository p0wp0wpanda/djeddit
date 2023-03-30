from django.urls import reverse
from blog.models import Post, Category
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class PostTests(APITestCase):

    def test_can_view_post_list(self):
        """
        Test if we get a HTTP 200 when trying to view all post
        """
        url = reverse('blog_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_does_return_created_post_data(self):
        """
        Test if 
        """
        self.test_category = Category.objects.create(name='django')

        self.testuser1 = User.objects.create_user(
            username='test_user1', password='123456789')

        data = {"title": "new", 
                "author": 1,
                "text": "new"}
        
        url = reverse('blog_api:listcreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 5)
