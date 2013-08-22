# -*- coding: utf-8 -*-

from .. import Service
from .models import User


class UsersService(Service):
    __model__ = User
