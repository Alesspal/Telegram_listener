from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os

async def auth():
	"""
	Authentification to the Telegram API
	"""
	# Load environment variables
	api_id = os.getenv('TELEGRAM_API_ID')
	api_hash = os.getenv('TELEGRAM_API_HASH')
	session = os.getenv('TELEGRAM_SESSION')

	# Check if the environment variables are defined
	if api_id is None or api_hash is None:
		raise Exception("Telegram API ID and/or API HASH are not defined in the environment variables")

	# Create a client
	if session is None:
		client = TelegramClient(StringSession(), api_id, api_hash)
	else:
		client = TelegramClient(StringSession(session), api_id, api_hash)
	return client

async def close_session(client):
	"""
	Close the session with the Telegram API
	"""
	print("Client trying to disconnect from the Telegram session")
	await client.log_out()
	print("Client Telegram disconnected")

async def get_channels_id(client):
	"""
	Get the ids of the channels
	"""
	info = []
	async for dialog in client.iter_dialogs():
		entity_info = {
			'id': dialog.id,
			'title': dialog.name,
			'username': dialog.entity.username,
			'verified': dialog.entity.verified,
			'type': type(dialog.entity).__name__
		}
		info.append(entity_info)
	return info
