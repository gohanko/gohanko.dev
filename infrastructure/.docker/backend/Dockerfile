FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=utf8

WORKDIR /backend/

RUN pip install --upgrade pip
COPY requirements.txt /backend/
RUN pip install -r requirements.txt

COPY ./.docker/production/backend/entrypoint.sh /backend/
RUN sed -i 's/\r$//g' /backend/entrypoint.sh
RUN chmod +x /backend/entrypoint.sh

COPY . /backend/

ENTRYPOINT ["/backend/entrypoint.sh"]