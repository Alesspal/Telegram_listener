import asyncio
import signal
import telegram_utils
import os
from dotenv import load_dotenv
from telethon import events
from telethon.tl.types import InputPeerChannel, Channel
from pprint import pprint

async def main():

	# Load environment variables
	dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
	load_dotenv(dotenv_path)

	print("Authentification")
	try:
		client = await telegram_utils.auth()
	except Exception as e:
		print("Error while authenticating the client : ", e)
		return

	# Configuration of signals
	# print("Configuration of signals")
	# loop = asyncio.get_event_loop()
	# for sig in {signal.SIGTERM, signal.SIGINT}:
	# 	loop.add_signal_handler(sig, lambda: asyncio.create_task(telegram_utils.close_session(client)))

	# Démarrage de la session
	print("client has connected to the Telegram session")
	async with client:
		# Informations du compte connecté
		account_info = await client.get_me()
		print ("account info :", account_info)

		# Get the ids of the channels
		# print("Get the info of the channels :")
		# channels_info = await telegram_utils.get_channels_id(client)
		# pprint(channels_info)

		# Get the entity of the channel
		entity = await client.get_entity(int(os.getenv('TELEGRAM_CHANNEL_ID')))
		@client.on(events.NewMessage(chats=entity))
		async def new_message_listener(event):
			print(event.raw_text)

		# waiting for the session to be closed
		await client.run_until_disconnected()
	print("client has disconnected from the Telegram session")

asyncio.run(main())