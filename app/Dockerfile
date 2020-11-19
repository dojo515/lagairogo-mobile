FROM rlesouef/alpine-python-3.5
WORKDIR /lagairogo-mobile-priceband/app/
COPY . .
RUN pip3 install -r requiremets.txt
EXPOSE 5001
ENTRYPOINT ["PYTHON"]
CMD ["app.py"]