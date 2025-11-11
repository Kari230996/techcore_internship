import asyncio
import grpc
import author_pb2
import author_pb2_grpc


async def run():
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = author_pb2_grpc.AuthorServiceStub(channel)
        response = await stub.GetAuthor(author_pb2.AuthorRequest(id=1))
        print(f"Ответ от сервера: {response.name}")


if __name__ == "__main__":
    asyncio.run(run())
