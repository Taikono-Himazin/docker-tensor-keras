FROM tensorflow/tensorflow:1.13.1-gpu-py3-jupyter
LABEL maintainer='username'

WORKDIR /jupyter

COPY jupyter_notebook_config.py ../root/.jupyter/jupyter_notebook_config.py

RUN pip --no-cache-dir install \
	keras\
	opencv-python\
	pillow\
	tqdm

EXPOSE 8888

COPY jupyter_notebook_config.py ../root/.jupyter/
