from admin import Admin as Ad

my_admin = Ad(first_name="Hieu", last_name="Le", age=20, location="Viet Nam", logon_attempts=0, privileges=['Can post','can write','can edit'])
my_admin.describe_user()
my_admin.greet_user()
my_admin.privileges.show_privileges()