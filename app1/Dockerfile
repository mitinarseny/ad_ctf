FROM python:3.7.3-alpine3.9
LABEL maintainer="mitinarseny@gmail.com"

ARG UID=1000
ARG GID=1000
ENV UID=${UID}
ENV GID=${GID}
RUN addgroup -g 2000 app1_user \
    && adduser -u 2000 -G app1_user -s /bin/sh -D app1_user

USER app1_user

WORKDIR app1
COPY ./requirements.txt .

RUN pip install --upgrade --user pip && pip install --user -r requirements.txt

COPY . .

CMD ["python", "run.py"]
