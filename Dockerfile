#
FROM python:3.12

#
WORKDIR /code

#
COPY ./requirements.txt /code/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#
COPY main.py /code/app
COPY model.pkl /code/app

#
CMD ["uvicorn", "code:app", "--host", "0.0.0.0", "--port", "80"]