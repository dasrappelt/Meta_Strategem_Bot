import subprocess
import shlex
import platform


def RateSentiment(sentiString):
    cmd = "java -jar /Users/philipprapp/Documents/Projekte/Coding/Twitter-Bot/Meta-Bot/SentiStrength_Data/SentiStrength.jar stdin sentidata /Users/philipprapp/Documents/Projekte/Coding/Twitter-Bot/Meta-Bot/SentiStrength_Data/"

    if platform.system() ==	'Windows':
      cmd = "java -jar SentiStrength_Data/SentiStrength.jar stdin sentidata SentiStrength_Data/"

    p = subprocess.Popen(shlex.split(cmd), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         shell=False)

    b = bytes(sentiString.replace(" ", "+"), 'utf-8')
    stdout_byte, stderr_text = p.communicate(b)

    stdout_text = stdout_byte.decode("utf-8")

    stdout_text = stdout_text.rstrip().replace("\t", ",")
    stdout_text = stdout_text.split(",")
    return stdout_text
