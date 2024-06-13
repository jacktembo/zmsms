import requests


base_url = 'https://zmsms.online/api/v1'


class SMSClient:
    """Python client library for Zambia SMS Gateway API.
    """

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def send_sms(self, message: str, sender_id: str, phone_numbers: list):
        """Send SMS message to one or more phone numbers.

        Args:
            message (str): The message to be sent.
            sender_id (str): The sender ID to be used.
            phone_numbers (list): A list of phone numbers to send the message to.

        Returns:
            dict: A dictionary containing the response from the API.
        """

        headers = { 'Content-Type': 'application/json' }

        data = {
        "auth": {
            "username": self.username,
            "password": self.password
        },
        "sender_id": sender_id,
        "message": message,
        "phone_numbers": phone_numbers
        }

        r = requests.post(f"{base_url}/bulksms", json=data, headers=headers)

        return r.json()


    def check_balance(self):
        """Check the balance of the account.

        Returns:
            dict: A dictionary containing the response from the API.
        """

        headers = { 'Content-Type': 'application/json' }

        data = {
            "username": self.username,
            "password": self.password
        }

        r = requests.post(f"{base_url}/balance", json=data, headers=headers)

        return r.json()
    

    def list_sender_ids(self):
        """List the available sender IDs.

        Returns:
            dict: A dictionary containing the response from the API.
        """

        headers = { 'Content-Type': 'application/json' }

        data = {
            "username": self.username,
            "password": self.password
        }

        r = requests.post(f"{base_url}/sender-ids", json=data, headers=headers)

        return r.json()
    
