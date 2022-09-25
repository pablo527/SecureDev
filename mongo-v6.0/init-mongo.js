db.createUser(
    {
        user: "security",
        pwd: "secrect",
        roles: [
            {
                role: "readWrite",
                db: "my_db"
            }
        ]
    }
);
db.createCollection("ips"); //MongoDB creates the database when you first store data in that database