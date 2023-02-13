FROM ubuntu
CMD apt update -y && apt install python3,python3-pip,aws-cli
COPY . .
CMD pip3 install -r requirements.txt
CMD sh preConfig.sh
CMD python3 main.py
