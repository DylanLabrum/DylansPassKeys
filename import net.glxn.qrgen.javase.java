import net.glxn.qrgen.javase.QRCode;

// Generate QR code for Google account sign-in
String googleAccount = "example@gmail.com";
QRCode.from(googleAccount).file("google_qr.png");

// Generate QR code for Microsoft account sign-in
String microsoftAccount = "example@hotmail.com";
QRCode.from(microsoftAccount).file("microsoft_qr.png");

// Generate QR code for Apple ID passkey
String appleId = "example@apple.com";
QRCode.from(appleId).file("apple_qr.png");
