import os
os.system('cls') or None

print("\n Bem-vindo --------------- ")
entrada = int(input('\n Digite o tempo (em S):'))
dias        = entrada // (24 * 60 * 60)

resto       = entrada % (24* 60 * 60)
horas       = resto // (60 * 60)

resto       = resto % (60 * 60)
minutos     = resto // 60

resto       = resto %  60
segundos    = resto

print('\n São', dias,'dia(s,', horas, 'hora(s),', minutos, 'minutos e', segundos, 'segundos')
print('\n ------------------------------- \n')