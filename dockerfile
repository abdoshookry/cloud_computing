FROM python

COPY . /assignment
WORKDIR /assignment

CMD python books.py