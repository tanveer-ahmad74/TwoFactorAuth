# TwoFactorAuth

1. First you have to create a user use this endpoint: http://localhost:8000/user/
2. Then you have to generate otp using http://localhost:8000/get-otp/
3. After that you have to copy that otp and hit this endpoint http://localhost:8000/verify/ that otp 
but make sure when you create user make sure you are login to that use other wise it will get you message mobile number does not exist.
The one thing is that you can only 4 times otp per day. i handle these request using throttle. 
