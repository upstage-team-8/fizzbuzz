import random

def simulate_trial():
    boxes = list(range(100))
    random.shuffle(boxes)
    
    for prisoner in range(100):
        found = False
        next_box = prisoner
        for _ in range(50):
            if boxes[next_box] == prisoner:
                found = True
                break
            next_box = boxes[next_box]
        if not found:
            return False
    return True

def simulate_prisoners(trials):
    success_count = sum(simulate_trial() for _ in range(trials))
    return success_count / trials

# 9999번의 시도로 성공 확률 계산
probability = simulate_prisoners(3000)
print(f"성공 확률: {probability}")
