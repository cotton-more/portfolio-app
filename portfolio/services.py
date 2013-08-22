# -*- coding: utf-8 -*-

from .projects import ProjectService, CardService
from .users import UsersService

projects = ProjectService()
cards = CardService()

users = UsersService()
