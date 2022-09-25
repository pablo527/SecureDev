FROM alpine:3.10 AS build

RUN apk --no-cache add ca-certificates
RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

RUN mkdir -p /home/appuser && HOME=/home/appuser \
 && chmod -R 0755 /home/appuser    \
 && addgroup -S -g 10101 appuser   \
 && adduser -S -D -s /sbin/nologin -h /home/appuser -G appuser appuser

WORKDIR /home/appuser
COPY . .
RUN pip3 install -r requirements.txt

ENV USER_DB=security
ENV PASSWORD_DB=secrect

USER appuser
EXPOSE 5003
ENTRYPOINT [ "python3" ]

CMD [ "src/app.py" ]