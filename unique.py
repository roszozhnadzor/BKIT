class Unique(object):
    rez = []
    def __init__(self, items, **kwargs):
        ignore_case = kwargs.get('ignore_case')
        self.index = 0
        el = list(items)
        for i in el:
            if ignore_case:
                if not(i.lower() in [x.lower() for x in self.rez]):
                    self.rez.append(i)
            else:
                if not(i in self.rez):
                    self.rez.append(i)

# Нужно реализовать конструктор
# В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
# в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
# Например: ignore_case = True, Aбв и АБВ - разные строки
# ignore_case = False, Aбв и АБВ - одинаковые строки, одна из которых удалится
# По-умолчанию ignore_case = False

    def __next__(self):
        array_length = len(self.rez)
        prev_index = self.index
        if self.index < array_length:
            self.index += 1
        if prev_index <= array_length and prev_index < array_length:
            return self.rez[prev_index]
        else:
           self.index = 0
           raise StopIteration

    def __iter__(self):
        return self

def main():
    data = ["A", "B", "a", "b"]
    newdata = Unique(data, ignore_case=True)
    for i in newdata:
        print(i)

if __name__ == "__main__":
    main()