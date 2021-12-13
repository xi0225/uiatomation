import grpcio
import
import grpc

def run():    # 连接 rpc 服务器    channel = grpc.insecure_channel('localhost:50051')    # 调用 rpc 服务    stub = helloworld_pb2_grpc.GreeterStub(channel)    response = stub.SayHello(helloworld_pb2.HelloRequest(name='test'))    print("Greeter client received: " + response.message)if __name__ == '__main__':    run()

    python - m
    grpc_tools.protoc - -python_out =.--grpc_python_out =.-I.helloworld.proto