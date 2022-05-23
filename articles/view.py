def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = func(*args, **kwargs)
            print('=' * 50)
        return wrap
    return wrapper

class UserInterface:
    @add_title('Enter User Data')
    def wait_user_answer(self):
        print("Ввод пользовательских данных ".center(50, "="))
        print("Действие со Статъьями")
        print("1 - Create Article"
              "\n2 - View Articles"
              "\n3 - View Definition article"
              "\n4 - Deleting Article"
        "\nq - Выход Из Программы")
        user_answer = input("Выберите Вариант Действия: ")
        print("=" * 50)
        return user_answer

    def add_user_article(self):
        dict_article = {
            'Название': None,
            'author': None,
            'Number Char': None,
            'Description': None
        }
        print(" Creation Article: ".center(50, '='))
        for key in dict_article:
            dict_article[key] = input(f'Input {key} article')
        print("=" * 50)
        return dict_article

    def show_all_articles(self, articles):
        print(" List articles: ".center(50, "="))
        for ind, article in enumerate(articles, start=1):
            print(f"{ind}. {articles}")
            print('+' * 50)

    @add_title('Enter Name Article: ')
    def user_article(self):
        user_article = input("Enter Name Article: ")
        return user_article()

    @add_title('View article: ')
    def show_single_article(self, article):
        for key in article:
            print(f"{key} article = {article[key]}")

    def show_incorrect_title_error(self, user_title):
        print(f"Article with Name {user_title} Not Exist")

    @add_title
    def remove_single_article(selfself, article):
        print(f"Article {article} - Was deleted")
    @add_title
    def show_incorrect_answer_error(self, answer):
        print(f"Variant with Name {answer} Not Exists")