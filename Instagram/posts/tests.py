# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

# from django.test import TestCase
# from .models import Post
# from accounts.models import User

# # Create your tests here.
# class PostTestCases(TestCase):

#     def setUp(self):
#     	user = User.objects.get()
#         Post.objects.create(title='aem j',content='aem j bijivar')

#     def test_example(self):
#         p = Post.objects.get(title='aem j')
#         self.assertEqual(p.content,'aem j bijivar')

#     def test_example2(self):
#         count = Post.objects.all().count()
#         self.assertEqual(count,1)

#     def test_example3(self):
#         self.assertEqual(5,3+3)
from __future__ import unicode_literals
import unittest
from django.test import TestCase
from accounts.models import User
from posts.models import Post
from accounts.views import login_view,register_view,followlist_view,follow_view,profile_follower
from .views import post_list,post_delete
from Instagram.settings import *
from django.test.client import Client
from django.test import RequestFactory
import pytest

# import pytest
# from mixer.backend.django import mixer
# pytestmark = pytest.mark.django_db

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': ':memory:',
#     }
# }
# client = Client()
# class TestFunctionsMethods(TestCase):
	
# 	def setUp(self):
# 		self.user = User.objects.create(username="Jany")
# 		self.post = Post.objects.create(user = self.user, title = "First Post")
# 		self.c = Client()

# 	def test_login(self):
# 		#user = User.objects.get(username="Jany")
# 		#print(user.id)
# 		self.assertEqual(self.user.username,"Jany")

# 	def test_post_creation(self):
# 		self.assertEqual(self.post.title,"First Post")

# 	def test_loginview(self):
# 		self.c.login(username='Jany', password='1234')
# 		response = self.c.get('/login/')
# 		self.assertEqual(response.status_code,200)
# 		# req = RequestFactory().get('/login/')
# 		# resp = login_view.as_view()(req)
# 		# assertEqual(response.status_code,200)

# 	def test_sample1(self):
# 		response = self.c.get('/register/')
# 		self.assertEqual(response.status_code,200)


# class TestUserModel(TestCase):

# 	def setUp(self):
# 		user = User.objects.create(username="Jany",email= "jany@gmail.com")
# 		post = Post.objects.create(user=user,title='First Insta Post')

# 	def test_username(self):
# 		user = User.objects.get(id=1)
# 		field_label = user.username
# 		self.assertEquals(field_label,'Jany')

# 	def test_email(self):
# 		user = User.objects.get(id=1)
# 		email = user.email
# 		self.assertEqual(email,"jany@gmail.com")

# 	def test_Instapost(self):
# 		posttitle = Post.objects.get(id=1)
# 		title = posttitle.title
# 		self.assertEqual(title,"First Insta Post")

class Testviewsfunctions(TestCase):

	def setUp(self):
		User.objects.create(password="1234abcd1",email= "jany@gmail.com")
		self.factory = RequestFactory()
		self.client = Client()

	def test_login(self):
		request = self.factory.get('/login/')
		response = login_view(request)
		self.assertEqual(response.status_code, 200)

	def test_register(self):
		request = self.factory.get('/register/')
		response = register_view(request)
		self.assertEqual(response.status_code, 200)

	# def test_followlist(self):
	# 	request = self.factory.get('/follow/')
	# 	response = followlist_view(request)
	# 	self.assertEqual(response.status_code,200)

	# def test_followuser(self):
	# 	request = self.factory.get('/followuser/')
	# 	response = follow_view(request,id=1)
	# 	self.assertEqual(response.status_code,200)

	# def test_profilefollower(self):
	# 	request = self.factory.get('/profile_follower/')
	# 	response = profile_follower(request,id=1)
	# 	self.assertEqual(response.status_code,200)

	# def test_postdelete(self):
	# 	request = self.factory.get('/'+id+'/delete/')
	# 	response = post_delete(request,1)
	# 	self.assertEqual(response.status_code,200)






if __name__ == '__main__':
    unittest.main()