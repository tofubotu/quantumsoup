FROM alpine:3.12.0

RUN apk add --no-cache --update \
    samba-common-tools \
    samba-client \
    samba-server \
    shadow

RUN useradd -M -s /sbin/nologin leone

RUN smbpasswd -a -n leone && \
    echo -e "test123\ntest123" | smbpasswd -s leone

COPY smb.conf /etc/samba/smb.conf

EXPOSE 139/tcp 445/tcp

CMD ["smbd", "--foreground", "--log-stdout", "--no-process-group"]

