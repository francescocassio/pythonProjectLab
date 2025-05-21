import mysql.connector

def esegui_query_insert(query, valori):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ecommerce"
    )

    cursor = conn.cursor()

    cursor.execute(query, valori)
    conn.commit()

    print(f"{cursor.rowcount} record inserito.")

    cursor.close()
    conn.close()

def query_select(query, valori):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ecommerce"
    )

    cursor = conn.cursor(dictionary=True)

    cursor.execute(query, valori)
    risultati = cursor.fetchall()

    cursor.close()
    conn.close()

    return risultati


def login_utente():
    nome_utente = input("Inserisci nome utente: ")
    password = input("Inserisci password: ")

    q = "SELECT * from utenti where username = %s and pswd = %s"
    v = (nome_utente, password)

    risultato = query_select(q, v)

    # print(risultato)

    if len(risultato) == 0:
        print("Utente non esistente o password errata")
        return -1
    else:
        print(f"Benvenuto {risultato[0]['username']}")
        print(f"Hai accesso come {risultato[0]['ruolo']}")

        return risultato[0]

def menu_cliente():
    print("1) Visualizza saldo")
    print("2) Ricarica credito")
    print("3) Visualizza prodotti")
    print("4) Acquista prodotto")
    print("5) Visualizza storico acquisti")
    print("6) Logout")


def menu_start():
    print("1) Registra utente cliente")
    print("2) Registra utente admin")
    print("3) Login utente")
    print("4) Esci")

def menu_admin():
    pass

def registra_utente_cliente():
    nome_utente = input("Inserisci nome utente: ")
    password = input("Inserisci password: ")

    q = "insert into utenti(username, pswd, ruolo) VALUES (%s, %s, %s);"
    v = (nome_utente, password, "cliente")

    esegui_query_insert(q, v)


if __name__ == '__main__':
    while True:
        menu_start()
        scelta_start = int(input("Scelta: "))

        if scelta_start == 1:
            registra_utente_cliente()
        elif scelta_start == 2:
            pass
        elif scelta_start == 3:
            risultato = login_utente()

            if risultato != -1:
                if risultato['ruolo'] == "admin":
                    menu_admin()
                else:
                    while True:
                        menu_cliente()

                        scelta_cliente = int(input("Scelta: "))

                        if scelta_cliente == 1:
                            pass
                        elif scelta_cliente == 2:
                            pass
                        elif scelta_cliente == 6:
                            break


        elif scelta_start == 4:
            break


