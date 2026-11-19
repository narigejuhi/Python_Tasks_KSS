
##13. Secure Login System (Decorators) 
##A web application wants to ensure that users are authenticated before accessing 
##sensitive functions. Create a decorator that checks whether the user is logged in before 
##allowing access to a function.


def login_required(func):
    def wrapper(is_logged_in):
        if is_logged_in:
            return func()
        else:
            print("Please login first")

    return wrapper

@login_required
def dashbord():
    print("welcome to Dashbord")

dashbord(True)
dashbord(False)
