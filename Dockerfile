FROM python:slim
COPY app.py /app/
COPY tail.sh /app/
WORKDIR /app
#CMD python app.py
CMD ./tail.sh | python app.py
