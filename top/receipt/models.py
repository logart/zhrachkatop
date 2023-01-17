from enum import Enum

from django.db import models
import json

# Create your models here.

class CheckType(str, Enum):
    KITCHEN = 'kitchen'
    CLIENT = 'client'


class CheckStatus(str, Enum):
    NEW = 'new'
    RENDERED = 'rendered'
    PRINTED = 'printed'


class Printer(models.Model):
    name = models.CharField(max_length=200)
    api_key = models.CharField(max_length=200)
    check_type = models.CharField(max_length=7,
                                  choices=[(checkType, checkType.value) for checkType in CheckType],
                                  default=CheckType.KITCHEN)
    point_id = models.IntegerField()


class Check(models.Model):
    printer_id = models.ForeignKey(Printer, on_delete=models.CASCADE)
    type = models.CharField(max_length=7,
                            choices=[(checkType, checkType.value) for checkType in CheckType])
    order = models.JSONField()
    status = models.CharField(max_length=8, choices=[(checkStatus, checkStatus.value) for checkStatus in CheckStatus])
    pdf_file = models.FileField()
