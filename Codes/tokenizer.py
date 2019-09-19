import re
import sys

if __name__ == "__main__":
    regex_word = r"[a-zA-Z]+"
    regex_punt = r"[\-\,\.;\'\`\"\?!”“’]|(&amp;)|\/" # can check for ellipses using \u2026|(\.\.\.) but not sure if the test cases consider ellipses as separate punctuation 
    regex_email = r"[a-zA_Z0-9#$_\-]+(?:\.[a-zA-Z0-9#$_\-]+)*@(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?"
    regex_url = r"(http://)?(https://)?(ftp://)?(www\.)?[^\s/$\.?#]+\.[^\.\s]{1,}[^\s]+"       
    regex_currency = r"[$₹€£¥\+\-]*[0-9,.]+[$₹€£¥]*"      
    regex_name = r"[A-Z][a-z]+"       
    regex_hashtag = r"#[a-zA-Z_0-9$\-]+"      
    regex_mention = r"@[a-zA-Z0-9$_\-]+"
    all_regex = re.compile("(%s|%s|%s|%s|%s|%s|%s|%s)" % (regex_punt, regex_hashtag, regex_mention, regex_url, regex_email, regex_currency, regex_name, regex_word))
    if len(sys.argv)<2:
        print("Error! Enter name of file to parse")
        print("Program will exit")
        sys.exit()
    file_name =  sys.argv[1]
    # print("Reading from file:",file_name)
    tok_list = []
    last_line = None
    with open(file_name, 'r') as fll:
        last_line = fll.readlines()[-1]
    with open(file_name, 'r') as fh:
        for line in fh:
            tokenised_list = []
            tok_list.append(all_regex.finditer(line))
            for iters in tok_list:
                for match in iters:
                    tokenised_list.append(match.span())
            tokenised_list = list(set(tokenised_list))
            tokenised_list.sort()
            indexes = []
            for tokens in tokenised_list:
                start = tokens[0]
                end = tokens[1]
                if end not in indexes:
                    indexes.append(start)
                    indexes.append(end)

            indexes.sort()
            # print(line,end='')
            # print(indexes)
            for i in range(0,len(indexes)-1,2):
                # print(indexes[i],indexes[i+1])
                if i+1==len(indexes)-1:
                    print(line[indexes[i]:indexes[i+1]],sep='',end='')
                else:
                    print(line[indexes[i]:indexes[i+1]],sep='',end=' ')
            # To print trailing whitespaces if required
            # r = len(line)-2
            # while(line[r]==' ' or line[r]=='\t'):
            #     print(line[r],sep='',end='')
            #     r -= 1
            if line != last_line:
                print("")
