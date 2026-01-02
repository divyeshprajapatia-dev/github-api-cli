import requests

def fatch_github_user(username):
    url = f'http://api.github.com/users/{username}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None
    
def extrect_user_info(data):
    return{
        "Username":data.get("login","Not available"),
        "Account Type":data.get("type","Not available"),
        "Name":data.get("name","Not available"),
        "Location":data.get("location","Not available"),
        "Public Repos":data.get("public_repos","Not available"),
        "Followers":data.get("followers","Not available"),
        "Following":data.get("following","Not available"),
        "Account Created":data.get("created_at","Not available"),
    }
    
if __name__ == "__main__":
    row_data = fatch_github_user("divyeshprajapatia-dev")

    if row_data == None:
        print("user not found")
    else:
        user_info = extrect_user_info(row_data)
        print(user_info)

