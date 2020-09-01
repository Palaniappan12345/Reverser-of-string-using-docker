FROM python:3 
COPY . .
RUN pip3 install flask
EXPOSE 5001 
ENTRYPOINT [ "python" ] 
CMD [ "reverser.py" ] 
