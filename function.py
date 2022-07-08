import enum
properties={
    'data':
    {
        'properties':
        [
            {
            'name':'ram',
            'rank':'1',
            'contact':['abc@gmail.com','5456544']
            },
            {
            
            'name':'sita',
            'rank':'2',
            'contact':['efg@gmail.com','654654']                
            }
        ]
    },"total_count":2,
}
s=properties.get('data').get('properties')
for i in s:
    print("**********************************************************")
    print(f"Name: {i.get('name')}")
    print(f"Rank:{i.get('rank')}")
    for index,j in enumerate(i.get('contact'),1):
        print(f"Contact {index}: {j}")


        








