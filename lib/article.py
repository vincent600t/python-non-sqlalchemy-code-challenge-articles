class Article:
    all = []

    def __init__(self, author, magazine, title):
        # delayed imports to avoid circular imports
        from lib.author import Author
        from lib.magazine import Magazine

        # validate author and magazine
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be an instance of Magazine")

        # validate title
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Title must be a string between 5 and 50 characters")

        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)

    # TITLE
    @property
    def title(self):
        return self._title

   # AUTHOR
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        from lib.author import Author
        if not isinstance(value, Author):
            raise Exception("Author must be an instance of Author")
        self._author = value

    # MAGAZINE
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        from lib.magazine import Magazine
        if not isinstance(value, Magazine):
            raise Exception("Magazine must be an instance of Magazine")
        self._magazine = value
