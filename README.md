# Requirements
*(tested on) python 3.8*

Install pip requirements using `requirements.txt`:

```sh
pip install -r requirements.txt
```

# How to Run
## Start the Todo App Service
```sh
python main.py 8081 /tmp/db
```

- The service will listen for requests on port `8081`
- `/tmp/db` is the path to the "db" file used by the service to store the todo tasks.

## Issue REST requests (w/ JSON payloads)
- Responses to requests that affect a bulk of tasks (e.g. delete) will include an `ids` field with a list of identifiers that match the tasks that have been affected as a result of the operation. For example, if you delete two notes, `123` and `567` and only note with id `123` exists, the response `ids` field will contain only `123`.

- The service supports both plain JSON, and protobuf payloads. It discerns the type according to the `Content-Type` header, and sends back the response in the format that corresponds to `Accept` header (JSON is used by default).

### Create a Task
To create a new task:
```sh
curl -i \
    -x POST \
    --data '{ "task": { "contents": "buy milk" } }' \
    -H "Content-Type: application/json" \
    -H "Accept: application/json" \
    http://localhost:8081/create
```

### Get All Tasks
To retrieve all tasks:
```sh
curl -i -x GET http://localhost:8081/getall
```

### Mark Tasks as Done
To mark tasks with ids `123`, `456` as "DONE":


```sh
curl -i \
    -x PUT \
    --data '{ "ids": [123, 456] }' \
    -H "Content-Type: application/json" \
    -H "Accept: application/json" \
    http://localhost:8081/done
```

### Delete Tasks
To delete tasks with ids `123`, `456`:

```sh
curl -i \
    -x POST \
    --data '{ "ids": [123, 456] }' \
    -H "Content-Type: application/json" \
    -H "Accept: application/json" \
    http://localhost:8081/delete
```

## Tests
```sh
python -m unittest -v test.test_todoapp
python -m unittest -v test.test_storage
```

## Compile Protobuf
run `protoc` while in `syte-ai/proto` directory:

```sh
cd proto/
protoc -I=. --python_out=. api.proto
```

# Design Overview

- `TodoAppSvc` - Flask service code. A wrapper that handles marshalling/unmarshalling of response/request payloads, input sanitization, and error handling.

- Both JSON and protobuf payloads are supported (using `flask_pbj.py`)

- `Storage` is an interface that can be implemented in order to add new storage options for the todo app. `BadStorage` is used for testing storage layer throwing exceptions, `InMemStorage` is used for testing, and `TinyDBStorage` is used as persistent storage that backs the todo app service.


# TODO
- [ ] Storage layer shouldn't raise random exceptions depending on underlying implementation.
- [ ] Bulk Create operation
- [ ] use enums for http status codes instead of integers
- [ ] `pbj` is kinda janky, maybe replace (fixed >4 bugs so far)
- [ ] pagination of tasks: getall method is easy, but can potentially become a performance bottleneck.
