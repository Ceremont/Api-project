import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_user(user_id, session):
    url = f"{BASE_URL}/users/{user_id}"
    try:
        response = session.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data["name"]
    except requests.exceptions.RequestException:
        return "Пользователь не найден"


def get_post(post_id, session):
    url = f"{BASE_URL}/posts/{post_id}"
    try:
        response = session.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data["title"]
    except requests.exceptions.RequestException:
        return "Пост не найден"


def create_post(title, body, user_id, session):
    url = f"{BASE_URL}/posts"
    payload = {
        "title": title,
        "body": body,
        "userId": user_id
    }

    try:
        response = session.post(url, json=payload, timeout=5)
        if response.status_code == 201:
            data = response.json()
            return f"Пост успешно создан, id: {data.get('id')}"
        return "Ошибка создания"
    except requests.exceptions.RequestException:
        return "Ошибка создания"

def get_all_users(session):
    url = f"{BASE_URL}/users"
    try:
        response = session.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return [user["name"] for user in data]
    except requests.exceptions.RequestException:
        return "Error"

def get_comments_by_post(post_id, session):
    url = f"{BASE_URL}/posts/{post_id}/comments"
    params = {"postId": post_id}
    try:
        response = session.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        return [comment["email"] for comment in data]
    except requests.exceptions.RequestException:
        return "Error"

def show_menu():
    print("\n1. Get user")
    print("2. Get post")
    print("3. Create post")
    print("4. Get all users")
    print("5. Get comments by post id")
    print("6. Exit")


def get_int_input(prompt):
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            print("Нужно ввести число")


def main():
    session = requests.Session()

    while True:
        show_menu()
        choice = input("Choose: ")

        if choice == "1":
            user_id = get_int_input("Give user id: ")
            user_name = get_user(user_id, session)
            print(user_name)

        elif choice == "2":
            post_id = get_int_input("Give post id: ")
            post_title = get_post(post_id, session)
            print(post_title)

        elif choice == "3":
            title = input("Give post title: ")
            body = input("Give post body: ")
            user_id = get_int_input("Give post user id: ")

            result = create_post(title, body, user_id, session)
            print(result)

        elif choice == "4":
            users = get_all_users(session)
            for index, user in enumerate(users,start=1):
                print(f"{index}. {user}")

        elif choice == "5":
            post_id = get_int_input("Give post id: ")
            comments = get_comments_by_post(post_id, session)
            for index, comment in enumerate(comments,start=1):
                print(f"{index}. {comment}")

        elif choice == "6":
            print("Bye")
            break

        else:
            print("Неверный выбор")


if __name__ == "__main__":
    main()