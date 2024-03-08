#!/usr/bin/python3
"""This begins the process in the package"""
from models.file_storage import FileStorage

storage = FileStorage()
storage.reload()
