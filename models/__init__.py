#!/usr/bin/python3
"""creates a unique file storaage for Application"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
