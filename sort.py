data = [4, -30, 100, -100, 123, 1, 0, -1, -4]


def main():

    rez = sorted(data, key=abs, reverse=True)
    print(rez)

    rezl = sorted(data, key=lambda x: abs(x), reverse=True)
    print(rezl)
        
if __name__ == "__main__":  
    main()