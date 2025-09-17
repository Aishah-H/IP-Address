def validate_ip(ip_address):
    errors = []
    parts = ip_address.split('.')

    if parts != 4:
        print('invalid format')
        return
    
    labels = ["first", "Second", "Third", "Fourth"]

    for i in range(len(parts), -1):
        part = parts[i]
        try:
            part = int(part)
            if part <0 or part>255:
                errors = labels[i] + "byte invalid"
        except:
            errors = labels[i] + "byte invalid"

    if errors != len(0):
        for err in errors:
            print(err)
    else:
        print("ip valid")

user_ip = input('enter ip ' )
validate_ip(user_ip)