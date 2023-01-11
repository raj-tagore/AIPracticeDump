import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

'''subject = "this is my first test email"
email={}
email['Subject'] = subject
email['From'] = 'noreply.leader.factory@gmail.com'
email['To'] = 'usernamerajtagore@gmail.com'
s = smtplib.SMTP('smtp.gmail.com', 587)
s.connect("smtp.gmail.com",587)
s.ehlo()
s.starttls()
s.ehlo()
s.login('noreply.leader.factory@gmail.com', 'noreplyLF1234')
s.sendmail('usernamerajtagore@gmail.com', 'usernamerajtagore@gmail.com', subject)
s.quit()'''


def SendMail(Subject, TextContent, HtmlContent, Recipient):
	Email= MIMEMultipart("alternative")
	Email['Subject'] = Subject
	Email['From'] = 'noreply.leader.factory@gmail.com'
	Email['To'] = Recipient

	ConvertedText = MIMEText(Text, 'plain')
	ConvertedHTML = MIMEText(HTML, 'html')
	Email.attach(ConvertedText)
	Email.attach(ConvertedHTML)

	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.connect("smtp.gmail.com",587)
	s.ehlo()
	s.starttls()
	s.ehlo()
	s.login('noreply.leader.factory@gmail.com', 'noreplyLF1234')
	s.sendmail('noreply.leader.factory@gmail.com', Recipient, Email.as_string())
	s.quit()

Subject = "test4"

Text = """
		Thank You, Mr. {name}
		Your order has been successfully placed
		Details:
		{course Name}
		Price: Rs. {price}
		Your order will be delivered in {time}
		"""

HTML = """
		<html>
		<head>
		<style>
		h1 {text-align: center;}
		h2 {text-align : center;}
		h4 {text-align: left;}
		body {text-align: center;}
		.left {text-align: left;}
		.row {background-color: lightyellow;}
		.ProductPic {float: left;
		            width: 30%;
		            padding: 10px;}
		.ProductInfo {float: right;
		            width: 60%;
		            padding: 10px;
		            text-align: left;}
		.row::after {content: '';
		            clear: both;
		            display: table;}
		</style>
		</head>
		<body>
		<h1>Thank You</h1>
		<h3>Mr. {participant Name}</h3>
		<h3>Your order has been successfully placed</h3>
		<h4>Order Details:</h4>
		<div class="row">
		    <div class="ProductPic">
		    <img src="C:/Users/Raj Tagore/Pictures/Screenshots/onlineCourse.png" alt="" width= 100%> 
		    </div>
		    <div class="ProductInfo">
		    <p><h3 class="left">{CourseName}</h3></p>
		    <p>{about course} a;cen;aoc n;aeon cernvks ubyvkeuarvbe ukveuveuk vekucva kuvy rae ukcv</p>
		    <p>price: {price}</p>
		    </div>
		</div>
		<br><br>

		</body>
		</html> """

SendMail(Subject, Text, HTML, 'usernamerajtagore@gmail.com')