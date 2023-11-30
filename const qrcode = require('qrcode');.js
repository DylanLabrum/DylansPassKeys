const qrcode = require('qrcode');

// Generate QR code for Google account sign-in
const googleAccount = "example@gmail.com";
qrcode.toFile('google_qr.png', googleAccount);

// Generate QR code for Microsoft account sign-in
const microsoftAccount = "example@hotmail.com";
qrcode.toFile('microsoft_qr.png', microsoftAccount);

// Generate QR code for Apple ID passkey
const appleId = "example@apple.com";
qrcode.toFile('apple_qr.png', appleId);
