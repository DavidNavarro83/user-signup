from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)


@app.route("/signup", methods=['GET'])
def get_signup():
    return render_template('signup.html')


@app.route("/signup", methods=['POST'])
def signup():
    # look inside the request to figure out what the user typed
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    # print('\nthe username sent in was =' + username)
    # print('the password sent in was =' + password)
    # print('the verify sent in was =' + verify)
    # print('the email sent in was =' + email)

    username_error = False
    password_error = False
    verify_error = False
    email_error = False

    if username == '' or len(username) < 3 or len(username) > 20 or ' ' in username:
        username_error = True

    if password == '' or len(password) < 3 or len(password) > 20 or ' ' in password:
        password_error = True

    if verify != password:
        verify_error = True

    if len(email) > 0 and ( len(email) < 3 or len(email) > 20 or ' ' in email or email.count('@') != 1 or email.count('.') != 1):
        email_error = True

    if username_error or email_error or verify_error or password_error:
        return render_template('signup.html', username_text=username, email_text=email, email_error=email_error, verify_error=verify_error, password_error=password_error, username_error=username_error)

    return render_template('welcome.html', username=username)


@app.route("/")
def index():
    return redirect('/signup')

if __name__ == "__main__":
    app.run()
