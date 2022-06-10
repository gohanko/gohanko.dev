FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=utf8

WORKDIR /backend/

RUN pip install --upgrade pip
COPY ./backend/requirements.txt /backend/
RUN pip install -r requirements.txt

COPY ./infrastructure/docker/backend/entrypoint.sh /backend/
RUN sed -i 's/\r$//g' /backend/entrypoint.sh
RUN chmod +x /backend/entrypoint.sh

COPY ./backend/ /backend/

ENTRYPOINT ["/backend/entrypoint.sh"]