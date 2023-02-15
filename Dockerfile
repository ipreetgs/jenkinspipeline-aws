FROM ubuntu
RUN apt update -y && apt install -y python3 python3-pip awscli
COPY . .
RUN pip3 install -r requirements.txt
RUN sh preConfig.sh
ARG MY_VARIABLE=default_value
CMD python3 main.py ${MY_VARIABLE}
