FROM python:3.8.12


RUN python -m  pip install pip==21.3.1 
RUN python -m  pip install rasa

WORKDIR /app

COPY . .
#RUN rasa train nlu

RUN rasa train nlu
# set the user to run, do not run as root
USER 1011

# set entrypoint for interactive shells 

ENTRYPOINT ["rasa"]


CMD ["run", "--enable-api", "--port", "8080"]


