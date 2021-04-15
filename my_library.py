import colorama


class Book:
    media_type = 'Book'

    def __init__(self, title, authors, publish_year, pages, language, price, total_read_pages=0):
        """

        :param title: A string, title of book
        :param authors: A list of strings, authors of book
        :param publish_year: int
        :param pages: int, number of all book pages
        :param language: string, the language of book
        :param price: float, price of book in $
        :param total_read_pages: int all pages that user read.
            it is placed in __init__ so that user can enter media
            when he/she is read/listened some pages/minutes of media
        """
        self.title = title
        self.publish_year = publish_year
        self.language = language
        self.price = price
        self.authors = authors
        self.pages = pages
        self.total_read_pages = total_read_pages
        self.progress = round((self.total_read_pages / self.pages) * 100)

    def read(self, read_pages):
        """
        this method shows some Messages depending on the number of pages read based on total_read_pages
        :param read_pages: number of pages is read now
        :return: total read pages
        """
        if self.pages < (self.total_read_pages + read_pages):
            read_message = "input is out of range...!"

        else:
            self.total_read_pages += read_pages
            self.progress = round((self.total_read_pages / self.pages) * 100)
            if 0 <= self.total_read_pages < self.pages:

                read_message = f'you have read {read_pages} more pages from "{self.title}".' \
                          f' and {self.pages - self.total_read_pages} pages left'
            else:
                read_message = f'congratulations! You have read 'f'all {self.total_read_pages}' \
                          f' pages of "{self.title}" try a new one'
        return read_message

    def get_status(self):
        """
         This method assignees a string to attribute 'status' based on total_read_pages
        :return: status of reading media
        """

        if 0 < self.total_read_pages < self.pages:
            status = 'reading'
        elif self.total_read_pages == self.pages:
            status = 'finished'
        else:
            status = 'Unread'
        return status

    def __str__(self):

        return f'title: {self.title} \nauthor(s): {self.authors} \n' \
               f'publish year: {self.publish_year} \nnumber of pages: {self.pages} \n' \
               f'language: {self.language} \nprice: {self.price}$\n' \
               f'total read pages:{self.total_read_pages}\nreading status: {self.get_status()}\n' \
               f'reading progress:{self.progress}%\n'

    @staticmethod
    def get_info(media_type, shelf):
        """

        :param shelf: list of medias in library which are same as media_type
        :param media_type: text type media: Book, Magazine
        :return: an (book/magazine) object
        """

        title_list = [objects.title for objects in shelf]
        text_media = None

        while True:
            title = input(f'title of {media_type}:')
            if title in title_list:
                print(colorama.Fore.CYAN, f'this {media_type} already exist in'
                                          f' {media_type} shelf try another', colorama.Fore.RESET)
            else:
                title_list.append(title)
                break
        authors = input(f'author(s) of {media_type}:').split(',')
        publish_year = int(input(f'publish_year of {media_type}:'))
        pages = int(input(f'number of pages of {media_type}:'))
        language = input(f'language of {media_type}:')
        price = float(input(f'price of {media_type}in $:'))
        total_read_pages = 0
        init_read = bool(input(f'Have you read/listen this {media_type} before?').capitalize())
        if init_read:
            total_read_pages = int(input(f'initial reading pages of {media_type}:'))

        if media_type == 'Book':
            text_media = Book(title, authors, publish_year, pages, language, price, total_read_pages)
        elif media_type == 'Magazine':
            issue = float(input(f'issue of {media_type}:'))
            text_media = Magazine(title, authors, publish_year, pages, language, price, issue, total_read_pages)
        else:
            print('check input...!')
        return text_media


