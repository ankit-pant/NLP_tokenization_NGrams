import re
import sys

if __name__ == "__main__":
    regex_word = re.compile(r"[a-zA-Z]+")
    regex_punt = re.compile(r"[,.;''""]")
    regex_email = re.compile(r"email")
    regex_url = re.compile(r"url")
    regex_currency = re.compile(r"currency")        
    regex_name = re.compile(r"name")        
    regex_hashtag = re.compile(r"#")        
    regex_mention = re.compile(r"@") 
    if len(sys.argv)<2:
        print("Error! Enter name of file to parse")
        print("Program will exit")
        sys.exit()
    file_name =  sys.argv[1]
    print("Reading from file:",file_name)
    