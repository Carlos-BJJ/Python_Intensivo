users = {
    "goat" : {
         "first_name" : "Anderson",
         "last_name" : "Silva",
         "Born_in" : "Brasil"
     },

     "Sujo" : {
              "first_name" : "Jon",
              "last_name" : "Jones",
              "Born_in" : "USA"
          }
}

for username, user_info in users.items():
    print(f"\nUsername : {username}")
    full_name = f"{user_info["first_name"]} {user_info["last_name"]}"
    born = user_info["Born_in"]

    print(f"\t{full_name}")
    print(f"\t{born}")