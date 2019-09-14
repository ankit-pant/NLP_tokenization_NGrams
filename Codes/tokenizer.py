import re
import sys

if __name__ == "__main__":
    regex_word = re.compile(r"[a-zA-Z]+")
    regex_punt = re.compile(r"[\-\,\.;\'\`\"\?!]")
    regex_email = re.compile(r"[a-z0-9#$_\-]+(?:\.[a-z0-9#$_\-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?",re.IGNORECASE)
    regex_url = re.compile(r"(http://)?(https://)?(ftp://)?(www\.)?[^\s/$.?#]*\.[^\s]+")         
    regex_currency = re.compile(r"[$₹€£¥\+\-]*[0-9,.]+[$₹€£¥]*")        
    regex_name = re.compile(r"[A-Z][a-z]+")        
    regex_hashtag = re.compile(r"#[a-zA-Z_0-9$\-]+")        
    regex_mention = re.compile(r"@[a-zA-Z0-9$_\-]+") 
    # all_regex = re.compile(regex_punt '|' regex_word '|' regex_email '|' regex_url '|' regex_currency '|' regex_name '|' regex_hashtag '|' regex_mention)
    if len(sys.argv)<2:
        print("Error! Enter name of file to parse")
        print("Program will exit")
        sys.exit()
    file_name =  sys.argv[1]
    # print("Reading from file:",file_name)
    word_list = []
    punc_list = []
    email_list = []
    url_list = []
    currency_list = []
    name_list = []
    hashtag_list = []
    mention_list = []
    # tok_list = []
    with open(file_name, 'r') as fh:
        for line in fh:
            # tok_list.append(all_regex.finditer(line))
            tokenised_list = []
            # iter = re.finditer(regex_word,line)
            # if iter:
            #     word_list.append(iter)
            # else:
            #     iter = re.finditer(regex_punt,line)
            #     if iter:
            #         punc_list.append
            # iter = re.finditer(regex_word,line)
            # if iter:
            #     word_list.append(iter)
            #     continue
            hashtag_list.append(re.finditer(regex_hashtag,line))
            mention_list.append(re.finditer(regex_mention,line))
            word_list.append(re.finditer(regex_word,line))
            punc_list.append(re.finditer(regex_punt,line))
            email_list.append(re.finditer(regex_email,line))
            url_list.append(re.finditer(regex_url,line))
            currency_list.append(re.finditer(regex_currency,line))
            name_list.append(re.finditer(regex_name,line))

            for iters in word_list:
                for match in iters:
                    tokenised_list.append(match.span())
            for iters in name_list:
                for match in iters:
                    tokenised_list.append(match.span())
            for iters in hashtag_list:
                for match in iters:
                    tokenised_list.append(match.span())
            for iters in mention_list:
                for match in iters:
                   tokenised_list.append(match.span())
            for iters in punc_list:
                for match in iters:
                    tokenised_list.append(match.span()) 
            for iters in email_list:
                for match in iters:
                    tokenised_list.append(match.span())
            for iters in url_list:
                for match in iters:
                    tokenised_list.append(match.span())
            for iters in currency_list:
                for match in iters:
                    tokenised_list.append(match.span())
            # for iters in tok_list:
            #     for match in iters:
            #         tokenised_list.append(match.span())
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
            print(line,end='')
            # print(indexes)
            for i in range(0,len(indexes)-1,2):
                # print(indexes[i],indexes[i+1])
                if i+1==len(indexes):
                    if line[indexes[i]]!='\n':
                        print(line[indexes[i]],sep='',end=' ')
                else:
                    print(line[indexes[i]:indexes[i+1]],sep='',end=' ')
            print("")
            print("")
            

    