# provide random data for testing, support by random&faker
import random
from faker import Faker


class DataGenerator:
    def __init__(self, locale='en_US', seed=-1):
        self.random = random
        # user can input locale to generate data by local, default local is en_US
        self.fake = Faker(locale)
        # user can input seed which greater or equal than 0 to get the same result
        if seed >= 0:
            self.fake_seed = Faker().seed(seed)
            self.random_seed = random.seed(seed)

    def random_int(self, a=0, b=100):
        return self.random.randint(a, b)

    def random_uniform(self, a=0, b=1):
        return self.random.uniform(a, b)

    def random_randrange(self, start=0, stop=101, step=2):
        return self.random.randrange(start, stop, step)

    def random_choice(self, seq=None):
        return self.random.choice(seq)

    def random_sample(self, population=None, k=0):
        return self.random.sample(population, k)

    def random_shuffle(self, x):
        self.random.shuffle(x)
        return x

    def random_phone_number(self):
        return self.fake.phone_number()

    def random_name(self):
        return self.fake.name()

    def random_password(self, length=8, special_chars=True, digits=True, upper_case=True, lower_case=True):
        return self.fake.password(length, special_chars, digits, upper_case, lower_case)

    def random_address(self):
        return self.fake.address()

    def random_postcode(self):
        return self.fake.postcode()

    def random_company(self):
        return self.fake.company()

    def random_email(self):
        return self.fake.email()

    def random_ipv4(self):
        return self.fake.ipv4()

    def random_user_agent(self):
        return self.fake.user_agent()

    def random_date(self):
        return self.fake.date()

    def random_time(self):
        return self.fake.time()

    def random_date_time(self):
        return self.fake.date_time()

    def random_word(self, ext_word_list=None):
        return self.fake.word(ext_word_list)

    def random_words(self, nb=3, ext_word_list=None):
        return self.fake.words(nb, ext_word_list)

    def random_sentence(self, nb_words=6, variable_nb_words=True, ext_word_list=None):
        return self.fake.sentence(nb_words, variable_nb_words, ext_word_list)

    def random_sentences(self, nb=3, ext_word_list=None):
        return self.fake.sentences(nb, ext_word_list)

    def random_paragraph(self, nb_sentences=3, variable_nb_sentences=True, ext_word_list=None):
        return self.fake.paragraph(nb_sentences, variable_nb_sentences, ext_word_list)

    def random_paragraphs(self, nb=3, ext_word_list=None):
        return self.fake.paragraphs(nb, ext_word_list)

    def random_text(self, max_nb_chars=200, ext_word_list=None):
        return self.fake.text(max_nb_chars, ext_word_list)


if __name__ == '__main__':
    # some demos for reference
    data = DataGenerator('en_US', 0)
    print('--------')
    print(data.random_int(0, 10000))
    print(data.random_uniform(1, 2))
    print(data.random_randrange(1, 100, 2))
    char_list = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=',
                 '{', '[', '}', ']', ':', ';', '"', '\'', '|', '\\', '<', ',', '>', '.', '?', '/']
    print(data.random_choice(char_list))
    print(data.random_sample(char_list, 3))
    int_list = [0, 1, 2, 3, 4]
    print(data.random_shuffle(int_list))
    print('--------')
    print(data.random_phone_number())
    print(data.random_name())
    print(data.random_password())
    print(data.random_address())
    print(data.random_postcode())
    print(data.random_email())
    print(data.random_ipv4())
    print(data.random_user_agent())
    print('--------')
    print(data.random_word())
    print(data.random_words())
    print(data.random_sentence())
    print(data.random_sentences())
    print(data.random_paragraph())
    print(data.random_paragraphs())
    print(data.random_text())
    print('--------')
    word_list = ['python', 'is', 'a', 'programming', 'language']
    print(data.random_word(word_list))
    print(data.random_words(3, word_list))
    print(data.random_sentence(4, False, word_list))
    print(data.random_sentences(3, word_list))
    print(data.random_paragraph(6, False, word_list))
    print(data.random_paragraphs(3, word_list))
    print(data.random_text(300, word_list))
    print('--------')
