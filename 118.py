def email_slicer():
    email = input("Enter your email address: ")

    if "@" not in email or "." not in email:
        print("Invalid email address!")
        return
    
    username, domain = email.split("@")
    domain_name, extension = domain.split(".")

    print(f"Username: {username}")
    print(f"Domain: {domain_name}")
    print(f"Extension: {extension}")

email_slicer()
