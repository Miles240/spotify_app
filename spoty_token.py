import requests
import base64

# Replace with your client ID and client secret
client_id = '98e4cec5c8ec4c5196eab297805847b5'
client_secret = '620146e44fbc44f7a7978674aee1acde'

# Spotify's token endpoint
auth_url = 'https://accounts.spotify.com/api/token'

# Encode client ID and client secret
auth_str = f"{client_id}:{client_secret}"
b64_auth_str = base64.b64encode(auth_str.encode()).decode()

# Set headers and data for the POST request
auth_headers = {
    'Authorization': f'Basic {b64_auth_str}',
    'Content-Type': 'application/x-www-form-urlencoded'
}
auth_data = {
    'grant_type': 'client_credentials'
}

# Send POST request to get access token
auth_response = requests.post(auth_url, headers=auth_headers, data=auth_data)
auth_response_data = auth_response.json()

# Extract the access token from the response
access_token = auth_response_data.get('access_token')

if not access_token:
    raise Exception('Failed to retrieve access token')

print('Access token:', access_token)
