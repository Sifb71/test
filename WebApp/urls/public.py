#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Sifb71'
from WebApp.handlers.public.index import index

urls = [
    ("/", index.IndexHandler, None, "index"),

    ("/signup", index.SignupHandler, None, "signup"),

    ("/logout", index.LogoutHandler, None, "logout"),


]
