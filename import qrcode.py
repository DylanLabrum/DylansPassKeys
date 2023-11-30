import qrcode

# Generate QR code for Google account sign-in
google_account = "example@gmail.com"
google_qr = qrcode.make(google_account)
google_qr.save("google_qr.png")

# Generate QR code for Microsoft account sign-in
microsoft_account = "example@hotmail.com"
microsoft_qr = qrcode.make(microsoft_account)
microsoft_qr.save("microsoft_qr.png")

# Generate QR code for Apple ID passkey
apple_id = "example@apple.com"
apple_qr = qrcode.make(apple_id)
apple_qr.save("apple_qr.png")
