def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = func(*args, **kwargs)
            print('=' * 50)
            return output

        return wrap

    return wrapper


class UserInterface:
    @add_title('Ввод пользовательских данных')
    def wait_user_answer(self):
        # print("Ввод пользовательских данных ".center(50, "="))
        print("Действие со Статъьями")
        print("1 - Создание статьи"
              "\n2 - Просмотр со статьями"
              "\n3 - Просмотр определенной статьи"
              "\n4 - Deleting Article"
              "\nq - Выход Из Программы")
        user_answer = input("Выберите Вариант Действия: ")
        # print("=" * 50)
        return user_answer
    @add_title('Создание статьи:')
    def add_user_article(self):
        dict_article = {
            'название': None,
            'автор': None,
            'количество знаков': None,
            'описание': None
        }
        # print(" Создание статьи: ".center(50, '='))
        for key in dict_article:
            dict_article[key] = input(f'Введите {key} статьи')
        # print("=" * 50)
        return dict_article

    @add_title('Спмсок статей:')
    def show_all_articles(self, articles):
        # print(" Список статей: ".center(50, "="))
        for ind, article in enumerate(articles, start=1):
            print(f"{ind}. {article}")
        # print('+' * 50)

    @add_title('Ввод названия статьи:')
    def get_user_article(self):
        user_article = input("Введите название статьи: ")
        return user_article

    @add_title('Просмотр статьи: ')
    def show_single_article(self, article):
        for key in article:
            print(f"{key} статьи - {article[key]}")

    @add_title('Сообщение Об Ошибке:')
    def show_incorrect_title_error(self, user_title):
        print(f"Статьи с названием {user_title} Не Существует")
    #
    # @add_title
    # def remove_single_article(selfself, article):
    #     print(f"Article {article} - Was deleted")
    #
    # @add_title
    # def show_incorrect_answer_error(self, answer):
    #     print(f"Variant with Name {answer} Not Exists")
