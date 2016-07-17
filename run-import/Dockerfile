FROM carbolymer/python3:pandas-0.18.1
WORKDIR /import
COPY requirements.txt /tmp
RUN pip3 install --requirement /tmp/requirements.txt
COPY db.hdf ./
COPY import.py ./
ENTRYPOINT ["python3"]
CMD ["-u", "./import.py"]
