class animals(object):
    def run(self):
        print ('animals is running')

class dog(animals):
    pass

def run_twice(animals):
    animals.run()

class tortoise(object):
    def run(self):
        print('start')

run_twice(tortoise())

