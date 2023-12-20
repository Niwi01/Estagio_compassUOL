class Calculo:
    
    def soma(self,x,y):
        return x+y
        
    def sub(self,x,y):
        return x-y
        
su = Calculo()

print(f'Somando:4+5 = {su.soma(4,5)}')
print(f'Subtraindo:4-5 = {su.sub(4,5)}')