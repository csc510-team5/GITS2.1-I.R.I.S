# Use an official Ubuntu as a parent image
FROM ubuntu:latest

# Update the package list and install dependencies
RUN apt update && apt install -y python3 python3-pip git curl gpg

# Install github CLI
RUN curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | gpg --dearmor -o /usr/share/keyrings/githubcli-archive-keyring.gpg
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | tee /etc/apt/sources.list.d/github-cli.list > /dev/null
RUN apt update && apt install -y gh

RUN git clone https://github.com/csc510-team5/GITS2.1-I.R.I.S.git /app
RUN ln -s /app/code /root/code # necessary for gits list

# Install any needed packages specified in requirements.txt
RUN pip install -r app/requirements.txt

# Run the project_init.sh script as part of the Docker image build
RUN bash app/configurations/project_init.sh

# Source the .bashrc file if needed
RUN . ~/.bashrc

