# pull official base image
FROM python:3.11-slim

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p static
# install psycopg2 dependencies
# RUN apk update
RUN apt update 
# RUN apt install -y virtualenv
# RUN virtualenv venv
RUN apt install -y ffmpeg
# RUN apt install -y python3-pip libpango-1.0-0 libharfbuzz0b libpangoft2-1.0-0 libffi-dev libjpeg-dev libopenjp2-7-dev

    # && apk add python3-opencv
# && apk add postgresql-dev gcc python3-dev musl-dev

# RUN export LDFLAGS="-L/usr/local/opt/libffi/lib"  && export CPPFLAGS="-I/usr/local/opt/libffi/include"

# install dependencies
RUN pip3 install --upgrade pip
# RUN pip3 install --upgrade pip setuptools wheel
# RUN pip3 install opencv-python numpy scipy
COPY ./development.txt .
COPY ./requirements.txt .
RUN pip install -r development.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]