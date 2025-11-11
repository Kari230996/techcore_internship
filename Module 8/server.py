import asyncio
import grpc
import author_pb2
import author_pb2_grpc


class AuthorService(author_pb2_grpc.AuthorServiceServicer):
    async def GetAuthor(self, request, context):
        print(f"Запрос получен: id={request.id}")
        return author_pb2.AuthorReply(id=request.id, name="John Doe")


async def serve():
    server = grpc.aio.server()
    author_pb2_grpc.add_AuthorServiceServicer_to_server(
        AuthorService(), server)
    listen_addr = "[::]:50051"
    server.add_insecure_port(listen_addr)
    await server.start()
    print(f"gRPC-сервер запущен на {listen_addr}")
    await server.wait_for_termination()

if __name__ == "__main__":
    asyncio.run(serve())
