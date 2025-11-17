import json
import csv


def json_to_dsv(json_file_path, delimeter="\t") -> list:
    with open(json_file_path, 'r', encoding="Windows-1251") as json_file:
        data = json.load(json_file)

        user_headers = ["id", "name", "mail", "registration_date", "last_auth", "status", "birthday_date", "gender"]
        publication_headers = ["user_id", "publication_id", "publication_name", "description",
                               "volume", "category", "review_count"
                               ]
        reviews_headers = ["publication_id", "user_id", "text", "words_count"]

        user_rows = [user_headers]
        publication_rows = [publication_headers]
        reviews_rows = [reviews_headers]

        for user_id, user_data in data.items():
            user_row = [
                user_data['id'],
                user_data['name'],
                ';'.join(user_data['mail']),
                user_data['registration_date'],
                user_data['last_auth'],
                user_data['status'],
                user_data['birthday_date'],
                user_data['gender']
            ]

            user_rows.append(user_row)

            for publication_id, publication_data in user_data['publication_info'].items():
                publication_row = [
                    int(publication_id),
                    publication_data['name'],
                    publication_data['description'],
                    publication_data['volume'],
                    publication_data['category'],
                    len(publication_data['reviews'].keys())
                ]

                publication_rows.append(publication_row)

            for review_id, review_data in publication_data['reviews'].items():
                review_row = [
                    int(publication_id),
                    review_data['id'],
                    review_data['text'],
                    calculate_word_count(review_data['text'])
                ]

                reviews_rows.append(review_row)

        with open('users_table.dsv', 'w', encoding='utf-8', newline='\n') as file:
            writer = csv.writer(file, delimiter=delimeter)
            writer.writerows(user_rows)

        with open('publications_table.dsv', 'w', encoding='utf-8', newline='\n') as file:
            writer = csv.writer(file, delimiter=delimeter)
            writer.writerows(publication_rows)

        with open('reviews_table.dsv', 'w', encoding='utf-8', newline='\n') as file:
            writer = csv.writer(file, delimiter=delimeter)
            writer.writerows(reviews_rows)

        print("Файлы users_table.dsv, publications_table.dsv, reviews_table.dsv созданы.")

        return reviews_rows


def calculate_word_count(reviews_str: str) -> int:
    text = reviews_str.replace('\n', ' ').split(' ')
    count = len(text)

    return count


if __name__ == "__main__":
    list_review = json_to_dsv("users_data.json")
