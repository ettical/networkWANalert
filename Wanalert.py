from plyer import notification
import requests


def get_wan_ip_address():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        if response.status_code == 200:
            data = response.json()
            ip_address = data.get('ip')
            return ip_address
    except requests.exceptions.RequestException:
        pass

    return None
 
if __name__ == "__main__":
    wan_ip_address = get_wan_ip_address()
    if wan_ip_address:
        notification.notify(
        title="WAN IP Address",
        message=wan_ip_address,
        app_icon=None  # Set the path to your custom app icon if desired
    )    


