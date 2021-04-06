

# `flask_pbj.py` modifications
1. if client doesn't send "accepted content type" header, pbj cannot respond: changed it so it respond in json by default.
2. For responses to be sent in protobuf, only 4xx error codes are considered "errors" and use the `errors=pb.ApiErr` annotation to marshal the responses used in `pbj.api` (example: on db error, which should be classified as 5xx error since it is indeed a server error, if we want to indicate that to gRPC clients, we can't). Changed so that 5xx error codes are also marshalled into protobuf.


# Possible Improvements
- [ ] Use something "larger" for an `id` type (currently 32 bits, treated as `int32`)
- [ ] Need to improve error reporting for bulk operations (e.g. `/create` will return -1 as `id` for tasks that could not be created, because of db error for example, instead of something more informative)
- [ ] Storage layer shouldn't raise random exceptions depending on underlying implementation.
- [ ] Performing bulk operations on
- [ ] use the `errors=` feature of `pbj` (in `pbj.api` annotation)
- [ ] use enums for http status codes instead of integers
- [ ] `pbj` is kinda janky: had to manually fix two issues
