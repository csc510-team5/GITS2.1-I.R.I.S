import os

# create a doskey file to be referenced by registory
macrosFile = open("macros.doskey", "w")
# add alias for gits command
n = macrosFile.write("gits=python \"" + os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "\code\gits.py\" $*")
macrosFile.close()

# create a directory gits specific records
gitPath = os.path.join(os.getcwd(), ".gits")
os.mkdir(gitPath)

# create a directory inside .gits for logs
logPath = os.path.join(gitPath, "logs")
os.mkdir(logPath)

# create a batch file to create necessary directories and doskey file
autoRunFile = open("autoRun.bat", "w")
n = autoRunFile.write("reg add \"HKEY_LOCAL_MACHINE\Software\Microsoft\Command Processor\" /v Autorun /d \"doskey /macrofile=" + os.getcwd() + "\macros.doskey\" /f")
autoRunFile.close()
