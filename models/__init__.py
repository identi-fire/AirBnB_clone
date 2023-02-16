"""
creates a unique file storaage instance
"""

from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
