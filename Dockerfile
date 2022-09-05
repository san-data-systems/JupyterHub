FROM continuumio/anaconda3
ARG PY=3.9
RUN conda install -c conda-forge jupyterhub mlflow -y
COPY config.py /etc/config.py

COPY entrypoint.sh /etc/entrypoint.sh
RUN chmod +x /etc/entrypoint.sh

COPY auth.py /tmp/auth.py
RUN cat /tmp/auth.py >> /opt/conda/lib/python${PY}/site-packages/jupyterhub/auth.py

COPY kernel.json /opt/conda/share/jupyter/kernels/python3/kernel.json
EXPOSE 8888
CMD /etc/entrypoint.sh


