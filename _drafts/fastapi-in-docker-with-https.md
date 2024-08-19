# Running a FastAPI service in a container over HTTPS

We wanted to deidentify medical free text using [philter-lite][2] in a web service, so we used [FastAPI][1].


## Docker

The service runs nicely inside Docker. Here's the Dockerfile used to build the container image:

```Dockerfile
FROM python:3.11-slim-bullseye as builder

WORKDIR /workdir

ARG PIP_EXTRA_INDEX_URL

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -U pip \
    && PIP_EXTRA_INDEX_URL=$PIP_EXTRA_INDEX_URL pip install --no-cache-dir -r requirements.txt \
    && python -c 'import nltk; nltk.download("averaged_perceptron_tagger", download_dir="/usr/share/nltk_data")'

COPY deidentifier deidentifier

EXPOSE 80

CMD ["fastapi", "run", "deidentifier", "--port", "80"]
```

```sh
docker build --file docker/Dockerfile --tag deidentifier:latest .
```

```sh
docker run -d --name deidentifier --rm -p 80:80 deidentifier:latest
```

Access the API using [HTTPie][4]:

```sh
http http://127.0.0.1/
```

...or use [curl][5] if you prefer:

```sh
curl http://127.0.0.1/
```

```sh
http post http://localhost:80/deidentify @data/example.json
```


### Running as a unprivileged user

[Why not run the service as root?][101]. [Best practice guides from docker][103] and [elsewhere][102] say it's better to use an unprivileged user.

```Dockerfile
FROM python:3.11-slim-bullseye as builder

WORKDIR /workdir

ARG PIP_EXTRA_INDEX_URL

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -U pip \
    && PIP_EXTRA_INDEX_URL=$PIP_EXTRA_INDEX_URL pip install --no-cache-dir -r requirements.txt \
    && python -c 'import nltk; nltk.download("averaged_perceptron_tagger", download_dir="/usr/share/nltk_data")'

COPY deidentifier deidentifier

ARG GROUP_ID=1048
ARG USER_ID=1227
.
RUN addgroup --gid ${GROUP_ID} storagegroup \
    && useradd -m -s /bin/sh -g ${GROUP_ID} -u ${USER_ID} deidentifieruser

USER deidentifieruser
EXPOSE 80

CMD ["fastapi", "run", "deidentifier", "--port", "80"]
```

### SSL

We can serve our API over HTTPS.

```Dockerfile
FROM python:3.11-slim-bullseye as builder

WORKDIR /workdir

ARG PIP_EXTRA_INDEX_URL

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -U pip \
    && PIP_EXTRA_INDEX_URL=$PIP_EXTRA_INDEX_URL pip install --no-cache-dir -r requirements.txt \
    && python -c 'import nltk; nltk.download("averaged_perceptron_tagger", download_dir="/usr/share/nltk_data")'

COPY deidentifier deidentifier

COPY ssl/key.pem ssl/key.pem
COPY ssl/cert.pem ssl/cert.pem
RUN chgrp storagegroup ssl/*

ARG GROUP_ID=1048
ARG USER_ID=1227
RUN addgroup --gid ${GROUP_ID} storagegroup \
    && useradd -m -s /bin/sh -g ${GROUP_ID} -u ${USER_ID} deidentifieruser

USER deidentifieruser
EXPOSE 443

CMD ["uvicorn", "deidentifier:app", "--host", "0.0.0.0", "--port", "443", "--ssl-keyfile", "ssl/key.pem", "--ssl-certfile", "ssl/cert.pem"]
```

If the above is in a file called `DockerfileSSL`, we can build it:

```sh
docker build --file docker/DockerfileSSL --tag deidentifier-ssl:latest .
```

...and run the container, exposing port 443:

```sh
docker run -d --rm --name deidentifier -p 443:443  deidentifier-ssl:latest
```

Now we access our service over HTTPS and need to provide a means for the client to follow the chain of certs up to some source of trust.

```sh
http --verify ssl/my-ca-bundle.pem https://127.0.0.1/
```

If you want to inpect what TLS versions your service is offering, use the following command:

```sh
curl -Iiv --tlsv1.1 --cacert ssl/my-ca-bundle.pem  https://127.0.0.1/
```

That produces a bunch of output which should contain something similar to `SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384`.


### Serving both HTTP and HTTPS endpoints

This can be done, but may not be a good idea.

```sh
docker run -d -p 80:80 -p 443:443 \
--name deidentifier \
deidentifier-ssl:latest \
sh -c "uvicorn deidentifier:app --ssl-certfile ssl/cert.pem --ssl-keyfile ssl/key.pem --host 0.0.0.0 --port 443 --workers 1 & uvicorn deidentifier:app --host 0.0.0.0 --port 80 --workers 1"
```

[1]: https://fastapi.tiangolo.com/
[2]: https://github.com/SironaMedical/philter-lite
[4]: https://httpie.io/
[5]: https://curl.se/docs/manpage.html

[101]: https://stackoverflow.com/questions/68155641/should-i-run-things-inside-a-docker-container-as-non-root-for-safety
[102]: https://dev.to/hazarnenni/docker-best-practices-55j0
[103]: https://docs.docker.com/build/building/best-practices/