class Podcast:
    media_type = 'Podcast'

    def __init__(self, title, speakers, publish_year, time, audio_language, price, total_listened_time=0):

        """

        :param title: string, Title of Podcast episode
        :param speakers: list of speaker(s) in podcast
        :param publish_year: int, Publish year of podcast
        :param time: float, Duration of podcast file
        :param audio_language: string, Language of podcast speaker
        :param price: float, Price of podcast in $
        """
        self.title = title
        self.speakers = speakers
        self.publish_year = publish_year
        self.time = time
        self.audio_language = audio_language
        self.price = price
        self.total_listened_time = total_listened_time
        self.progress = round((self.total_listened_time / self.time) * 100)

    def listen(self, listened_time):
        """
        this method shows some Messages depending on the time duration listened based on total_listened_time
        :param listened_time: time duration is listened now
        :return: total listened time
        """
        if self.time < (self.total_listened_time + listened_time):
            listen_message = "input is out of range...!"

        else:
            self.total_listened_time += listened_time

            self.progress = round((self.total_listened_time / self.time) * 100)

            if 0 <= self.total_listened_time < self.time:

                listen_message = f'you have listened {listened_time} more minutes from "{self.title}".' \
                          f' and {self.time - self.total_listened_time} minutes left'
            else:
                listen_message = f'congratulations! You have listened all {self.total_listened_time}' \
                          f' minutes of "{self.title}" try a new one'
        return listen_message

    def get_status(self):
        """
         This method assigns a string to attribute 'status' based on total_listened_time
        :return: status of listening media
        """

        if 0 < self.total_listened_time < self.time:
            status = 'listening'
        elif self.total_listened_time == self.time:
            status = 'finished'
        else:
            status = 'Untouched'
        return status

    def __str__(self):
        return f'title: {self.title}\nspeaker(s): {self.speakers} \n' \
               f'publish year: {self.publish_year} \nfile duration: {self.time} minutes \n' \
               f'language: {self.audio_language} \nprice: {self.price}$ \n' \
               f'total listened time:{self.total_listened_time}\nstatus: {self.get_status()}\n' \
               f'listening progress: {self.progress}%\n'

    @staticmethod
    def get_info(media_type, shelf):
        """
        this function is same as get info in parent class (book) but gets attributes of audio media
        :param media_type: Podcast or audiobook
        :param shelf:
        :return: a (Podcast/audiobook) object
        """

        title_list = [_.title for _ in shelf]
        audio = None
        while True:
            title = input(f'title of {media_type}:')
            if title in title_list:
                print(colorama.Fore.CYAN, f'this {media_type} already exist in'
                                          f' {media_type} shelf try another', colorama.Fore.RESET)
            else:
                title_list.append(title)
                break

        speakers = input(f'speaker of {media_type}:').split(',')
        publish_year = int(input(f'publish_year of {media_type}:'))
        time = int(input(f'time duration of {media_type}:'))
        audio_language = input(f'audio language of {media_type}:')
        price = float(input(f'price of {media_type} in $:'))
        total_listened_time = 0
        init_listen = bool(input(f'press any key if you listened this {media_type} before?'))
        if init_listen:
            total_listened_time = int(input(f'initial listening time of {media_type} in minutes :'))

        if media_type == 'Podcast':
            audio = Podcast(title, speakers, publish_year, time, audio_language, price, total_listened_time)
        elif media_type == 'Audiobook':
            authors = input(f'author(s) of {media_type}:').split(',')
            pages = int(input(f'pages of {media_type}:'))
            book_language = input(f'book language of {media_type}:')
            audio = AudioBook(title, speakers, authors, publish_year, time, pages, book_language, audio_language, price,
                              total_listened_time)
            audio.listen(total_listened_time)
        return audio


class Magazine(Book):
    media_type = 'Magazine'

    def __init__(self, title, authors, publish_year, pages, language, price, issue, total_read_pages=0):
        """

                :param title: A string, title of magazine
        :param authors: A list of strings, authors of magazine
        :param publish_year: int
        :param pages: int, number of all magazine pages
        :param language: string, the language of magazine
        :param price: float, price of magazine in $
        :param issue: float, version of Magazine
        :param total_read_pages: int all pages that user read.
            it is placed in __init__ so that user can enter media
            when he/she is read some pages of media
        """
        super().__init__(title, authors, publish_year, pages, language, price)
        self.issue = issue
        self.total_read_pages = total_read_pages
        self.progress = round((self.total_read_pages / self.pages) * 100)

    def __str__(self):
        return f'title: {self.title} \nauthor(s): {self.authors} \n' \
               f'publish year: {self.publish_year} \nnumber of pages: {self.pages} \n' \
               f'language: {self.language} \nprice: {self.price}$\nissue: {self.issue}' \
               f'total read pages:{self.total_read_pages}\nreading status: {self.get_status()}\n' \
               f'reading progress:{self.progress}%\n'


