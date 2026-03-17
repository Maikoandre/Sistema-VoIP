import requests
from asterisk.agi import AGI

agi = AGI()

caller = agi.env.get('agi_callerid')

response = requests.get(f'http://127.0.0.1:8000/api/extensions/')

agi.verbose(f"Caller ID: {caller}")
agi.verbose(f"Response from API: {response.text}")