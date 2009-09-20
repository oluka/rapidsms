#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4


from rapidsms.tests.scripted import TestScript
from app import App


class TestApp (TestScript):
    apps = (App,)

    testDefaultResponse = """
        1 > LOL
        1 < Sorry, we could not understand that message.
    """
