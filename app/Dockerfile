# pull official base image
FROM python:3

# set work directory
# create the appropriate directories
# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup --system app && adduser --system app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir -p $APP_HOME
RUN mkdir -p $APP_HOME/static
RUN mkdir -p $APP_HOME/media

RUN chown app:app $HOME
RUN chown app:app $APP_HOME
RUN chown app:app $APP_HOME/static
RUN chown app:app $APP_HOME/media

WORKDIR $APP_HOME

#RUN mkdir /code
#RUN mkdir /code/staticfiles
#WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY /requirements.txt $APP_HOME
RUN pip install -r requirements.txt

# copy entrypoint-prod.sh
COPY ./entrypoint.sh $APP_HOME

# copy project
COPY . $APP_HOME

# chown all the files to the app user
#RUN chown -R app:app $APP_HOME
RUN chown -R app:app .

# change to the app user
USER app

# run entrypoint.sh
ENTRYPOINT ["/home/app/web/entrypoint.sh"]
