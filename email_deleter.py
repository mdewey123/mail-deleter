

import imaplib
import email


def deleteMail():
    mailbox = input('mail service (ex. "gmail.com"): ')
    account = input("email: ")
    password = input("password: ")
    date = input('Date DD-MMM-YYYY (ex: 24-DEC-2025): ') 
    mail = imaplib.IMAP4_SSL(f'imap.{mailbox}', 993)
    mail.login(account, password)
    mail.select('"[Gmail]/All Mail"')

    result, search_results = mail.search(None, f'UNSEEN BEFORE {date}')

    if result != "OK":
        print('Search Error')
        return  

    email_ids = search_results[0].split()
    print("Raw email IDs:", email_ids)
    
    if not email_ids:
        print("No applicable mails")
        return

    print(f'{len(email_ids)} are staged for deletion')

    for email_id in email_ids:
        print(f'flagging {email_id}')       
        mail.store(email_id, '+X-GM-LABELS', '\\Trash')
        
    
    print('emails marked for removal')
    
    delete_check = input(f' type "y" to delete {len(email_ids)} from inbox Or type "n" to cancel... ')

    if delete_check == "y":
        mail.expunge()
        mail.select("[Gmail]/Bin")
        print('Deleted')
        mail.logout()
        print('logged out')
        return
    elif delete_check == "n":
        print('clearing data and logging out')
        
        mail.logout()
        print('logged out')
        return
    else:
        print('invalid input')
        delete_check


deleteMail()