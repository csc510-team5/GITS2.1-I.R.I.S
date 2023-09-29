# Use an official Ubuntu as a parent image
FROM ubuntu:latest

# Update the package list and install dependencies
RUN apt update && apt install -y python3 python3-pip git

RUN git clone https://github.com/csc510-team5/GITS2.1-I.R.I.S.git /app
RUN ln -s /app/code /root/code # necessary for gits list

# Install any needed packages specified in requirements.txt
RUN pip install -r app/requirements.txt

# Run the project_init.sh script as part of the Docker image build
RUN bash app/configurations/project_init.sh

# Source the .bashrc file if needed
RUN . ~/.bashrc

