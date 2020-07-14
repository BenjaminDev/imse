FROM nvidia/cuda

ENV DEBIAN_FRONTEND=noninteractive

ARG PROJECT=imse

ARG USERNAME=user
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME
# RUN groupadd -r  $USERNAME -g 901 && useradd -u 901 -r -g  $USERNAME
RUN sudo apt update -y
RUN apt install -y \ 
                ffmpeg\
                zsh\
                curl\
                wget\
                unzip\
                git
               
RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt install python3.8   python3.8-venv python3.8-dev -y
RUN curl https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py
RUN python3.8 /tmp/get-pip.py

ENV PATH="/home/${USERNAME}/.local/bin:${PATH}"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION=1.0.9

# the user we're applying this too (otherwise it most likely install for root)
USER $USERNAME

RUN pip install --upgrade pip setuptools wheel \
    && pip install "poetry==$POETRY_VERSION"


ENV VIRTUAL_ENV=/home/$USERNAME/.virtualenvs/$PROJECT
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /tmp
COPY poetry.* pyproject.toml ./

RUN python3.8 -m venv $VIRTUAL_ENV
RUN python3.8 -m pip install --upgrade pip setuptools
RUN poetry  install -vvv

WORKDIR /workspaces

# RUN chown -R $USERNAME:$USERNAME $VIRTUAL_ENV
# terminal colors with xterm
ENV TERM xterm
# set the zsh theme
ENV ZSH_THEME agnoster

# run the installation script  
RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true


ENV DEBIAN_FRONTEND=dialog
