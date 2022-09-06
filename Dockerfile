FROM python:3.9

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

COPY ./main.py /app

COPY ./InputModel.py /app

COPY ./model_built_fapi.pkl /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
