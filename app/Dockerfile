FROM rlesouef/alpine-python-3.5
WORKDIR /lagairogo-mobile/app/
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5001
ENTRYPOINT ["PYTHON"]
CMD ["app.py"]
