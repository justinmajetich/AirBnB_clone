#!/usr/bin/python3

from sqlalchemy import create_engine

engine = create_engine("mysql://root:root@localhost")

engine.execute("INSERT INTO e")
