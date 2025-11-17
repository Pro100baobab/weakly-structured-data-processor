import json
import random


class ExampleData:
    """
    Класс для хранения возможных экземпляров данных о пользователях
    """
    name_list_example = ["Артем", "Максим", "Дмитрий", "Александр", "Сергей", "Андрей", "Алексей", "Иван", "Кирилл",
                         "Михаил",
                         "Никита", "Егор", "Даниил", "Павел", "Роман", "Владимир", "Тимофей", "Матвей", "Глеб", "Олег",
                         "Ярослав", "Федор", "Константин", "Артур", "Борис", "Василий", "Виктор", "Григорий", "Денис",
                         "Евгений", "Анна", "Мария", "Елена", "Ольга", "Наталья", "Ирина", "Светлана", "Татьяна",
                         "Екатерина",
                         "Юлия", "Анастасия", "Дарья", "Ксения", "Александра", "Полина", "София", "Вероника", "Валерия",
                         "Виктория", "Кристина", "Алина", "Маргарита", "Ульяна", "Алиса", "Диана", "Евгения", "Карина",
                         "Людмила", "Надежда", "Вера"]
    mail_address_example = [
        "user123@mail.ru", "ivan.petrov@yandex.ru", "ekaterina.smirnova@gmail.com",
        "alexander1985@inbox.ru", "maria.ivanova@list.ru", "sergey.kuznetsov@rambler.ru",
        "olga.sidorova@bk.ru", "dmitry.volkov@yahoo.com", "natalya.orlova@hotmail.com",
        "andrey.popov@protonmail.com", "svetlana.fedorova@outlook.com", "mikhail.novikov@icloud.com",
        "tatyana.morozova@aol.com", "pavel.belov@zoho.com", "elena.kozlova@yandex.com",
        "viktor.medvedev@mail.com", "irina.lebedeva@gmx.com", "konstantin.egorov@seznam.cz",
        "anna.pavlova@live.com", "roman.sokolov@me.com", "yulia.vorobeva@orange.fr",
        "artem.frolov@sfr.fr", "ekaterina.nesterova@free.fr", "maxim.davydov@wanadoo.fr",
        "daria.romanova@laposte.net", "kirill.makarov@tele2.fr", "alexey.orshanskiy@sapo.pt",
        "lyudmila.kozlova@web.de", "nikita.baranov@t-online.de", "vera.popova@gmx.de",
        "georgiy.vasilev@freenet.de", "sofia.ignateva@arcor.de", "timur.zaytsev@alice.it",
        "valeriya.belyaeva@libero.it", "vladimir.sorokin@virgilio.it", "galina.nikitina@tin.it",
        "stanislav.mironov@aliceadsl.fr", "larisa.guseva@neuf.fr", "igor.savin@club-internet.fr",
        "nadezhda.titova@bbox.fr", "denis.fomin@numericable.fr", "evgeniya.sergeeva@rediffmail.com",
        "grigoriy.petuhov@bigpond.com", "polina.volkova@ntlworld.com", "fedor.denisov@blueyonder.co.uk",
        "veronika.efimova@talktalk.net", "boris.gromov@plus.net", "karina.mihaylova@sky.com",
        "leonid.panin@btinternet.com", "elvira.zaharova@virginmedia.com", "vadim.erohin@o2.co.uk",
        "margarita.soloveva@ee.co.uk", "rostislav.vinogradov@three.co.uk", "zoya.kruglova@vodafone.com",
        "german.lobanov@orange.co.uk", "tamara.bobrova@tiscali.co.uk", "valentin.golubev@ntlworld.com",
        "regina.sorokina@live.co.uk", "vitaliy.melnikov@googlemail.com", "albina.chernova@ymail.com",
        "eduard.isaev@rocketmail.com", "lilia.komarova@att.net", "yaroslav.burov@bellsouth.net",
        "kseniya.golikova@charter.net", "vsevolod.rybakov@comcast.net", "arzamaskaya.ina@verizon.net",
        "rodion.voloshin@cox.net", "elena1987@optimum.net", "vasiliy.shuvalov@earthlink.net",
        "irina.shiroka@juno.com", "gennadiy.muhin@windstream.net", "marina.volkova@frontier.com",
        "anatoliy.lapin@centurylink.net", "oksana.belova@embarqmail.com", "valeriy.gorshkov@cableone.net",
        "lyubov.orlova@bright.net", "viktorija.antonova@netzero.net", "arkadiy.biryukov@suddenlink.net",
        "evdokiya.fomina@cfl.rr.com", "vladislav.pestov@twc.com", "snezhana.kozlova@insightbb.com",
        "gordon.freeman@half-life.com", "tony.stark@starkindustries.com", "bruce.wayne@wayne-enterprises.com",
        "peter.parker@dailybugle.com", "clark.kent@dailyplanet.com", "selina.kyle@catwoman.com",
        "wade.wilson@deadpool.com", "natasha.romanoff@shield.gov", "steve.rogers@avengers.com",
        "thor.odinson@asgard.com", "hermione.granger@hogwarts.edu", "harry.potter@gryffindor.com",
        "john.smith@matrix.com", "neo.anderson@zion.org", "leia.organa@alderaan.gov",
        "luke.skywalker@jedi-order.org", "anakin.skywalker@tatooine.net", "padme.amidala@naboo.gov"
    ]
    # Упрощенный вариант без проверки числа дней в месяце
    registration_data_example = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
    ]
    # Упрощенный вариант без проверки registration_data_example
    last_auth_example = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        [2024, 2025]
    ]
    status_example = ["подтвержден", "не подтвержден"]

    publication_name_example = [
        "Основы программирования на Python", "Искусство цифровой фотографии", "Кулинарные шедевры мира",
        "Путеводитель по Европе", "Йога для начинающих", "Финансовая грамотность", "История древнего мира",
        "Современное искусство", "Астрономия для всех", "Психология общения", "Дизайн интерьера",
        "Здоровое питание", "Маркетинг в социальных сетях", "Самооборона для женщин", "Английский язык за 30 дней",
        "Вязание крючком", "Садоводство для начинающих", "Детская психология", "Фитнес дома",
        "Инвестиции в криптовалюту", "Рисование акварелью", "Уход за домашними растениями",
        "Основы первой помощи", "Фотография на smartphone", "Медитация и mindfulness",
        "Путешествия по России", "Книга рецептов выпечки", "Основы веб-дизайна",
        "Уход за кожей лица", "История моды", "Шахматы для начинающих", "Основы игры на гитаре",
        "Рукоделие для детей", "Кинология: воспитание собаки", "Автомобили для чайников",
        "Основы макияжа", "Путеводитель по Азии", "Флористика для начинающих",
        "Основы программирования на Java", "Йога для беременных", "Книга о кошках",
        "Основы финансового планирования", "Фотография природы", "Кулинария для студентов",
        "Основы игры на пианино", "Саморазвитие личности", "История музыки",
        "Ремонт в квартире своими руками", "Основы бодибилдинга", "Книга о путешествиях",
        "Основы программирования на C++", "Искусство каллиграфии", "Уход за волосами",
        "Основы игры в покер", "Книга о здоровом образе жизни", "Фотография портретов",
        "Основы программирования на JavaScript", "Кулинария для веганов", "Йога для детей"
    ]
    publication_description_example = [
        "Подробное руководство по основам программирования на Python с примерами и упражнениями.\nИдеально подходит для начинающих разработчиков.\nВключает практические задания и проекты.",
        "Исчерпывающее пособие по цифровой фотографии.\nТехники съемки, работа со светом и композицией.\nПодходит как для любителей, так и для профессионалов.",
        "Сборник лучших рецептов со всего мира.\nОт итальянской пасты до японских суши.\nПодробные инструкции и красивые фотографии блюд.",
        "Полный путеводитель по европейским странам.\nДостопримечательности, культура, советы путешественникам.\nМаршруты и рекомендации по бюджетным поездкам.",
        "Пошаговое руководство по йоге для начинающих.\nОсновные асаны, дыхательные техники, программы тренировок.\nПодходит для любого уровня подготовки.",
        "Основы финансовой грамотности для современного человека.\nБюджетирование, инвестиции, планирование расходов.\nПрактические советы и кейсы.",
        "Увлекательное путешествие в древний мир.\nЦивилизации, культура, великие империи.\nИсторические факты и археологические находки.",
        "Исследование современного искусства XX-XXI веков.\nОсновные направления, художники, техники.\nАнализ ключевых произведений.",
        "Доступное введение в астрономию для всех возрастов.\nСозвездия, планеты, телескопы.\nНаблюдение за звездным небом.",
        "Практическое руководство по эффективному общению.\nПсихология отношений, конфликтология, коммуникативные техники.\nПримеры из реальной жизни.",
        "Основы дизайна интерьера для создания уютного пространства.\nЦветовые решения, планировка, выбор мебели.\nСоветы профессионалов.",
        "Принципы здорового питания и составления рациона.\nРецепты, пищевая ценность, советы по приготовлению.\nДля поддержания здоровья и энергии.",
        "Стратегии маркетинга в социальных сетях для бизнеса.\nSMM, контент-план, таргетированная реклама.\nКейсы успешных кампаний.",
        "Практическое руководство по самообороне для женщин.\nОсновные приемы, техники безопасности, психологическая подготовка.\nДля уверенности в себе.",
        "Интенсивный курс английского языка для начинающих.\nГрамматика, лексика, разговорная практика.\n30-дневная программа обучения."
    ]
    publication_page_count_example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    publication_category_example = [
        "спорт", "кулинария", "искусство", "путешествия", "образование", "психология",
        "дизайн", "здоровье", "маркетинг", "технологии", "хобби", "история",
        "наука", "финансы", "мода", "музыка", "литература", "фотография",
        "рукоделие", "автомобили"
    ]
    publication_review_text_example = [
        "Отличная публикация! Очень понятно и доступно изложен материал.\nМного полезной информации для начинающих.\nРекомендую всем, кто хочет разобраться в теме.",
        "Прекрасное руководство с практическими примерами.\nАвтор подробно объясняет каждый шаг.\nИдеально подходит для самостоятельного изучения.",
        "Очень информативно и интересно написано.\nМного полезных советов и рекомендаций.\nБуду перечитывать и использовать в работе.",
        "Отличное качество издания, красивые иллюстрации.\nСодержание соответствует описанию.\nДостойная покупка по разумной цене.",
        "Очень доволен приобретением. Материал структурирован логично.\nПодходит как для новичков, так и для опытных специалистов.\nСоветую к прочтению.",
        "Понравился практический подход автора.\nМного реальных кейсов и примеров из жизни.\nПомогло в профессиональном развитии.",
        "Отличное сочетание теории и практики.\nАвтор умеет объяснять сложные вещи простым языком.\nРекомендую коллегам и друзьям.",
        "Очень полезное и своевременное издание.\nАктуальная информация, современные подходы.\nПомогло в решении рабочих задач.",
        "Прекрасный стиль изложения, читается на одном дыхании.\nМного инсайтов и новых идей.\nВдохновило на новые проекты.",
        "Качественный контент, профессиональный подход.\nВсе темы раскрыты глубоко и подробно.\nСтоит каждой потраченной копейки.",
        "Идеально для самостоятельного изучения.\nПонятные объяснения, хорошие примеры.\nПомогло освоить новую тему с нуля.",
        "Очень практично и применимо в реальной жизни.\nМного конкретных советов и инструкций.\nУже использую полученные знания.",
        "Отличная структура и организация материала.\nЛегко найти нужную информацию.\nУдобно использовать как справочник.",
        "Вдохновляющая и мотивирующая публикация.\nАвтор делится ценным опытом.\nПомогло по-новому взглянуть на тему.",
        "Профессиональный и качественный контент.\nПодробно разобраны все аспекты темы.\nРекомендую специалистам в области."
    ]

    birthday_day_example = birthday_data_example = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        [1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995,
         1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010]
    ]
    gender_example = ["м", "ж"]