class AudioBook(Podcast, Book):
    media_type = 'Audiobook'
    """
    """

    def __init__(self, title, speakers, authors, publish_year, time, pages,
                 book_language, audio_language, price, total_listened_time=0):
        """

        :param title: string, Title of audiobook
        :param speakers: list of Persons' name who reads the book
        :param authors: list of author(s) Names of persons  who writes the paper book
        :param publish_year: int, Publish year of Audio file
        :param pages: int, Number of pages in paper book
        :param time: float, Time duration of audio file
        :param book_language: string, Language of paper book
        :param audio_language: string, Language of audio file
        :param price: float, Price of audio file in $
        :param total_listened_time: total listened time from audio file
        """
        Podcast.__init__(self, title, speakers, publish_year, time, audio_language, price)
        Book.__init__(self, title, authors, publish_year, pages, book_language, price)
        self.book_language = book_language
        self.total_listened_time = total_listened_time
        self.progress = round((self.total_listened_time / self.time) * 100)

    def __str__(self):
        return f'\ntitle: {self.title}\nspeaker(s): {self.speakers}\n' \
               f'author(s): {self.authors}\npublish year: {self.publish_year}\n' \
               f'number of pages: {self.pages}\naudio_duration: {self.time}' \
               f'\nlanguage of book: {self.book_language}' \
               f'\nlanguage of audio: {self.audio_language}\nprice: {self.price}\nstatus: {self.get_status()}\n' \
               f'listening progress: {self.progress}%\n'


def get_info():
    """
        This function, depending on the media type, takes information of a media from user until 5 is entered,
        then appends it to related media type in main library
    :return: None
    """
    media_types = {'1': 'Book', '2': 'Magazine', '3': 'Podcast', '4': 'Audiobook', '5': 'quit'}
    while True:
        media_type = input('1.Book, 2.Magazine, 3.Podcast, 4.Audiobook or 5.Quit:').capitalize()
        if media_type not in media_types.keys():
            print(colorama.Fore.RED, 'ERROR: Invalid media type...!', colorama.Fore.RESET)

        elif media_type in media_types.keys() and media_type != '5':
            for _ in library[media_types[media_type]]:
                if _.media_type == media_types[media_type]:
                    library[media_types[media_type]].append(_.get_info(media_types[media_type],
                                                                       library[media_types[media_type]]))
                    sorting(library)
                    break
        else:
            break


def easy_print(list_to_print):
    """
    At first prints titles of table
    then in a for loop prints wanted objects attributes
    :param list_to_print: a list of objects to print in table form
    :return: nothing, just print objects
    """
    max_width = len(max(list_to_print, key=lambda x: len(x.__getattribute__('title'))).title)
    cyan_color = colorama.Fore.CYAN
    reset_color = colorama.Fore.RESET
    max_width += 6

    print(' ' * 24 + ' ' * int(0.5 * (max_width - len('media type'))) + cyan_color + 'media_type'
          + ' ' * int(0.5 * ((max_width + 1 if max_width % 2 != 0 else 0) - len('media type'))) + '|'
          + ' ' * int(0.5 * ((max_width + 1 if max_width % 2 != 0 else 0) - len('title'))) + 'title'
          + ' ' * int(0.5 * (max_width - len('title'))) + '|' + ' '
          * int(0.5 * ((max_width + 1 if max_width % 2 != 0 else 0) - len('progress'))) + 'progress' + reset_color)

    print(' ' * 24, '-' * (3 * max_width))

    for _ in list_to_print:
        odd = max_width
        if (max_width - len(str(_.media_type)) % 2) != 0:
            odd += 1
        print(' ' * 24 + ' ' * int(0.5 * (max_width - len(str(_.media_type)))) + _.media_type + ' '
              * int(0.5 * (odd - len(str(_.media_type)))) + cyan_color + '|' + reset_color
              + ' ' * int(0.5 * (odd - len(str(_.title)))) + _.title
              + ' ' * int(0.5 * (max_width - len(str(_.title)))) + cyan_color + '|' + reset_color
              + ' ' * int(0.5 * (odd - len(str(_.progress)))) + str(_.progress) + '%')


