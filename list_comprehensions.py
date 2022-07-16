def main():
    list = [i*i for i in range(1,101) if i % 3 != 0]
    challenge = [i for i in range(1,100000) if i % 36 == 0]
    print(challenge)

if __name__ == '__main__':
    main()