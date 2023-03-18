import subprocess
import getpass

subprocess.Popen(f'"C:/Program Files/MySQL/MySQL Workbench 8.0/"mysql --user=root --password={getpass.getpass()} < E:/world.sql', shell=True)