#!/usr/bin/python3
import json
from datetime import datetime
from models import *


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        self.reload()

    def all(self, cls=None):
        if cls is None:
            return FileStorage.__objects

        storage = {}
        for obj_id in FileStorage.__objects:
            obj_cls = FileStorage.__objects[obj_id].__class__.__name__
            if cls == obj_cls:
                storage[obj_id] = FileStorage.__objects[obj_id]

        return storage

    def new(self, obj):
        if obj is not None:
            FileStorage.__objects[obj.id] = obj

    def save(self):
        store = {}
        for k in FileStorage.__objects.keys():
            store[k] = FileStorage.__objects[k].to_json()

        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as fd:
            fd.write(json.dumps(store))

    def update(self, cls, obj_id, key, new_value):
        if obj_id not in FileStorage.__objects:
            return 0

        obj = FileStorage.__objects[obj_id]
        setattr(obj, key, new_value)
        return 1

    def reload(self):
        try:
            with open(FileStorage.__file_path,
                      mode="r+", encoding="utf-8") as fd:
                FileStorage.__objects = {}
                temp = json.load(fd)
                for k in temp.keys():
                    cls = temp[k].pop("__class__", None)
                    cr_at = temp[k]["created_at"]
                    cr_at = datetime.strptime(cr_at, "%Y-%m-%d %H:%M:%S.%f")
                    up_at = temp[k]["updated_at"]
                    up_at = datetime.strptime(up_at, "%Y-%m-%d %H:%M:%S.%f")
                    FileStorage.__objects[k] = eval(cls)(temp[k])
        except Exception as e:
            pass

    def delete(self, obj=None):
        if obj is None:
            return

        FileStorage.__objects.pop(obj.id, 0)

    def close(self):
        self.save()
