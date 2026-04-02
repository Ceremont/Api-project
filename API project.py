import requests


def get_user(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data["name"]
    except requests.exceptions.RequestException:
        return "Пользователь не найден"


def get_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data["title"]
    except requests.exceptions.RequestException:
        return "Пост не найден"


def create_post(title, body, user_id):
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": title,
        "body": body,
        "userId": user_id
    }

    try:
        response = requests.post(url, json=payload, timeout=5)

        if response.status_code == 201:
            data = response.json()
            return f"Пост успешно создан, id: {data.get('id')}"
        return "Ошибка создания"
    except requests.exceptions.RequestException:
        return "Ошибка создания"


while True:
    print("\n1. Get user")
    print("2. Get post")
    print("3. Create post")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        user_id = input("Give user id: ")
        user_name = get_user(user_id)
        print(user_name)

    elif choice == "2":
        post_id = input("Give post id: ")
        post_title = get_post(post_id)
        print(post_title)

    elif choice == "3":
        title = input("Give post title: ")
        body = input("Give post body: ")
        user_id = input("Give post user id: ")
        result = create_post(title, body, user_id)
        print(result)

    elif choice == "4":
        print("Bye")
        break

    else:
        print("Неверный выбор")