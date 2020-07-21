class HashTable:
    def __init__(self,size):
        self.size=size
        self.buckets=self.create_buckets()

    def create_buckets(self):
        return [[] for i in range(self.size)]

    def initial_insert(self):
        with open('KeyValuePair.txt') as file:
            for line in file:
                [key,value]=line.split(' : ')
                k=self.search(key)
                if k[0]==False:
                    bucket=hash(key)%self.size
                    self.buckets[bucket].append((key, value.rstrip()))
        return 'All Values Inserted'

    def insert_pair(self,email,value):
        k=self.search(email)
        if k[0]==False:
            bucket=hash(email)%self.size
            self.buckets[bucket].append((email,value))
            return 'Value Inserted Successfully at index {}\
'.format(bucket)
        else:
            return 'Your mentioned key already has value \
associated to it.Modification Not Allowed'

    def search(self,key):
        bucket=hash(key)%self.size
        for key_check,value in self.buckets[bucket]:
            if key==key_check:
                return True,value
        return False,'{} Not Found'.format(key)

    def modification(self,key,value):
        k=self.search(key)
        if k[0]==False:
            return "This key doesn't exists so can't be modified"
        else:
            bucket=hash(key)%self.size
            for i,j in self.buckets[bucket]:
                if key==i:
                    self.buckets[bucket].remove((i,j))
                    self.buckets[bucket].append((key,value))
                    return "Modification Successfully Completed"

hash_table=HashTable(256)
hash_table.initial_insert()
print(hash_table.insert_pair('bishwas@gmail.com','Software Engineer'))
print(hash_table.insert_pair('bishwas@gmail.com','Engineer'))
print(hash_table.modification('bishwas@gmail.com','Engineer'))
print(hash_table.search('qglljxr@gmail.com'))
print(hash_table.search('bishwas@gmail.com'))
print(hash_table.search('bissdfss@gmail.com'))
