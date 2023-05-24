numbers = [2,7]	

def f(num):
    smallest=0
    if num % 2 == 0: # 짝수일 경우
        smallest = int(bin(num)[2:]+'1',2)
        



def solution(numbers):
    answer = []
    print(numbers)

    for n in numbers:
        print(f(n))
        answer.append(f(n))
    return answer

solution(numbers)