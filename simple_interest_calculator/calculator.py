def calculate_simple_interest(principal: float, rate: float, time: float):
    si = (principal * rate * time) / 100
    total = principal + si
    return si, total