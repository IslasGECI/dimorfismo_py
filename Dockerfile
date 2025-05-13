FROM python:3
WORKDIR /workdir
COPY . .
RUN pip install --upgrade pip && pip install \
    black \
    descarga-datos \
    flake8 \
    geci-test-tools \
    mutmut==3.*\
    mypy \
    pandas-stubs \
    pylint \
    pytest \
    pytest-cov \
    requests

RUN make install
