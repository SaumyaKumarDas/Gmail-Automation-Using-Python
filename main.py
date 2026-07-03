import smtplib as s

# Connect to Gmail SMTP Server
ob = s.SMTP("smtp.gmail.com", 587)
ob.ehlo()
ob.starttls()

# Login
ob.login("saumyadasqwerty@gmail.com", "wmqq wqub ngpm buyk")

# Inputs
subject = input("Enter Subject: ")

print("Enter your message (type 'END' on a new line when done):")
lines = []
while True:
    line = input()
    if line.strip() == "END":
        break
    lines.append(line)

body = "\n".join(lines)

# Create Email
message = f"Subject: {subject}\n\n{body}"

# Recipients
listadd = [
    "prajapatgaurav08@gmail.com",
    "dassaumya13@gmail.com",
    "ssaumyaddas21@gmail.com"
]

# Send Email (only once to all recipients)
ob.sendmail("saumyadasqwerty@gmail.com", listadd, message)

print("Email Sent Successfully!")

ob.quit()