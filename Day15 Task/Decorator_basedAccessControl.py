##8. Decorator-based Access Control 
##Scenario: 
##Restrict access to certain functions. 
##Task: 
##● Create a decorator to check user role 
##● Use condition inside decorator 
##● Apply decorator to multiple functions 
##● Store roles in a dictionary


roles = {
    "Juhi": "admin",
    "Ravi": "user",
    "Priya": "manager"
}

current_user = "Juhi"


def check_role(required_role):

    def decorator(func):

        def wrapper():

            user_role = roles.get(current_user)

            if user_role == required_role:
                func()
            else:
                print("Access Denied!")

        return wrapper

    return decorator


@check_role("admin")
def delete_data():
    print("Admin can delete data")


@check_role("manager")
def view_report():
    print("Manager can view report")


delete_data()
view_report()
