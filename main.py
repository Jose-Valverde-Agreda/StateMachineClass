class SM:
    def start(self):
        # Toda clase hijo tendrá un estado inicial llamado startState
        self.state = self.startState

    def step(self, inp):
        # El método getNExtValues es un método genérico
        # dependerá de la clase hijo que lo llame
        (s, o) = self.getNextValues(self.state, inp)
        self.state = s 
        return o

    def transduce(self, inputs):
        self.start()
        return [self.step(inp) for inp in inputs]

class Turnstile(SM):
    # Todas las clases hijo iniciaran con este estado, es por
    # es que no se le pone SELF
    startState = 'locked'

    def getNextValues(self, state, inp):
        if inp == 'coin':
            return ('unlocked', 'enter')
        elif inp == 'turn':
            return ('locked', 'pay')
        elif state == 'locked':
            return ('locked', 'pay')
        else:
            return ('unlocked', 'enter')

testInputs = [None, 'coin', None, 'turn', 'turn', 'coin', 'coin']
ts = Turnstile()
print(ts.transduce(testInputs))