def sorting(media_dict_or_list):
    """
    This function transfers all objects in a dictionary of 4 kinds of media to
     a list and sorts them by progress percent descending.
    :param media_dict_or_list: main library
    """

    if type(media_dict_or_list) == dict:
        all_media = []
        for ob_lst in media_dict_or_list.values():
            for mda in ob_lst:
                all_media.append(mda)
        sorted_media = sorted(all_media, key=lambda x: x.__getattribute__('progress'), reverse=True)
    else:
        sorted_media = sorted(media_dict_or_list, key=lambda x: x.__getattribute__('progress'), reverse=True)
    print(colorama.Fore.GREEN, '.' * 50 + 'sorted media in library/shelf by progress' + '.' * 50, '\n',
          colorama.Fore.RESET)
    easy_print(sorted_media)
    return sorted_media


def show(lib_or_shelf):
    """

    :param lib_or_shelf: dictionary( main library) or list (a media shelf)
    :return: prints list or dictionary
    """
    if type(lib_or_shelf) is dict:
        for key, value in lib_or_shelf.items():
            print(colorama.Fore.MAGENTA, f'shelf of {key}s:'.capitalize(), colorama.Fore.RESET)
            for _ in value:
                print(_)
    elif type(lib_or_shelf) is list:
        for _ in lib_or_shelf:
            print(_)


def clear_it(shelf_or_lib):
    """
    this method clears all lists of objects or objects in list
    :param shelf_or_lib: main library or a shelf of library
    :return: empty dictionary or list
    """
    check = input('!!!! your library/shelf is about to be cleared, are you sure?')
    if check:
        if type(shelf_or_lib) == dict:
            for lis in shelf_or_lib.values():
                lis.clear()
        elif type(shelf_or_lib) == list:
            shelf_or_lib.clear()
        print(colorama.Fore.LIGHTGREEN_EX, 'your library/shelf is successfully cleared...', colorama.Fore.RESET)
    else:
        print(colorama.Fore.LIGHTRED_EX, 'Deleting action has been aborted...', colorama.Fore.RESET)


def study(media):
    massage = ''
    if media.media_type in ['Book', 'Magazine']:
        pages = int(input('Enter number of pages you read: '))
        massage = media.read(pages)
    elif media.media_type in ['Podcast', 'Audiobook']:
        time = float(input('Enter time duration you listened: '))
        massage = media.listen(time)
    return massage


def media_menu(chosen_shelf):
    """
    This function is for choosing methods of objects
    first while loop: choose media(object) loop
    second while loop: switch between methods that apply to a media
    :param chosen_shelf: name of shelf
    :return:
    """
    shelf_medias_title = [x.title for x in library[chosen_shelf]]
    for i in range(len(shelf_medias_title)):
        print(colorama.Fore.CYAN, i + 1, '.', shelf_medias_title[i], colorama.Fore.RESET)

    """

    """
    while True:
        media_title = shelf_medias_title[int(input(f'Enter the title of your considering {chosen_shelf}: ')) - 1]
        if media_title not in shelf_medias_title:
            print(f'ERROR: please enter a number from 1 - {len(shelf_medias_title) + 1}..')
        else:
            break

    while True:
        print(colorama.Fore.LIGHTMAGENTA_EX, f'\n1. Study "{media_title}"'
                                             f'\n2. check status of "{media_title}"'
                                             f'\n3. remove "{media_title}" from shelf'
                                             f'\n4. show the "{media_title}"'
                                             f'\n5. chek progress of "{media_title}"'
                                             f'\n6. back to shelf menu', colorama.Fore.RESET)

        while True:
            act = input('Take an action to continue: ')
            if act not in media_method_dict.keys() and act != '6':
                print(colorama.Fore.RED, 'invalid order... just 1 - 6 are valid', colorama.Fore.RESET)
            else:
                break
        if act == '6':
            break

        else:
            for _ in library[chosen_shelf]:
                if media_title == _.title:
                    media_method_dict[act](_)


