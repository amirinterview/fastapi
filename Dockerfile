FROM python:3.6
RUN pip install fastapi uvicorn[standard]
COPY . /app
CMD cd /app && uvicorn --host 0.0.0.0 main:app --reload
