FROM python:3
COPY . /app
WORKDIR /app
RUN pip uninstall py-cord
RUN pip uninstall discord.py
RUN pip install py-cord 
RUN apt update && apt install -y git build-essential libffi-dev openssl libssl-dev && pip install --upgrade -r requirements.txt
CMD python -u main.py