def create_date(date_list: list) -> str:
    """
    Создает дату по полученному списку возможных дат
    :return: строка в формате dd--mm-yyyy
    """

    day = date_list[0][random.randint(0, 27)]
    month = date_list[1][random.randint(0, 11)]
    year = date_list[2][random.randint(0, len(date_list[2]) - 1)]

    return f'{day}-{month}-{year}'


def create_publication_info() -> dict:
    """ Создает словарь данных о публикациях пользователя """
    publication_number = random.randint(1, 5)
    publications_data = dict()

    for _ in range(publication_number):
        publication = dict()

        publication['name'] = ExampleData.publication_name_example[
            random.randint(0, len(ExampleData.publication_name_example) - 1)]
        publication['description'] = ExampleData.publication_description_example[
            random.randint(0, len(ExampleData.publication_description_example) - 1)]
        publication['volume'] = ExampleData.publication_page_count_example[
            random.randint(0, len(ExampleData.publication_page_count_example) - 1)]
        publication['category'] = ExampleData.publication_category_example[
            random.randint(0, len(ExampleData.publication_category_example) - 1)]

        review_count = random.randint(0, 5)
        review_info = dict()

        for j in range(review_count):
            k = dict()
            k['id'] = random.randint(0, 1000)
            k['text'] = ExampleData.publication_review_text_example[
                random.randint(0, len(ExampleData.publication_review_text_example) - 1)]
            review_info[j] = k

        publication['reviews'] = review_info
        publications_data[i] = publication
    return publications_data


