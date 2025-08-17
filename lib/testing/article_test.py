# classes/many_to_many.py

class Article:
    all = []

    def __init__(self, author, magazine, title):
        # validate author
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance")

        # validate magazine
        if not isinstance(magazine, Magazine):
            raise Exception("magazine must be a Magazine instance")

        # validate title
        if not isinstance(title, str):
            raise Exception("title must be a string")
        if not (5 <= len(title) <= 50):
            raise Exception("title must be between 5 and 50 characters")

        self._title = title  # immutable
        self.author = author
        self.magazine = magazine

        Article.all.append(self)

    @property
    def title(self):
        return self._title


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise Exception("name must be a non-empty string")
        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list(set(mag.category for mag in self.magazines()))


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise Exception("name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or not (2 <= len(category) <= 16):
            raise Exception("category must be a string between 2 and 16 characters")

        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        return [
            author for author in self.contributors()
            if len([a for a in Article.all if a.author == author and a.magazine == self]) > 2
        ]
