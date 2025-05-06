from django.test import TestCase
from .forms import CommentForm


class TestForms(TestCase):
    def test_comment_form_valid(self):
        form = CommentForm(data={"body": "This is a test comment."})
        self.assertTrue(form.is_valid())

    def test_comment_form_invalid(self):
        form = CommentForm(data={'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn("body", form.errors)
        