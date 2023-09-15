def do_fizzbuzz(num):
    """
    fizzbuzz 기능 수행
    정해진 숫자에 대해 
    3의 배수는 'fizz'
    5의 배수는 'buzz'
    15의 배수는 'fizzbuzz'
    나머지 수자는 그대로 출력
    """
    for i in range(1, num+1):
        if i%15 == 0:
            print('fizzbuzz')
        elif i%3 == 0:
            print('fizz')
        elif i%5 == 0:
            print('buzz')
        else: 
            print(i)

if __name__ == '__main__':
    do_fizzbuzz(16)
