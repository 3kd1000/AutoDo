from django.test import TestCase
from django.test.client import Client
from django.conf import settings
from django.template import loader
from .models import Project
from .models import User


# Test Cases for Django Database Model. Written by JS
class ProjectModelTestCase(TestCase):

    def setUp(self):
        u = User.objects.create(email="test")
        Project.objects.create(repository_url="obj1", description='before statement', user=u)
        Project.objects.create(repository_url="obj2", branch_count=100, is_enrolled=False, user=u)
        self.wrong_type_int_to_bool = False
        self.wrong_type_int_to_str = "5"
        self.wrong_type_bool_to_str = "False"
        self.wrong_type_bool_to_int = 3
        self.wrong_type_str_to_int = 4
        self.wrong_type_str_to_bool = True
        self.correct_str = "test statement"

    def test_wrong_data_type_int_to_str_should_raise_type_error(self):
        obj = Project.objects.get(repository_url="obj1")
        obj.branch_count = self.wrong_type_int_to_str
        self.assertRaises(TypeError, obj.update)

    def test_wrong_data_type_int_to_bool_should_raise_type_error(self):
        obj = Project.objects.get(repository_url="obj1")
        obj.branch_count = self.wrong_type_int_to_bool
        self.assertRaises(TypeError, obj.update)

    def test_wrong_data_type_bool_to_int_should_raise_type_error(self):
        obj = Project.objects.get(repository_url="obj1")
        obj.is_enrolled = self.wrong_type_bool_to_int
        self.assertRaises(TypeError, obj.enroll)

    def test_wrong_data_type_bool_to_str_should_raise_type_error(self):
        obj = Project.objects.get(repository_url="obj1")
        obj.is_enrolled = self.wrong_type_bool_to_str
        self.assertRaises(TypeError, obj.enroll)

    def test_wrong_data_type_str_to_int_should_raise_type_error(self):
        obj = Project.objects.get(repository_url="obj1")
        obj.description = self.wrong_type_str_to_int
        self.assertRaises(TypeError, obj.desc_update, self.correct_str)

    def test_wrong_data_type_str_to_bool_should_raise_type_error(self):
        obj = Project.objects.get(repository_url="obj1")
        obj.description = self.wrong_type_str_to_bool
        self.assertRaises(TypeError, obj.desc_update, self.correct_str)

    def test_wrong_param_data_type_str_to_int_should_raise_type_error(self):
        obj = Project.objects.get(repository_url="obj1")
        obj.description = self.correct_str
        self.assertRaises(TypeError, obj.desc_update, self.wrong_type_str_to_int)

    def test_wrong_param_data_type_str_to_bool_should_raise_type_error(self):
        obj = Project.objects.get(repository_url="obj1")
        obj.description = self.correct_str
        self.assertRaises(TypeError, obj.desc_update, self.wrong_type_str_to_bool)

    def test_desc_update(self):
        obj1 = Project.objects.get(repository_url="obj1")
        obj1.desc_update("test statement")
        self.assertEqual(obj1.description, "test statement")

    def test_branch_count_update(self):
        obj = Project.objects.get(repository_url="obj2")
        obj.update()
        self.assertEqual(obj.branch_count, 101)

    def test_enroll(self):
        obj = Project.objects.get(repository_url="obj2")
        obj.enroll()
        self.assertEqual(obj.is_enrolled, True)


class UserModelTestCase(TestCase):

    def setUp(self):
        self.correct_email = "test@test.com"
        self.wrong_email = "abcd.com"
        self.wrong_length_email = "@"
        self.correct_account_ID = "test_account"
        self.wrong_account_ID = " "

    def test_wrong_email_should_raise_value_error(self):
        self.assertRaises(ValueError, User, self.wrong_email, self.correct_account_ID)

    def test_wrong_length_email_should_raise_value_error(self):
        self.assertRaises(ValueError, User, self.wrong_length_email, self.correct_account_ID)

    def test_correct_email_and_account_ID_should_not_raise_value_error(self):
        u = User(self.correct_email, self.correct_account_ID)
        self.assertIsNotNone(u)

    def test_wrong_account_ID_should_raise_value_error(self):
        self.assertRaises(ValueError, User, self.correct_email, self.wrong_account_ID)


class ViewTestCase(TestCase):
    # To be implemented
    def setUp(self):
        self.client = Client()

    def test_login_page_switch(self):
        response = self.client.get("/")
        #   Status Code Check
        self.assertEqual(response.status_code, 200)
        #   Template Check
        self.assertTemplateUsed(response, 'AutoDoApp/login.html')
        #   Context value Check
        self.assertEqual(response.context['client_id'], settings.GIT_HUB_URL)

    def test_main_page_switch(self):
        session = self.client.session
        session['oauth'] = 'test_oauth'
        session.save()
        response = self.client.get("/main/")
        #   Template Check
        self.assertTemplateUsed(response, 'AutoDoApp/main.html')

    def test_main_status_code(self):
        session = self.client.session
        session['oauth'] = 'test_oauth'
        session.save()
        response = self.client.get("/main/")
        #   Status Code Check
        self.assertEqual(response.status_code, 200)

    def test_main_context_content(self):
        session = self.client.session
        session['oauth'] = 'test_oauth'
        session.save()
        response = self.client.get("/main/")
        #   Context value Check
        self.assertEqual(response.context['client_id'], settings.GIT_HUB_URL)
