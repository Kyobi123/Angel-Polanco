# hash
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_users(n):
    users = {}

    print("\n=== REGISTRO DE USUARIOS ===")
    for i in range(n):
        print(f"\nUsuario #{i+1}")
        username = input("Nombre de usuario: ")
        name = input("Nombre real: ")
        age = int(input("Edad: "))
        password = input("Contraseña: ")

        hashed = hash_password(password)  

        users[username] = {
            "name": name,
            "age": age,
            "password_hash": hashed
        }

    return users

def search_user(users, username):
    if username in users:
        return users[username]
    return None

if __name__ == "__main__":
    print("=== SISTEMA DE USUARIOS CON BÚSQUEDA HASH ===")

    n = int(input("¿Cuántos usuarios deseas registrar? "))

    user_table = register_users(n)

    print("\n=== BUSCAR USUARIO ===")
    username = input("Ingresa el usuario a buscar: ")

    result = search_user(user_table, username)

    if result:
        print("\nUsuario encontrado:")
        print("Nombre:", result["name"])
        print("Edad:", result["age"])
        print("Contraseña (HASH):", result["password_hash"])
    else:
        print("\n❌ Usuario no encontrado.")