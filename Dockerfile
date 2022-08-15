FROM continuumio/anaconda3
ARG PY=3.9
RUN conda install -c conda-forge jupyterhub mlflow -y
COPY config.py /etc/config.py
COPY auth.py /tmp/auth.py
RUN cat /tmp/auth.py >> /opt/conda/lib/python${PY}/site-packages/jupyterhub/auth.py
EXPOSE 8888
CMD ["jupyterhub", "-f", "/etc/config.py"]

