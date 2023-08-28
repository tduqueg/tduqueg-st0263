from flask import Flask, jsonify, request
import grpc
from generated import microservices_pb2, microservices_pb2_grpc

app = Flask(__name__)

GRPC_SERVER = '54.237.135.137:50051'


@app.route('/list_files', methods=['GET'])
def list_files():
    with grpc.insecure_channel(GRPC_SERVER) as channel:
        stub = microservices_pb2_grpc.MicroservicesStub(channel)
        response = stub.ListFiles(microservices_pb2.ListRequest())
    return jsonify(files=response.files)


@app.route('/search_files', methods=['GET'])
def search_files():
    pattern = request.args.get('pattern', '')
    with grpc.insecure_channel(GRPC_SERVER) as channel:
        stub = microservices_pb2_grpc.MicroservicesStub(channel)
        response = stub.SearchFiles(
            microservices_pb2.SearchRequest(pattern=pattern))
    return jsonify(files=response.files)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
