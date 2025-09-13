def calculate_simple_interest(principal: float, rate: float, time: float):
    si = (principal * rate * time) / 100
    total = principal + si
    return si, total

if __name__ == "__main__":
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest (%): "))
    time = float(input("Enter the time (in years): "))
    si, total = calculate_simple_interest(principal, rate, time)
    print(f"\nSimple Interest = {si:.2f}")
    print(f"Total Amount = {total:.2f}")