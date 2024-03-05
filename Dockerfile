FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# update the package list and install the required dependencies
# RUN apt-get update && apt-get install -y \
#     clang \
#     libjpeg-turbo-dev \
#     libwebp-dev \
#     python-dev \
#     zlib1g-dev \
#     && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the dependencies write in the requirements file
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory in the container
COPY /src /app

# Command to run on container start
CMD [ "python", "./main.py" ]
