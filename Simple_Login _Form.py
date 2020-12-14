import hashlib
import getpass
files = ['1:6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', '2:d4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35' , '3:4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce','4:4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a','5:ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d']
op = 'y'
while op == 'y':
    log = str(input(
        "Login (l)  Signup (s)    Change Username/password (c)   Delete Account (d)  Search Username (f)  Press Your Options  :"))

    if log == 's':
        adminpassword = "240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9"
        adminname = "admin"
        root = adminname + adminpassword
        useradmin = input("Enter Administrator Name     :")
        encodedPassword = hashlib.sha256(getpass.getpass(prompt="Enter Admin Password : ").encode())
        passadmin = encodedPassword.hexdigest()
        troot = useradmin + passadmin
        if troot == root:
            newuser = input("Enter New User Name    :")

            encodedUserPassword = hashlib.sha256(getpass.getpass("Enter Password     :").encode())
            newpass = encodedUserPassword.hexdigest()

            encodedUserConfPassword = hashlib.sha256(getpass.getpass("Confirm Password     :").encode())
            newpass1 = encodedUserConfPassword.hexdigest()
            if newpass == newpass1:
                print("Password Confirmed")
                print("New User added")
                new = str(newuser + ":" + newpass1)
                files = files + [new]
                print(files)
            else:
                print("Password nor match !!! please Try agian!!!")

        else:
            print("Administrator Incorrect!!")

    elif log == 'l':
        print("Login Your Account")
        username = input("Enter Your Username")
        result = hashlib.sha256(getpass.getpasst("Enter Your Password").encode())
        password = result.hexdigest()
        total = username + ":" + password
        lenpass = str(len(password))
        print("Length of Password is :" + lenpass)
        key = "no"
        print("Your name is :" + username)
        lenfiles = len(files)
        print("Lenght of files is   :" + str(lenfiles))
        for x in files:
            if total == x:
                key = "yes"
                break


            else:
                key = "no"
        if key == "yes":
            print("Login Successufull")
        else:
            print("Login Incorrect")
    elif log == 'c':
        print('Login Your Account')
        username = input("Enter Your Username")
        result = hashlib.sha256(getpass.getpass("Enter Your Password").encode())
        password = result.hexdigest()
        total = username + ":" + password
        lenpass = str(len(password))
        print("Length of Password is :" + lenpass)
        key = "no"
        print("Your name is :" + username)
        lenfiles = len(files)
        print("Lenght of files is" + str(lenfiles))
        i = -1
        for x in files:
            i = i + 1
            if total == x:
                key = "yes"
                break



            else:
                key = "no"
        if key == "yes":
            print("Login Successufull")
            print("")
            cname = input("Enter new Userame    :")
            resultcpass = hashlib.sha256(getpass.getpass("Enter new password   :").encode())
            cpass = resultcpass.hexdigest()
            resultcpass1 = hashlib.sha256(getpass.getpass("Confirm your password   :").encode())
            cpass1 = resultcpass1.hexdigest()
            if cpass == cpass1:
                print("Username is  :" + cname)
                print("Password is Confirmed")
                caccount = cname + ':' + cpass
                files[i] = caccount
                print("New Username & Password are added")

            else:
                print("Password not match !!!")
                exit(0)
        else:
            print("Login Incorrect")
            exit(0)
    elif log == 'd':
        if len(files) == 0:
            print("users are empty try Signup !!!")
        else:
            print("Login Your Account")
            username = input("Enter Your Username")
            resultdpass = hashlib.sha256(getpass.getpass("Enter Your Password").encode())
            password = resultdpass.hexdigest()
            total = username + ":" + password
            lenpass = str(len(password))
            print("Length of Password is :" + lenpass)
            key = "no"
            print("Your name is :" + username)
            lenfiles = len(files)
            print("Lenght of files is   :" + str(lenfiles))
            i = -1
            for x in files:
                i = i + 1
                if total == x:
                    key = "yes"
                    break


                else:
                    key = "no"
            if key == "yes":
                print("Login Successufull")
                print("Deleting Your Acoount")
                print(files)

                del files[i]
                print(files)
                print("Account Deleted")

            else:
                print("Login Incorrect")

    elif log == 'f':
        name = input('Enter Username want to Search     :')
        lenofname = len(name)
        key = 'no'
        i = 0
        for a in files:
            k = a
            for k in a:
                if a[0:lenofname] == name:
                    key = 'yes'
                    print("Found")
                    break
            if key == 'yes':
                break
        if key == 'no':
            print('NOT FOUND')

    else:
        print('Invaild Option Select an Option From')
        print('Login (l)  Signup (s)    Change Username/password (c) Delete Account (d)')

    op = input('Do you want to continue : press "y" or "n"  :')
    if op != ('y'):
        exit(0)

# Author :Mohamed Ansaf;mail:ansafmattathur@gmail.com;followmeoninstagram:anu_ansaf.3;
