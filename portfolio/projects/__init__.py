# -*- coding: utf-8 -*-

from .. import Service
from .models import Project, Card


class ProjectService(Service):
    __model__ = Project


class CardService(Service):
    __model__ = Card
