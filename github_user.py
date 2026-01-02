import sys
import requests
import argparse

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
        "Account Created":data.get("created_at","Not available")
    }
def main():
    parser = argparse.ArgumentParser(
        description="Github User Info CLI"
    )

    parser.add_argument(
        "username",
        help="Github username to fatch"
    )
    args = parser.parse_args()

    try:
        raw_data = fatch_github_user(args.username)
        if raw_data is None:
            print(f'user {args.username} is not found')
            sys.exit(1)
        
        user_info = extrect_user_info(raw_data)
        print("\nGithub User Info")
        print("-------------------------")
        for key,value in user_info.items(): 
            print(f"{key} : {value}")
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)
    
if __name__ == "__main__":
    main()

