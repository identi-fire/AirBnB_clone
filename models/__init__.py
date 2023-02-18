<<<<<<< HEAD
"""
creates a unique file storaage instance
"""

from models.engine import file_storage
=======
#!/usr/bin/python3
"""creates a unique file storaage for Application"""


from models.engine.file_storage import FileStorage
>>>>>>> cd9d38ee7216e648933f0eda01a10010b3bfcb06


storage = file_storage.FileStorage()
storage.reload()
