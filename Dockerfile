# set the Base Image from which your image will be built on
FROM python:3.8 
# create a directory called flask-circleci in root. This directory will contain the code which currentlt resides in
RUN mkdir /test_app
WORKDIR /test_app
# copy your requirements file to the directory you just created
COPY requirements.txt /test_app
RUN pip install -r requirements.txt


# copy the current directory in you local machine to /flask-circleci inyour image
ADD . /test_app

EXPOSE 5000

CMD ["python", "main.py"] 