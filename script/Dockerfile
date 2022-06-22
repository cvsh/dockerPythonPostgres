FROM python:3.9
WORKDIR /code
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY getData.py getData.py
COPY keys.json keys.json
CMD ["python", "getData.py"]