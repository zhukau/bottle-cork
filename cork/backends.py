# Cork - Authentication module for tyyhe Bottle web framework
# Copyright (C) 2013 Federico Ceratto and others, see AUTHORS file.
# Released under GPLv3+ license, see LICENSE.txt
#
# Backends API - used to make backends available for importing
#
from json_backend import JsonBackend
from mongodb_backend import MongoDBBackend
from sqlalchemy_backend import SqlAlchemyBackend
from sqlite_backend import SQLiteBackend
