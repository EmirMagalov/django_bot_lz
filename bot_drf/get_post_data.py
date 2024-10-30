import aiohttp
API_POSTS_ADD="http://host.docker.internal:8000/api/posts/"
API_POSTS_USER="http://host.docker.internal:8000/api/posts/getuserpost/?user_id="
API_POSTS_MESSAGE_ID="http://host.docker.internal:8000/api/posts/putadmin/?message_id="
async def getpostusers(user_id):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{API_POSTS_USER}{user_id}") as response:
            if response.status == 200:
                products = await response.json()
                result = []
                for product in products:
                    result.append(product)
                return result



            else:
                print("error")

async def getonepost(id):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{API_POSTS_ADD}{id}/") as response:
            if response.status == 200:
                products = await response.json()
                result = []
                for product in products:
                    result.append(product)
                return result



            else:
                print("error")

async def putonepost(id,data):
    async with aiohttp.ClientSession() as session:
        async with session.put(f"{API_POSTS_ADD}{id}/",json=data) as response:
            if response.status == 200:
                return await response.json()



            else:
                print("error")

async def putonepostadmin(message_id,data):
    async with aiohttp.ClientSession() as session:
        async with session.put(f"{API_POSTS_MESSAGE_ID}{message_id}",json=data) as response:
            if response.status == 200:
                return await response.json()



            else:
                print("error")
async def del_post(id):
    async with aiohttp.ClientSession() as session:
        async with session.delete(f"{API_POSTS_ADD}{id}/") as response:
            if response.status == 200:

                return await response.json()
            else:
                error_message = await response.text()
                print(f"Error: {response.status}, {error_message}")
                return None

async def postposts(data):
    async with aiohttp.ClientSession() as session:
        async with session.post(API_POSTS_ADD, json=data) as response:
            if response.status == 201:

                return await response.json()
            else:
                error_message = await response.text()
                print(f"Error: {response.status}, {error_message}")
                return None