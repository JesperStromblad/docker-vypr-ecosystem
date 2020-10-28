import docker
client = docker.from_env()

for container in client.containers.list():

	if container.image.tags[0] == 'vyprjupyter:latest':

		log = container.logs()

		start = log.index('http')

		url_with_characters = log[start:440]

		end_of_url = url_with_characters.index('[')

		get_token = url_with_characters[:end_of_url]

		start_token = get_token.index('?')

		token = get_token[start_token:]

		url = "http://127.0.0.1:9005/"+token

		print (url)

