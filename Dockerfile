FROM continuumio/miniconda3
WORKDIR /app

RUN apt-get update && apt-get upgrade -也
COPY environment.yml .
RUN conda update -n base -c defaults conda
RUN conda env create -f environment.yml
COPY ./ /app

RUN echo "conda init bash" >> $HOME/.bashrc
RUN echo "conda activate wa2_brussels" >> $HOME/.bashrc
