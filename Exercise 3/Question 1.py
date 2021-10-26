# Question1

def convert_to_days():
    hours = int(input('Enter number of Hours: '))
    minutes = int(input('Enter number of Minutes: '))
    seconds = int(input('Enter number of Seconds: '))
    return hours, minutes, seconds


def get_days(hours, minutes, seconds):
    days = (hours / 24) + (minutes/1440) + (seconds/86400)
    print(f"{days:.4f}")

def main():
    hours, minutes, seconds = convert_to_days()
    get_days(hours, minutes, seconds)

main()
