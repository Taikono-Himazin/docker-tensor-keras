FROM tensorflow/tensorflow:1.13.1-gpu-py3-jupyter
LABEL maintainer='username'

WORKDIR /jupyter

RUN pip --no-cache-dir install \
	keras\
	opencv-python\
	pillow\
	tqdm
RUN pip install jupyter_contrib_nbextensions

EXPOSE 8888

COPY jupyter_notebook_config.py ../root/.jupyter/
