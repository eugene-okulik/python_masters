FROM python
ENV COOL_PORT 8080
ENV COOL_IP 0.0.0.0
EXPOSE 8080/tcp
ENV COOL_LOG log
RUN mkdir "log"
RUN mkdir "/usr/share/cool-app/"
RUN echo "ST5 site" > /usr/share/cool-app/cool-text.txt
RUN git clone https://github.com/eugene-okulik/cool_web_app.git
CMD ["python3", "cool_web_app/run.py"]