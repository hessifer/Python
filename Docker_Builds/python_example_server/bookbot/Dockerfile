# Build form a slim Debian/Linux image
FROM debian:stable-slim

# Copy our code into the image
COPY main.py main.py

# Copy our data dependencies
COPY books/ books/

# Update apt
RUN apt update
RUN apt upgrade -y

# Install build tooling
RUN apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev

# Download Python interpreter code and unpack it
RUN wget https://www.python.org/ftp/python/3.12.7/Python-3.12.7.tgz
RUN tar -xf Python-3.12.*.tgz

# Build the Python interpreter
RUN cd Python-3.12.7 && ./configure --enable-optimizations && make && make altinstall

# Run our Python script
CMD ["python3.12", "main.py"]
