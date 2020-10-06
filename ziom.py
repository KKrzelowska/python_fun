#wyszukiwanie najczestszego motywu k o długości n

class Motif:
    def __init__(self):
        self.content = ''
        self.k_meres = []
    def add_content(self, element):
        self.content = element
    def k_mere_add(self, k):
        k_mere = ''
        n = 0
        for mark in self.content:
            n += 1
            k_mere += mark
            if n % k == 0:
                self.k_meres.append(k_mere)
                k_mere = ''
                n = 0
        return 0
    def seek(self, k):
        self.k_mere_add(k)
        return self.counting()
    def counting(self):
        most_popular_mere = ''
        n_occur = 0
        for element in self.k_meres:
            if self.k_meres.count(element) > n_occur:
                n_occur = self.k_meres.count(element)
                most_popular_mere = element
        return most_popular_mere


if __name__ == "__main__":
    print(0)
