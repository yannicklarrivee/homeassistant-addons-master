ARG BUILD_FROM
FROM $BUILD_FROM

# Add env
ENV LANG C.UTF-8

# Setup base
RUN apk add --no-cache jq curl findutils python3=3.8.10-r0 python3-dev=3.8.10-r0 py-pip && \
    pip3 install requests python-dateutil==2.6.1 pytz==2018.3

# Copy data
COPY run.sh /
COPY keep_last.py /
RUN ["chmod", "a+x", "/run.sh"]
RUN curl "https://raw.githubusercontent.com/andreafabrizi/Dropbox-Uploader/master/dropbox_uploader.sh" -o /dropbox_uploader.sh
RUN ["chmod", "a+x", "/dropbox_uploader.sh"]
WORKDIR /

CMD [ "/run.sh" ]
