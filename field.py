goods = [
   {'title': 'Ковер', 'price': 2000, 'color': 'green'},
   {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    assert len(args) > 0
    rez = []
    if len(args) == 1:
        for i in items:
                yield i[args[0]]
            
    else:
        for a in items:
            yield {args[i]: a[args[i]] for i in range(len(args))}
    

def main():

    rez = field(goods, 'title')
    for i in rez:
        print(i)
    rez = field(goods, 'title', 'price')
    for i in rez:
        print(i)

if __name__ == "__main__":
    main()