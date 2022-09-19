ARG BUILD_FROM
FROM $BUILD_FROM

# Setup base
RUN apk add --no-cache nginx openssl

RUN printf "%s%s%s%s\n" \
    "@nginx " \
    "http://nginx.org/packages/mainline/alpine/v" \
    `egrep -o '^[0-9]+\.[0-9]+' /etc/alpine-release` \
    "/main" \
    | tee -a /etc/apk/repositories

RUN curl -o /tmp/nginx_signing.rsa.pub https://nginx.org/keys/nginx_signing.rsa.pub
RUN mv /tmp/nginx_signing.rsa.pub /etc/apk/keys/
#RUN apk add --no-cache nginx-module-njs@nginx
#RUN apk add --no-cache nginx-mod-http-naxsi@nginx
RUN apk add --no-cache nginx-mod-http-js


# Copy data
COPY data/run.sh /
COPY data/nginx.conf /etc/
COPY data/hass_auth_script.js /etc



CMD [ "/run.sh" ]
