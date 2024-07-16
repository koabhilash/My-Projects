def caesar_cipher():
    k=int(input('Enter the key: '))
    t=input('Enter Encrypt for encryption or Decrypt for decryption: ')
    me=input('Enter the message: ')
    indx=[]
    r=[]
    m=me.lower()
    a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if t=='Encrypt':
        for j in range(0,len(m)):
            indx.append((a.index(m[j])+k)%26)    #c=(p+k)%26
            r.append(a[indx[j]])
        for i in range(0,len(r)):
            print(r[i],end=' ')
    elif t=='Decrypt':
        for j in range(0,len(m)):
            indx.append((a.index(m[j])-k)%26)   #p=(c-k)%26
            r.append(a[indx[j]])
        for i in range(0,len(r)):
            print(r[i],end=' ')
    else:
        print('Invalid entry..!')
    q=input('\nEnter yes if you want to continue and no to stop: ')
    if q=='yes':
        caesar_cipher()
caesar_cipher()
    
