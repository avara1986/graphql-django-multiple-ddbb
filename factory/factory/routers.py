# -*- coding: utf-8 -*-
"""
    Project: Lowi.es
    Authors: Paradigma Digital S.L.
"""
from django.conf import settings


class DatabaseAppsRouter(object):

    def db_for_read(self, model, **hints):
        print(model._meta.model_name)
        print(settings.DATABASE_MODEL_READ_MAPPING)
        if model._meta.model_name in settings.DATABASE_MODEL_READ_MAPPING:
            print("llega")
            return settings.DATABASE_MODEL_READ_MAPPING[model._meta.model_name]
        return None

    def db_for_write(self, model, **hints):

        if model._meta.model_name in settings.DATABASE_MODEL_WRITE_MAPPING:
            return settings.DATABASE_MODEL_WRITE_MAPPING[model._meta.model_name]
        return None

    def allow_relation(self, obj1, obj2, **hints):

        db1 = settings.DATABASE_MODEL_MIGRATE_MAPPING.get(obj1._meta.model_name)
        db2 = settings.DATABASE_MODEL_MIGRATE_MAPPING.get(obj2._meta.model_name)
        if db1 and db2:
            return db1 == db2
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if db in settings.DATABASE_MODEL_MIGRATE_MAPPING.values():
            return settings.DATABASE_MODEL_MIGRATE_MAPPING.get(model_name) == db
        elif model_name in settings.DATABASE_MODEL_MIGRATE_MAPPING:
            return False
