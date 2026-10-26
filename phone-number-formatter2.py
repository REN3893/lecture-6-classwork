def digit_sum(text):
    count =0
    for i in text:
        if(48<=ord(i)<=57):
            count += ord(i)-48
    return count


a = input('Phone number: ')
a = a.strip()
count = 0
for i in a :
    if(i!=' '):
        count += 1
bool1=False
if(a[0]=='0'):
    bool1=True
    
if(bool1 and count==10):
    print('Formatted: '+a.replace(' ','-'))
    print('Hidden: '+a.replace(' ','-')[:4]+('X'*3)+a.replace(' ','-')[7:])
    print('Digit sum:', digit_sum(a))
else:
    print('Invalid phone number')