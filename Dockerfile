FROM python:3

WORKDIR /usr/src/app/

RUN git clone https://github.com/elichad/ontology_task.git ontology_task/
WORKDIR ontology_task/

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "ontology_data/main.py"]
# show help if no command-line arguments provided
CMD ["-h"] 
