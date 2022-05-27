FROM ubuntu
RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip3 install dash
RUN pip3 install pandas
RUN pip3 install matplotlib
RUN pip3 install numpy
RUN pip3 install openpyxl
COPY obesidad.xlsx /
COPY app.py /
EXPOSE 8050
