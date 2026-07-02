import smtplib as s

# Connect to Gmail SMTP server
ob = s.SMTP("smtp.gmail.com", 587)
ob.ehlo()
ob.starttls()

# Login using your Gmail and App Password
ob.login("saumyadasqwerty@gmail.com", "uprd qkmq hojx ygks")

# Take input from the user
subject = input("Enter Subject: ")
body = input("Enter Message: ")

# Create email
message = f"Subject: {subject}\n\n{body}"

# List of recipients
listadd = [
    "prajapatgaurav08@gmail.com",
    "dassaumya13@gmail.com",
    "ssaumyaddas21@gmail.com"
]

# Send email
ob.sendmail("saumyadasqwerty@gmail.com", listadd, message)

print("Email Sent Successfully!")

# Close connection
ob.quit()