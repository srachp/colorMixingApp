FROM python:3.6-stretch

RUN pip3 install virtualenv

ENV VIRTUAL_ENV=/venv
RUN python3 -m virtualenv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY src/requirements.txt /app/src/
RUN . $VIRTUAL_ENV/bin/activate && $VIRTUAL_ENV/bin/pip3 install -r /app/src/requirements.txt

# Create logs directory and other directories needed
RUN mkdir -p /logs/
RUN mkdir -p /app/src/templates/

# Run the application:
COPY src/config.py /app/src/
COPY src/main.py  /app/src/
COPY templates/* /app/src/templates/
CMD ["python", "/app/src/main.py"]