def generate_data(id: int = 0) -> dict:
    """
    Функция для генерации исходного набора данных о пользователе
    :param id: уникальный идентификатор пользователя
    """
    data = dict()

    name = ExampleData.name_list_example[random.randint(0, len(ExampleData.name_list_example) - 1)]
    mail_number = random.randint(1, 3)
    mail_address = [addr for addr in [ExampleData.mail_address_example[random.randint(
        0, len(ExampleData.mail_address_example) - 1)]] for i in range(mail_number)]
    registration_date = create_date(ExampleData.registration_data_example)
    last_auth = create_date(ExampleData.last_auth_example)
    status = ExampleData.status_example[random.randint(0, len(ExampleData.status_example) - 1)]
    publication_info = create_publication_info()
    birthday_date = create_date(ExampleData.birthday_data_example)
    gender = ExampleData.gender_example[random.randint(0, len(ExampleData.gender_example) - 1)]

    data['id'] = id
    data['name'] = name
    data['mail'] = mail_address
    data['registration_date'] = registration_date
    data['last_auth'] = last_auth
    data['status'] = status
    data['publication_info'] = publication_info
    data['birthday_date'] = birthday_date
    data['gender'] = gender

    return data


if __name__ == "__main__":
    # Инициализация списка данных о пользователях
    users_data = dict()
    for i in range(1000):
        # Генерация данных и их добавление в общий список
        user_data = generate_data(i)
        users_data[i] = user_data
        if i == 0:
            print('Данные первого пользователя:')
            [print(key + ':', val) for key, val in user_data.items()]

    # Запись json файла
    with open('users_data.json', 'w') as file:
        json.dump(users_data, file, indent=4, ensure_ascii=False)