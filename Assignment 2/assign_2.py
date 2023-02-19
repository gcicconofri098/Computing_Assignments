import math
LIGHT_SPEED = 1

class Particle:
    def __init__(self, name, mass, charge, momentum =0.): 
        self._name = name
        self._mass= mass
        self._charge = charge
        self.momentum = momentum #non metto _momentum perché in questo modo l'input chiama il setter, che controlla se l'impulso messo nella definizione è fisico oppure no
        
    def info(self):
        msg = 'particle "{}" of mass {:.3f} MeV/c^2, charge: {}, momentum {:.3f}'
        return msg.format(self.name, self.mass, self.charge, self.momentum)
    @property
    def name(self):
        return self._name
    
    @property
    def mass(self):
        return self._mass
    
    
    @property
    def charge(self):
        return self._charge


    @property
    def momentum(self):
        return self._momentum
    @momentum.setter
    def momentum(self, momentum):
        if momentum < 0:
            print("Not a physical momentum")
            self._momentum = 0 #senza questa la property non avrebbe momentum definito
        else:
            self._momentum = momentum

    @property
    def energy(self):
        return math.sqrt(self.mass**2 + self.momentum**2)
        
    @energy.setter
    def energy(self, energy):
        if energy < self.mass:
            print('Cannot set the energy to a value lower tan the mass')
        else:
            self.momentum = math.sqrt(energy**2 - self.mass**2)
    @property
    def beta(self):
        return LIGHT_SPEED * self.momentum/self.energy
    @beta.setter
    def beta(self, beta):
        if(beta<0 or beta>1):
            print("Invalid value of beta")
            self.beta=0
        else:
            self.momentum = beta * self.energy
            
    @property
    def gamma(self):
        return 1/(math.sqrt(1- self.beta**2))
    
    @gamma.setter
    def gamma(self, gamma):
        if(gamma<1.):
            print("Invalid value of gamma")
            self._gamma=1
        else:
            self.momentum= self.energy* math.sqrt(1- 1/(gamma)**2)
        
    
class Proton(Particle):
    
    NAME = 'Proton'
    MASS = 938.5
    CHARGE = 1  
        
    def __init__(self, momentum=0.):
        super().__init__(self.NAME, self.MASS, self.CHARGE, momentum)

class Alpha(Particle):
    
    NAME = 'Alpha particle'
    MASS = 3780
    CHARGE = 0

    def __init__(self, momentum=0.):
        super().__init__(self.NAME, self.MASS, self.CHARGE, momentum)
    
'''
particle = Particle('Muon', 105.6,-1)
print(particle.info())
particle.energy= 200
print("particle energy: {:.2f}".format(particle.energy))
particle.energy= 100
print("particle energy: {:.2f}".format(particle.energy))
print(particle.momentum)
particle.momentum=-19
print(particle.momentum)


'''
proton= Proton(-100.)
print(proton.info())
proton.beta= 0.9
print(proton.info())
alpha= Alpha(20.)
alpha.gamma= 1000.
print(alpha.info())
print(alpha.momentum)
