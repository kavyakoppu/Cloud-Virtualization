# CloudVirtualization1
## Dynamic Website using Cloud Virtualization
This application will validate the input number is a prime or not.

Create a folder at your convenient location and clone the repository.
Sign in to your AWS Account.
Follow the User guide documentation to launch Amazon EC2 Linux Instance.
[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html#ec2-launch-instance]
Once your instance is in running state, check if the status checks are passed. Then, connect to your instance using putty.
[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html]
Set up WinSCP to transfer files to your Linux instance. Steps are provided in the above link.
Once connected to WinSCP, transfer the project folder CloudVirtualization1 to /home/ec2-user/
Now, set the current directory to /home/ec2-user/CloudVirtualization1/ in EC2 Console opened via putty.
`cd /home/ec2-user/CloudVirtualization1/`

Run `sudo python app.py`
Now, Flask starts serving your app at port 80 by default.
`app.run(host="0.0.0.0", port = 80)`

Once your web server is up and running, use your public ip to access the homepage.
This can be fetched from Description tab of Instances screen in EC2 console.

**************

## Enabling HTTPS :
Generate a Self-signed Certificate using Openssl.
`openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -keyout prime.key -out prime.crt`
Set SSL Context in app.py
`app.run(host="0.0.0.0", port=443, ssl_context=('prime.crt','prime.key'))`
Make sure your security group associated to your instance allows inbound access for HTTPS via Port 443.