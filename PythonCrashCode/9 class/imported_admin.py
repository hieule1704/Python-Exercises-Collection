import admin

admin_1 = admin.Admin("John", "Doe", 25, "New York",0,["can add post","can delete post","can ban user"])
admin_1.describe_user()
admin_1.privileges.show_privileges()