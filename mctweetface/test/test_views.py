# pylint: disable=unused-variable,expression-not-assigned

from expecter import expect

from mctweetface import views


def describe_index():

    def it_returns_a_string():
        expect(type(views.index())) == str
