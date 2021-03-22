FROM tensorflow/tensorflow:latest-py3 as base

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .

ENV PATH="/opt/venv/bin:$PATH"

ENV FLASK_APP=app.py

RUN apt-get update -y && apt-get install -y --no-install-recommends build-essential gcc libsndfile1

######################## DEBUGGER #################################

FROM base as debug

RUN pip install ptvsd

WORKDIR /app

CMD python -m ptvsd --host 0.0.0.0 --port 5678 --wait --multiprocess -m flask run -h 0.0.0 -p 5000

######################## PRODUCTION ###############################

FROM base as prod

CMD flask run -h 0.0.0 -p 5000