def shelf_menu(media_type):
    """
    shelf actions switching (methods which applies to a selected media shelf)
    :param media_type: can be book, podcast, magazine of audiobook
    :return: nothing
    """
    while True:
        print('\n1. Back to library menu'
              f'\n2. choose a {media_type}'
              f'\n3. Sort {media_type} shelf'
              '\n4. Show the shelf'
              f'\n5. Clear the {media_type} shelf')

        while True:
            select_shelf_act = input('Take an action to continue: ')
            if (select_shelf_act not in shelf_menu_func_dict.keys()) and (select_shelf_act not in ['2', '1']):
                print(colorama.Fore.RED, 'invalid order... just 1 - 5 are valid', colorama.Fore.RESET)
            else:
                break

        if select_shelf_act == '2':
            media_menu(media_type)
        elif select_shelf_act == '1':
            break
        else:
            shelf_menu_func_dict[select_shelf_act](library[media_type])


# .....................four dictionaries below are used to avoid too many nested "if"s and "else"s.....................
main_menu_func_dict = {'2': lambda lib: sorting(lib),
                       '3': lambda lib: show(lib),
                       '4': lambda lib: clear_it(lib)}

shelf_menu_func_dict = {'3': lambda lst_med: sorting(lst_med),
                        '4': lambda lst_med: show(lst_med),
                        '5': lambda lst_med: clear_it(lst_med), }

media_method_dict = {'1': lambda x: print(study(x)),
                     '2': lambda x: print(f'status of {x.title} is {x.get_status()}'),
                     '3': lambda x: library[x.media_type].remove(x) and print(f'{x.media_type}'
                                                                              f' named {x.title} is removed'),
                     '4': lambda x: print(x),
                     '5': lambda x: print(f'{x.progress}% of {x.title} reading/listening progress is completed...')}

media_types_choosing = {'1': 'Book', '2': 'Magazine', '3': 'Podcast', '4': 'Audiobook'}

# Default medias in library for testing the cod

podcast1 = Podcast('Ravaaq', 'Farzin Ranjbar', 2020, 50, 'persian', 0, 10)
book1 = Book('No Friend But The Mountains', 'Behrouz Boochani', 2018, 374, 'English', 10, 12)
book2 = Book('Symphony Of Dead', 'Behrouz Boochani', 2018, 374, 'English', 126)
magazine = Magazine('Bukhara', '[Ali Dehbashi,Darioush Ashoori]', 2020, 768, 'Persian', 55, 140, 23)
audio_book = AudioBook('The Black Swan', 'Ali Bandari', 'Nassim Nicholas Taleb', 2020, 400, 62,
                       'English', 'Persian', 0, 10)

# main library
library = {'Book': [book1, book2], 'Magazine': [magazine], 'Podcast': [podcast1], 'Audiobook': [audio_book]}
print('-' * 100)

# menu code
action = ''
while action != 'Quit':

    print(colorama.Fore.MAGENTA, '*&' * 35, 'Hello user. Welcome to your library'.upper(),
          '$*' * 35, colorama.Fore.RESET)
    print(colorama.Fore.LIGHTBLUE_EX,
          '\n1. Add media to the library'
          '\n2. Sort the library'
          '\n3. Show the library'
          '\n4. Clear the library',
          '\n5. choose a media shelf and study from it',
          '\n6. Quit', colorama.Fore.RESET)

    print(colorama.Fore.GREEN, 'please take an action 1 to 4 to modify the main library'
                               ' \n or enter 5 to go to a specific shelf: ', colorama.Fore.RESET)
    while True:
        action = input('action:').capitalize()
        if (action not in main_menu_func_dict.keys()) and (action not in ['1', '5', '6']):
            print(colorama.Fore.RED, 'invalid order... just 1 - 6 are valid', colorama.Fore.RESET)
        else:
            break
    if action == '1':
        get_info()

    elif action == '5':
        while True:
            media_typ = input(f'{colorama.Fore.LIGHTMAGENTA_EX}Choose a shelf to continue:'
                              f'1.Book/ 2.Magazine/ 3.Podcast/4.Audiobook{colorama.Fore.RESET} ').capitalize()
            if media_typ not in media_types_choosing.keys():
                print(f'ERROR:please enter 1 t0 4 to choose a media shelf')
            else:
                break
        shelf_menu(media_types_choosing[media_typ])

    elif action == '6':
        action = 'Quit'
    else:
        main_menu_func_dict[action](library)
