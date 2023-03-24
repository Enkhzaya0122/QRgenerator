resultMessages = {
    200 : 'Success',
    201 : 'Ok',
#   successCode

    400 : "Error",
    401 : "Failed",
#   errorCode
}
#   resultMessages

webSite = 'http://127.0.0.1:8000/'

mailContent = {
"validate_mail_subject" : 'Welcome to QR code generator',
"validate_mail_content1" : '''Эрхэм хэрэглэгч танд энэ өдрийн мэнд хүргэе!

Та QR code generator-д амжилттай бүртгэгдлээ.

Бидэнтэй холбоо барих:
Веб хаяг: https://mandakh.edu.mn/''',
#   validate_mail_subject

"forgotPassword_mail_subject" : 'QR code generator Password сэргээх',
"forgotPassword_mail_content1" : '''Эрхэм хэрэглэгч танд энэ өдрийн мэнд хүргэе!
Та QR code generator-ийн password солих бол доорх link-ээр хандана уу .
''' + webSite +"?codes=",
"forgotPassword_mail_content2" : '''Бидэнтэй холбоо барих:
Веб хаяг: https://mandakh.edu.mn/''',
} 
#   mailContent

dbname ='qrcodegenerator',
user ='qruser',
host='202.131.254.138',
password='qrcode1234',
port=5938,  

EMAIL_SENDER = 'mtaxapp@zohomail.com'
PASS_SENDER = 'N32sH@fGn2NtZAn'

