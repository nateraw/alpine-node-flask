FROM mhart/alpine-node:12.14.1
COPY package.json .
RUN npm install
FROM tiangolo/meinheld-gunicorn-flask:python3.7
COPY --from=0 node_modules /app/static
COPY requirements.txt /tmp
RUN pip install -U pip && \
	pip install -r /tmp/requirements.txt
COPY ./app /app