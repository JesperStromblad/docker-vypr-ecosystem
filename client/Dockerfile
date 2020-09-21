# Docker file for creating a container for RV tutorial 2020


# Date of creation - 18.09.2020
# Maintainer -  omjaved

# OS package, without tag means we will always take the latest os image
FROM python:2.7 AS base

# Install dependencies
RUN apt-get update && apt-get install -y \
curl python-pip sqlite3


RUN pip install virtualenv
RUN virtualenv venv --python=python2.7

# Source virtual environment
CMD source venv/bin/activate

# Current working directory to store repositories

# Cloning visualisation tool

RUN git clone https://github.com/pyvypr/VyPR-visualisation.git


WORKDIR VyPR-visualisation/

RUN git checkout 318e9ec21776fafb9c3616e72ce4465e99911c14

RUN pip install -r requirements.txt

RUN git clone https://github.com/pyvypr/VyPRServer.git

# Cloning Verdict server

WORKDIR VyPRServer/

RUN git checkout 6a12c9c3710cab2ff4832dd9d85d723f8b1e25a4

RUN rm -rf verdicts.db events.db

RUN sqlite3 verdicts.db < verdict-schema.sql

RUN sqlite3 events.db < app/events/events.sql

RUN pip install -r requirements.txt

# Cloning VyPR core

RUN git clone https://github.com/pyvypr/VyPR.git

WORKDIR VyPR/

# Setting the directory to test project
WORKDIR ../../test-project/

RUN export PYTHONPATH=$PYTHONPATH:.

RUN pip install -r requirements.txt

RUN git clone https://github.com/pyvypr/VyPRLocal-py2.git VyPR

CMD python VyPR/instrument.py

CMD python main.py



WORKDIR ../src/

