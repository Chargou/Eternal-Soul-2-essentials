# Made by Chargou (@chargou on dc, @GGames78 on roblox)
# Go to line 59 and modify N to simulate N rolls
# You can use https://www.online-python.com/ to run this if you don't have python :)

class Rolls():
    def __init__(self, F=0, E=0, D=0, C=0, B=0, A=0, S=0, SS=0, SSS=0, Z=0):
        self.F, self.E, self.D, self.C, self.B, self.A, self.S, self.SS, self.SSS, self.Z = round(F/100, 5), round(E/100, 5), round(D/100, 5), round(C/100, 5), round(B/100, 5), round(A/100, 5), round(S/100, 5), round(SS/100, 5), round(SSS/100, 5), round(Z/100, 5)
    
    def __add__(self, o):
        return Rolls((self.F+o.F)*100, (self.E+o.E)*100, (self.D+o.D)*100, (self.C+o.C)*100, (self.B+o.B)*100, (self.A+o.A)*100, (self.S+o.S)*100, (self.SS+o.SS)*100, (self.SSS+o.SSS)*100, (self.Z+o.Z)*100)
    
    def __str__(self):
        return f"F={self.F}\nE={self.E}\nD={self.D}\nC={self.C}\nB={self.B}\nA={self.A}\nS={self.S}\nSS={self.SS}\nSSS={self.SSS}\nZ={self.Z}"
    
    def __mul__(self, n):
        return Rolls(self.F*n*100, self.E*n*100, self.D*n*100, self.C*n*100, self.B*n*100, self.A*n*100, self.S*n*100, self.SS*n*100, self.SSS*n*100, self.Z*n*100)
    
    def crafted(self):
        F, E, D, C, B, A, S, SS, SSS, Z = self.F, self.E, self.D, self.C, self.B, self.A, self.S, self.SS, self.SSS, self.Z
        E += F//5
        F = F%5
        D += E//5
        E = E%5
        C += D//5
        D = D%5
        B += C//5
        C = C%5
        A += B//5
        B = B%5
        S += A//5
        A = A%5
        SS += S//5
        S = S%5
        SSS += SS//5
        SS = SS%5
        return Rolls(F*100, E*100, D*100, C*100, B*100, A*100, S*100, SS*100, SSS*100, Z*100)

roll_1 = Rolls(45,30,15,7,2.2,0.7,0.09,0.009,0.001)
roll_10th = Rolls(0,0,62,32,4.5,1,0.4,0.09,0.01)
roll_100th = Rolls(0,0,0,0,95,4,0.5,0.4,0.1)
roll_750th = Rolls(0,0,0,0,0,0,70,25,5,0.5)

roll_9 = roll_1*9
roll_10 = roll_9 + roll_10th
roll_49 = roll_10*4+roll_9
roll_90 = roll_10*9
roll_99 = roll_90 + roll_9
roll_100 = roll_99 + roll_100th
roll_750 = roll_100*7+roll_49+roll_750th
roll_800 = roll_750 + roll_49+roll_100th
roll_1500 = roll_100*14 + roll_99 + roll_750th*2
roll_150000 = roll_1500*100
for_1_Z = roll_150000.crafted()


###############################################
###############################################
###############################################
N = 10000 # Modify here to simulate N rolls ! #
###############################################
###############################################
###############################################

result = Rolls()
result = result + roll_1500 * (N//1500)
N %= 1500
result = result + roll_800 * (N//800)
N %= 800
result = result + roll_750 * (N//750)
N %= 750
result = result + roll_100 * (N//100)
N %= 100
result = result + roll_10 * (N//10)
N %= 10
result = result + roll_1 * (N//1)
N %= 1
print(result.crafted())