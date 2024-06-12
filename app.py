from waw import API, AllAPIs, Debug
import json


def main():
    config = {
        "temp-mail": "temp-mail.json"
    }
    apis = AllAPIs(config)

    data = apis.call("temp-mail", "get_mx_token")
    email = data["mailbox"]
    token = data["token"]

    apis.reinit_with_token("temp-mail", token)

    data = apis.call("temp-mail", "get_messages").json()
    print(email)
    print(data)


if __name__ == "__main__":
    main()
