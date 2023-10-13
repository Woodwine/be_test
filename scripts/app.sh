#!/bin/bash

alembic revision --autogenerate -m "Create"

alembic upgrade head

python3 run.py